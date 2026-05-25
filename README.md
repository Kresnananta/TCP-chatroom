# TCP Chatroom

Program ini adalah aplikasi chatroom sederhana berbasis TCP menggunakan Python. Aplikasi terdiri dari satu server dan beberapa client. Server bertugas menerima koneksi dari client, membaca pesan yang dikirim, lalu meneruskan pesan tersebut ke client lain yang sedang terhubung.

Project ini dibuat menggunakan library bawaan Python, yaitu `socket` untuk komunikasi jaringan dan `threading` untuk menangani beberapa koneksi secara bersamaan.

## Fitur

- Multi-client chatroom menggunakan protokol TCP.
- Server dapat menerima beberapa client secara bersamaan.
- Pesan dari satu client akan dikirim ke client lain.
- Notifikasi saat client masuk atau keluar dari chatroom.
- Client dapat menerima pesan sambil tetap bisa mengetik pesan baru.
- Command `/exit` atau `/quit` untuk keluar dari client dengan rapi.
- Server dapat dimatikan dengan `Ctrl+C`.

## Struktur File

```text
TCP-con/
|-- client.py
|-- server.py
`-- README.md
```

Keterangan:

- `server.py`: Program server utama yang menerima koneksi client dan melakukan broadcast pesan.
- `client.py`: Program client yang digunakan untuk masuk ke chatroom dan mengirim pesan.
- `README.md`: Dokumentasi project.

## Kebutuhan

- Python 3.x
- Terminal atau command prompt
- Jika ingin digunakan oleh beberapa PC, semua PC sebaiknya berada dalam jaringan lokal yang sama, misalnya WiFi yang sama.

## Konfigurasi

Konfigurasi server terdapat di `server.py`:

```python
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 12000
MAX_CLIENTS = 3
```

Keterangan:

- `SERVER_HOST = '0.0.0.0'` berarti server menerima koneksi dari semua alamat jaringan yang tersedia di komputer server.
- `SERVER_PORT = 12000` adalah port yang digunakan untuk komunikasi client dan server.
- `MAX_CLIENTS = 3` adalah jumlah maksimal koneksi client yang dapat masuk ke antrean koneksi server.

Konfigurasi client terdapat di `client.py`:

```python
SERVER_HOST = 'localhost'
SERVER_PORT = 12000
```

Jika client dijalankan di PC yang sama dengan server, gunakan:

```python
SERVER_HOST = 'localhost'
```

Jika client dijalankan dari PC lain dalam jaringan yang sama, ganti `SERVER_HOST` dengan IP address komputer yang menjalankan server, misalnya:

```python
SERVER_HOST = '192.168.1.10'
```

## Cara Menjalankan di Satu PC

1. Buka terminal pertama, lalu jalankan server:

   ```bash
   python server.py
   ```

2. Buka terminal kedua, lalu jalankan client:

   ```bash
   python client.py
   ```

3. Untuk menambahkan client lain, buka terminal baru lagi dan jalankan:

   ```bash
   python client.py
   ```

## Cara Menjalankan di Beberapa PC

1. Jalankan `server.py` di PC yang akan dijadikan server:

   ```bash
   python server.py
   ```

2. Cari IP address PC server.

   Di Windows, jalankan:

   ```powershell
   ipconfig
   ```

   Lihat bagian `IPv4 Address`, misalnya:

   ```text
   192.168.1.10
   ```

3. Pada PC client, ubah `SERVER_HOST` di `client.py` menjadi IP address PC server:

   ```python
   SERVER_HOST = '192.168.1.10'
   ```

4. Jalankan client:

   ```bash
   python client.py
   ```

Catatan: jika koneksi dari PC lain gagal, pastikan firewall pada PC server mengizinkan koneksi masuk ke port `12000`.

## Command Client

Saat berada di chatroom, client dapat mengetik pesan biasa untuk dikirim ke client lain.

Untuk keluar dari chatroom, gunakan salah satu command berikut:

```text
/exit
/quit
```

## Cara Mematikan Server

Untuk menghentikan server, tekan:

```text
Ctrl+C
```

Server akan menutup socket dan menghentikan program.

## Alur Kerja Singkat

```text
Client 1  ----\
               \
                Server ---- meneruskan pesan ke client lain
               /
Client 2  ----/
```

Alur komunikasi:

1. Server dijalankan dan menunggu koneksi.
2. Client terhubung ke server.
3. Server memberi notifikasi bahwa client baru telah masuk.
4. Client mengirim pesan ke server.
5. Server meneruskan pesan tersebut ke client lain.
6. Saat client keluar, server memberi notifikasi ke client lain.

## Catatan Firewall

Untuk penggunaan dalam jaringan lokal, biasanya tidak diperlukan port forwarding. Namun, firewall di PC server mungkin perlu mengizinkan koneksi masuk ke port `12000`.

Port forwarding hanya diperlukan jika client ingin terhubung dari luar jaringan lokal, misalnya dari jaringan internet yang berbeda.

## Teknologi yang Digunakan

- Python
- TCP socket
- Threading
