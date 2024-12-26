import os
import sys
import json
import httpx
import asyncio
import httpx_ws
from colorama import Fore, Style
from datetime import datetime


black = Fore.LIGHTBLACK_EX
green = Fore.LIGHTGREEN_EX
blue = Fore.LIGHTBLUE_EX
red = Fore.LIGHTRED_EX
white = Fore.LIGHTWHITE_EX
magenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.LIGHTYELLOW_EX
reset = Style.RESET_ALL


class TeneoXD:
    def __init__(self, no, ping_interval, max_retry):
        self.wss_url = "wss://secure.ws.teneo.pro/websocket"
        self.no = no
        self.ping_interval
        self.max_retry = max_retry

    def log(self, msg):
        now = datetime.now().isoformat(" ").split(".")[0]
        print(f"{black}[{now}]{reset} {blue}[{self.no}]{reset} {msg}{reset}")

    async def connect(self, userid, proxy=None):

        retry = 1
        headers = {
            "Host": "secure.ws.teneo.pro",
            "Connection": "Upgrade",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
            "Upgrade": "websocket",
            "Origin": "chrome-extension://emcclcoaglgcpoognfiggmhnhgabppkm",
            "Sec-WebSocket-Version": "13",
            "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
            "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
        }
        while True:
            try:
                if retry >= self.max_retry:
                    self.log(f"{yellow}max retrying reacted, try again later 1")
                    return
                async with httpx.AsyncClient(headers=headers, proxy=proxy) as client:
                    async with httpx_ws.aconnect_ws(
                        url=f"{self.wss_url}?userId={userid}&version=v0.2",
                        client=client,
                    ) as wss:
                        retry = 1
                        self.log(f"{green}connect to {white}websocket {green}server")
                        while True:
                            msg = await wss.receive_json(timeout=10)
                            point_today = msg.get("pointsToday")
                            point_total = msg.get("pointsTotal")
                            self.log(
                                f"{green}point today : {white}{point_today} {magenta}| {green}point total : {white}{point_total}"
                            )
                            for i in range(90):
                                await wss.send_json({"type": "PING"})
                                self.log(f"{white}send {green}PING {white}server !")
                                await countdown(self.ping_interval)
            except Exception as e:
                self.log(f"{red}error : {white}{e}")
                retry += 1
                continue


async def countdown(t):
    for i in range(t, 0, -1):
        minute, seconds = divmod(i, 60)
        hour, minute = divmod(minute, 60)
        seconds = str(seconds).zfill(2)
        minute = str(minute).zfill(2)
        hour = str(hour).zfill(2)
        print(f"waiting for {hour}:{minute}:{seconds} ", flush=True, end="\r")
        await asyncio.sleep(1)


def get_proxy(id, proxies):
    if len(proxies) <= 0:
        return None
    proxy = proxies[id % len(proxies)]
    if "http" not in proxy:
        proxy = "http://" + proxy
    if "socks5" in proxy:
        print("not support socks5 protocol !")
        return None
    return proxy


async def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        f"""
    {magenta}╔═╗╔╦╗╔═╗  {green}╔═╗┬─┐┌─┐ ┬┌─┐┌─┐┌┬┐
    {magenta}╚═╗ ║║╚═╗  {green}╠═╝├┬┘│ │ │├┤ │   │ 
    {magenta}╚═╝═╩╝╚═╝  {green}╩  ┴└─└─┘└┘└─┘└─┘ ┴ 
    
    {green}Github: {white}github.com/AkasakaID
          """
    )
    if not os.path.exists("userids.txt"):
        print(f"{red}error: {white}userid.txt file is not found !")
        exit()
    userids = open("userids.txt").read().splitlines()
    proxies = open("proxies.txt").read().splitlines()
    configs = open("config.json").read()
    config = json.loads(configs)
    interval = config.get("ping_interval", 10)
    max_retry = config.get("max_retry", 10)
    tasks = []
    for no, id in enumerate(userids):
        proxy = get_proxy(no, proxies)
        tasks.append(
            asyncio.create_task(
                TeneoXD(no=no + 1, ping_interval=interval, max_retry=max_retry).connect(
                    userid=id, proxy=proxy
                )
            )
        )
        print(f"preparing tasks-{no} ", flush=True, end="\r")
    print("                         ", flush=True, end="\r")

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    try:
        if os.name == "nt":
            loop = asyncio.ProactorEventLoop()
            asyncio.set_event_loop(loop=loop)
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    except KeyboardInterrupt:
        exit()
