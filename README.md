# GoalHub

Link: [https://yafi-alifuddin-goalhub.pbp.cs.ui.ac.id/](https://yafi-alifuddin-goalhub.pbp.cs.ui.ac.id/)

# Tugas 2: Implementasi Model-View-Template (MVT) pada Django

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

sumber: Materi Perkuliahan PBP 03 - MTV Django Architecture (https://scele.cs.ui.ac.id/pluginfile.php/269605/mod_resource/content/1/03%20-%20MTV%20Django%20Architecture.pdf)

**Penjelasan:**

* `urls.py` Berfungsi sebagai pemetaan URL. Ketika ada HTTP request dari browser, Django akan mencocokkan URL yang diminta dengan daftar path di urls.py. Jika cocok, request diteruskan ke fungsi yang sesuai di `views.py`.
* `views.py` berisi logika utama dari aplikasi, juga sebagai jembatan antara URLS dan templates. Fungsi view menerima request dari `urls.py`, memprosesnya, dan bisa Mengambil/menyimpan data ke database melalui `models.py`, Mengolah data dan meneruskannya ke template (berkas HTML), serta Mengembalikan HTTP response ke browser
* `models.py` Berisi definisi struktur data (model database). View akan membaca atau menulis data ke database melalui model ini.
* Template (HTML) berisi tampilan halaman web. View akan me-render template ini, mengisi data yang diperlukan, lalu mengirim hasil akhirnya sebagai HTTP response ke browser.

**Kesimpulan:**
`urls.py` mengarahkan request ke `views.py`, `views.py` bisa berinteraksi dengan `models.py` untuk data, lalu me-render template HTML dan mengirim hasilnya ke user.

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


# Tugas 3: Implementasi Form dan Data Delivery pada Django

### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery diperlukan dalam pengimplementasian sebuah platform karena menjadi mekanisme utama pertukaran informasi antara klien dan server, memungkinkan aplikasi menampilkan dan memperbarui data secara dinamis. Dengan data delivery, data dapat dikirim dan diterima secara efisien, aman, serta dapat dipahami oleh berbagai sistem yang saling terintegrasi, misalnya saat berkomunikasi dengan API eksternal. Selain itu, juga membuat pengguna memperoleh pengalaman interaktif tanpa perlu memuat ulang halaman penuh, sekaligus menghemat bandwidth dan meningkatkan skalabilitas. Tanpa data delivery, platform tidak dapat menyediakan informasi real-time, integrasi layanan pihak ketiga, maupun kontrol akses yang memadai bagi penggunanya.

### 2.  Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya, JSON lebih baik dari XML karena formatnya lebih ringkas, mudah dibaca, dan langsung cocok dengan struktur objek pada bahasa pemrograman populer seperti JavaScript, Python, atau Java. JSON memiliki struktur sederhana berbentuk key-value pairs, mirip dengan dictionary di Python. Hal ini membuat JSON lebih mudah dibaca dan dipahami oleh manusia, sekaligus lebih mudah diolah oleh mesin. Sebaliknya, XML punya aturan penulisan yang lebih panjang dan berulang karena setiap elemen harus punya tag pembuka dan penutup, sehingga ukuran datanya lebih besar dan proses membacanya butuh waktu lebih lama. Meskipun XML masih dipakai ketika dibutuhkan fitur khusus seperti skema yang ketat atau dokumen dengan struktur kompleks. JSON lebih populer karena efisiensi, kemudahan integrasi dengan API, serta dukungan luas di ekosistem web modern.

### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Dalam Django, method is_valid() digunakan untuk memeriksa apakah data yang dikirim melalui form sesuai dengan aturan validasi yang telah didefinisikan pada form tersebut. Ketika pengguna mengirimkan form, Django akan menampung data itu di objek form. Pemanggilan form.is_valid() akan menjalankan serangkaian pengecekan otomatis: memastikan setiap field terisi dengan benar (misal tipe data, panjang teks, dsb.), menjalankan cleaning atau validasi tambahan yang kita tulis sendiri, dan menandai hasilnya dengan nilai True jika semua data lolos, atau False jika ada kesalahan. Kita membutuhkan method ini karena hanya data yang sudah dipastikan valid yang aman untuk diproses lebih lanjut, seperti disimpan ke database atau dikirim ke layanan lain. Tanpa method is_valid(), kita berisiko menyimpan data yang salah format, kosong, atau berpotensi menimbulkan bug dan masalah keamanan pada aplikasi Django.

### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token adalah mekanisme pelindung dari serangan Cross-Site Request Forgery (CSRF). Token ini berupa nilai acak yang unik untuk setiap sesi pengguna dan disisipkan ke dalam setiap form HTML yang mengirim data dengan metode POST (atau request yang mengubah data). Saat form dikirim, server akan memeriksa apakah token yang diterima sama dengan token yang sebelumnya diberikan ke pengguna tersebut. Jika kita tidak menambahkan csrf_token, server tidak bisa memastikan bahwa permintaan benar-benar berasal dari pengguna yang sah. Akibatnya, penyerang bisa memanfaatkan celah ini dengan membuat website atau link palsu yang secara diam-diam mengirim permintaan ke server atas nama korban yang sedang login. Jadi, csrf_token mencegah serangan di mana penyerang menipu browser korban untuk menjalankan aksi yang merugikan tanpa sepengetahuan korban, menjaga integritas dan keamanan data pada aplikasi.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Berikut langkah-langkah yang saya lakukan:
1. Membuat direktori templates baru yang berisi base.html, kemudian menambahkannya ke settings.py supaya terdeteksi sebagai template
2. Membuat forms.py di dalam direktori main berisi ProductForm dengan field sesuai yang dibutuhkan ketika menambahkan produk
3. Menambahkan fungsi di views.py untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID. Juga dengan fungsi untuk menambahkan dan menampilkan produk
4. Melakukan konfigurasi di urls.py di dalam direktori main dengan membuat routing URL untuk masing-masing views yang telah ditambahkan 
5. Menambahkan isi main.html di dalam direktori main/templates dengan menambahkan button add product yang akan redirect ke halaman form untuk menambahkan product, menambahkan button detail untuk melihat detail penjelasan produk, dan meyesuaikan tampilan di halaman utama
6. Membuat berkas baru di dalam direktori main/templates, yaitu create_product.html sebagai halaman untuk menambahkan produk baru dan product_details.html untuk menampilkan penjelasan lengkap produk 

### 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Asdos sudah responsif dan sangat membantu ketika saya mengalami kesulitan di tutorial 2

### Screenshot dari hasil akses URL pada Postman
1. XML
https://github.com/Yalifuddin/GoalHub/blob/master/Screenshot%20(164).png

2. JSON
https://github.com/Yalifuddin/GoalHub/blob/master/Screenshot%20(165).png

3. XML by ID
https://github.com/Yalifuddin/GoalHub/blob/master/Screenshot%20(167).png

4. JSON by ID
https://github.com/Yalifuddin/GoalHub/blob/master/Screenshot%20(166).png

---

Sekian, Terimakasih

Yafi Alifuddin