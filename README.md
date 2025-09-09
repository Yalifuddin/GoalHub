# Tugas 2: Implementasi Model-View-Template (MVT) pada Django

# GoalHub

Link: [https://yafi-alifuddin-goalhub.pbp.cs.ui.ac.id/](https://yafi-alifuddin-goalhub.pbp.cs.ui.ac.id/)

---

## Jawaban dari Pertanyaan Tugas

### 1. Implementasi Checklist Step by Step

Saya memulai pengerjaan tugas ini secara bertahap sebagai berikut:

1. Membuat direktori untuk mengerjakan tugas 
2. Melakukan Inisialisasi Git di dalam direktori tersebut
3. membuat dan mengaktifkan virtual environment
4. Menambahkan dependencies ke 'requirements.txt' dan lakukan instalasi
5. Membuat proyek django 
6. Melakukan konfigurasi pada '.env' dan '.env.prod'
7. Melakukan konfigurasi pada 'settings.py'
8. Membuat repository baru di GitHub
9. Menambahkan berkas '.gitignore'
10. Menghubungkan repo lokal dengan github yang telah dibuat dan membuat branch utama
11. Melakukan Melakukan `git add`, `commit`, dan `push` ke GitHub.
12. Membuat proyek baru di PWS dan melakukan deploy awal
13. Membuat aplikasi baru bernama 'main' dan menambahkannya ke dalam INSTALLED_APPS di 'settings.py'
14. Membuat folder 'templates' di dalam 'main' dan mengisinya dengan berkas 'main.html'
15. Melakukan konfigurasi di 'models.py' dengan membuat class Product yang isinya tupple CATEGORY_CHOICES (kategori yang tersedia dalam toko), inisiasi attribute yang diperlukan, dan membuat beberapa fungsi.
16. Melakukan migrasi model untuk merefleksikan perubahan pada 'models.py'
17. Membuat function show_main di 'views.py' supaya bisa terintegrasi dengan templates
18. Membuat file urls.py di direktori main berisi konfigurasi routing untuk aplikasi main dan melakukan konfigurasi pada urls.py di direktori GoalHub supaya dapat melakukan pemetaan
19. Cek tampilan dengan menjalankan server
20. Melakukan push lagi ke GitHub dan PWS

---

### 2. Bagan Alur Request dan Response Django
<img alt="image" src="https://github.com/Yalifuddin/GoalHub/blob/c5979a5905171b259b430b7b48163b211326e890/image.png" />

sumber: Materi Perkuliahan PBP 02 - Introduction to the Internet and Web Framework (https://scele.cs.ui.ac.id/pluginfile.php/268491/mod_resource/content/1/02%20-%20Introduction%20to%20the%20Internet%20and%20Web%20Framework.pdf)

**Penjelasan:**

* `urls.py` menerima request dari client, kemudian mencocokkan URL yang diakses di browser dengan daftar path yang ada.
* Jika cocok, request diarahkan ke fungsi di `views.py`.
* `views.py` berisi logika utama dari aplikasi, juga sebagai jembatan antara URLS dan templates.
* Jika `views.py` membutuhkan data, maka akan memanggil `models.py`.
* Jika `views.py` membutuhkan tampilan, maka akan mme-render file HTML yang ada di templates.
* Browser akhirnya menerima `HTTP response` berupa halaman web.

---

### 3. Peran `settings.py`

File `settings.py` di proyek Django berperan sebagai pusat konfigurasi utama untuk seluruh aplikasi Django. Semua pengaturan penting yang memengaruhi cara kerja proyek didefinisikan di sini, seperti:

* **Konfigurasi Database**: menentukan jenis databse yang digunakan.
* **Installed Apps**: menentukan daftar aplikasi yang aktif dalam proyek.
* **Pengaturan Template dan Static Files**: mengatur lokasi dan cara Django mencari file HTML template.
* **Pengaturan Static Files**: mengatur lokasi file statis seperti CSS, JavaScript, dan gambar.
* **Keamanan**: Menyimpan secret key, pengaturan debug, dan daftar host yang diizinkan (ALLOWED_HOSTS). 

---

### 4. Cara Kerja Migrasi Database di Django

Migrasi database adalah cara Django melacak perubahan pada database. Migrasi ini adalah instruksi untuk mengubah struktur tabel basis data sesuai dengan perubahan model yang didefinisikan dalam kode terbaru.

* `makemigrations` → menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data.
* `migrate` → mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data dengan menjalankan perintah sebelumnya.

Dengan migrasi, perubahan database dapat dilakukan secara bertahap tanpa kehilangan data lama, dan semua perubahan tercatat rapi. 

---

### 5. Mengapa Django Dijadikan Permulaan?

Menurut saya, Django dipilih karena:

* Menggunakan bahasa Python, bahasa pemrograman yang mudah dipelajari, populer, dan banyak digunakan di dunia industri maupun akademik.
* Memiliki struktur proyek yang jelas dan terorganisir, sehingga pemula dapat belajar membangun aplikasi web dengan rapi dan sistematis.
* Dokumentasinya sangat lengkap dan komunitasnya besar, sehingga mudah mencari solusi jika mengalami kendala.
* Fitur lengkap bawaan (*batteries included*), menyediakan banyak fitur bawaan seperti autentikasi, admin panel, ORM, form handling, hingga keamanan dasar. Sehingga pemula tidak perlu ribet menginstal banyak library tambahan untuk membuat aplikasi web dasar, jadi bisa fokus pada konsep inti pengembangan web tanpa harus membangun semuanya dari nol.
* Menerapkan *best practice* seperti prinsip DRY (*Don’t Repeat Yourself*). Hal ini membentuk kebiasaan baik sejak awal belajar.
* Aman, skalabel, lintas platform, serta sudah terbukti digunakan oleh banyak perusahaan besar.

---

### 6. Feedback untuk Asisten Dosen

Menurut saya, tutorial 1 sudah sangat bagus. Panduannya jelas dan mudah dimengerti, setiap bagian dijelaskan dengan baik sehingga saya bisa memahami apa yang dilakukan.

---

Sekian, Terimakasih

Yafi Alifuddin