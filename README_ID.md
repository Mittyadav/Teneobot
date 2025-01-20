# TeneoXd

Untuk kalian yang malas aktif selama 24/7

# Fitur

- [x] Multi akun
- [x] Mendukung penggunaan proxy (Hanya protocol HTTP)

# Cara menggunakan

1. Pastikan dikomputer kamu sudah terinstall python dan git.

2. Clone repository ini
   
	```
	git clone https://github.com/akasakaid/teneoxd
	```

3. Masuk ke folder teneoxd
   
   ```
   cd teneoxd
   ```

4. Ini langkah opsional, membuat virtualenv
   
   Windows
   ```
   python/py -m venv env
   ```

   Linux
   ```
   python3 -m venv env
   ```

   Kemudian aktifkan virtualenv 

   Windows
   ```
   env\scripts\activate
   ```

   Linux
   ```
   source env/bin/activate
   ```

5. Install library yang dibutuhkan
   ```
   pip install -r requirements.txt
   ```
6. Masukkan akses token akun kalian ke file `data.txt`
   
   [Cara mendapatkan Akses Token Akun](#Cara-Mendapatkan-Akses-Token)

7. Edit `config.json` jika anda ingin mengubah config,berikut tabel penjelasan isi `config.json`
   
   | key           | description                    | value       |
   | ------------- | ------------------------------ | ----------- |
   | ping_interval | waktu tunggu/jeda antar ping   | harus angka |
   | max_retry     | maksimal uji coba ketika error | harus angka |

8. Jika kalian ingin menggunakan proxy maka masukkan proxy kalian ke file `proxies.txt`, format proxy yang digunakan adalah seperti berikut :
   
   Jika diharuskan memakai autentikasi

   `protocol://user:password@host:port`

   contoh

   `http://admin:admin@127.0.0.1:8000`

   Jika tidak memakai autentikasi

   `protocol://host:port`

   contoh:

   `http://127.0.0.1:8000`

9.  Setelah semua itu selanjutnya kalian hanya perlu menjalankan `main.py`
    ```
    python main.py
    ```

# Cara mendapatkan Akses Token

1. Masuk ke halaman dashboard teneo
   
   [https://dashboard.teneo.pro/](https://dashboard.teneo.pro/)

2. Buka devtool, kalian bisa menekan tombol f11/f12 atau klik kanan -> inspect element.

3. Masuk ke menu console

4. Ketikan `allow pasting` agar bisa melakukan paste kode javascript

5. Paste kode javascript berikut ke menu console

   ```
   copy(localStorage.getItem('accessToken'))
   ```

6. Kemudian paste / ctrol + v karena kode javascript diatas memiliki fungsi untuk mencopy dan memasukkan akses token ke clipboard perangkat kalian. Jika akses token tidak muncul atau tidak muncul apapun ketika di paste maka ada yang salah dengan aksi yang kalian lakukan.

7. Paste akses token ke file `data.txt`

# Traktir saya kopi

- Indonesia : [https://trakteer.id/fawwazthoerif/tip](https://trakteer.id/fawwazthoerif/tip)
- Internasional : [https://sociabuzz.com/fawwazthoerif/tribe](https://sociabuzz.com/fawwazthoerif/tribe)

# Terima kasih