# TeneoXd

For those who don't want to stay active 24/7

README bahasa indonesia : [README_ID.md](README_ID.md)

# Features

- [x] Multiple accounts
- [x] Proxy support (HTTP protocol only)

# How to Use

1. Make sure Python and Git are installed on your computer.

2. Clone this repository
   
   ```
   git clone https://github.com/akasakaid/teneoxd
   ```

3. Enter the teneoxd folder
   
   ```
   cd teneoxd
   ```

4. This is an optional step, creating virtualenv
   
   Windows
   ```
   python/py -m venv env
   ```

   Linux
   ```
   python3 -m venv env
   ```

   then enable virtualenv 

   Windows
   ```
   env\scripts\activate
   ```

   Linux
   ```
   source env/bin/activate
   ```
5. Install required libraries
   ```
   pip install -r requirements.txt
   ```

6. Enter your account userids into the `userids.txt` file
   
   You can get your account userid by running the `login.py` file which will automatically fill your account userid into the `userids.txt` file when successful.

7. Edit `config.json` if you want to change the config, here's an explanation table for `config.json` contents
   
   | key           | description                   | value            |
   | ------------- | ----------------------------- | ---------------- |
   | ping_interval | wait time/delay between pings | must be number   |
   | max_retry     | maximum retries when error    | must be a number |

8. If you want to use a proxy, enter your proxy into the `proxies.txt` file, the proxy format used is as follows:
   
   If authentication is required

   `protocol://user:password@host:port`

   example:

   `http://admin:admin@127.0.0.1:8000`

   If no authentication is needed

   `protocol://host:port`

   example:

   `http://127.0.0.1:8000`

9. After all that, you just need to run `main.py`
   ```
   python main.py
   ```

# Buy me a coffee

- Indonesia: [https://trakteer.id/fawwazthoerif/tip](https://trakteer.id/fawwazthoerif/tip)
- International: [https://sociabuzz.com/fawwazthoerif/tribe](https://sociabuzz.com/fawwazthoerif/tribe)

# Thank you