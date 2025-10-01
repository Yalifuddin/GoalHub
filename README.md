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
<img alt="image" src="https://github.com/Yalifuddin/GoalHub/blob/master/img/image.png" />

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

---

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
<img alt="image" src="https://github.com/Yalifuddin/GoalHub/blob/master/img/Screenshot%20(164).png" />

2. JSON
<img alt="image" src="https://github.com/Yalifuddin/GoalHub/blob/master/img/Screenshot%20(165).png" />

3. XML by ID
<img alt="image" src="https://github.com/Yalifuddin/GoalHub/blob/master/img/Screenshot%20(167).png" />

4. JSON by ID
<img alt="image" src="https://github.com/Yalifuddin/GoalHub/blob/master/img/Screenshot%20(166).png" />

---

# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django

### 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

AuthenticationForm adalah form bawaan Django yang digunakan untuk menangani proses login user. Fungsinya untuk memverifikasi kredensial (username & password) pengguna saat login. 
Kelebihan:
1. Terintegrasi penuh dengan sistem auth Django: Tidak perlu menulis validasi manual; otomatis mengecek hash password di model User
2. Perlindungan keamanan bawaan: Mendukung mekanisme keamanan bawaan Django (misalnya hashing password, CSRF, dll).
3. Validasi & error message otomatis: Jika username atau password salah, form akan memberikan error message standar seperti “Please enter a correct username and password” tanpa harus ditulis ulang.
4. Mudah dikustomisasi tampilan: Bisa di‐override label, widget, atau field tambahan.
Kekurangan:
1. Terbatas pada field standar: Hanya menyediakan username dan password. Kalau butuh login dengan email atau kombinasi lain, perlu subclassing/override.
2. Pengalaman pengguna standar: Tidak menyertakan fitur tambahan seperti “remember me”, login sosial (Google/Facebook), 2FA (two-factor authentication), atau login via OAuthjadi harus menambahkannya sendiri/manual.
3. Tidak mengatur alur login penuh: Hanya form, developer tetap harus mengatur view/URL dan template.

### 2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

Autentikasi: Tujuannya melakukan verifikasi terhadap pengguna (login), sebagai verifikasi awal (gerbang awal). Implementasi di django:
1. Form & Validasi: AuthenticationForm otomatis memvalidasi username & password dengan data di database.
2. Session Management: login(request, user) menyimpan ID user di session; Django men-set cookie session yang aman.
3. Logout: Fungsi logout_user memanggil logout(request) untuk menghapus session dan delete_cookie('last_login') agar jejak login terakhir hilang.
Otorisasi: Tujuannya melakukan verifikasi apa saja yang boleh dilakukan atau bisa diakses oleh pengguna, dilakuakn setelah identitas pengguna terverifikasi (autentikasi berhasil). Implementasi di django:
1. Decorator @login_required: Menjadi “gerbang” sebelum view dijalankan. Jika user belum login, otomatis diarahkan ke /login.
2. Filter data per user: Memastikan user hanya melihat produk yang dia miliki (contoh otorisasi berbasis data/row-level).

### 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Session: 
- Kelebihan: 
1. Lebih aman karena data sensitif (misalnya info user) tidak dikirim ke klien. Hanya ID acak yang disimpan di browser. Di Django, session ID otomatis di-hash dan dilindungi CSRF.
2. Bisa menyimpan lebih banyak informasi, karena ukuran data yang tak terbatas
3. Manajemen terpusat: Server bisa menghapus atau mengubah state kapan saja (misal paksa logout semua user).
4. Integrasi Django otomatis: request.session membuat penyimpanan dan pengambilan data sederhana.
- Kekurangan:
1. Beban server lebih besar karena semua data disimpan di sisi server sehingga butuh database/penyimpanan dan memori tambahan.
2. Session yang tidak dihapus bisa menumpuk sehingga perlu mekanisme pembersihan (Django biasanya pakai job cleanup).
3. Ketergantungan cookie untuk ID: Jika user menonaktifkan cookie, session tidak dapat dilacak.
Cookies:
- Kelebihan:
1. Semua data disimpan dan dikelola di sisi klien, sehingga tidak membebani server
2. Persisten di klien: Bisa disetel dengan waktu kadaluwarsa panjang → cocok untuk “remember me” atau preferensi UI.
3. Implementasi sederhana: Cukup set header Set-Cookie atau gunakan response.set_cookie() (seperti last_login).
- Kekurangan:
1. Ukuran terbatas: Sekitar 4 KB per cookie, jumlah cookie per domain juga dibatasi.
2. Risiko keamanan lebih tinggi: Bisa dibaca/diubah user, Rentan terhadap pencurian (misal cross-site scripting), Perlu proteksi HttpOnly, Secure, dan enkripsi bila menyimpan informasi penting.
3. Terkirim di setiap request: Menambah overhead jaringan jika data cookie besar.

### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Secara default cookies adalah potongan data polos yang dikirim bolak-balik antara browser dan server, sehingga ada beberapa risiko yang perlu diwaspadai:
1. Pencurian Cookie (Cookie Theft): Jika koneksi tidak terenkripsi (HTTP), cookie bisa disadap (sniffing). Penyerang bisa memakai cookie curian untuk session hijacking.
2. Cross-Site Scripting (XSS): Jika aplikasi rentan XSS, skrip berbahaya di browser dapat membaca/mengirim cookie ke pihak ketiga.
3. Cross-Site Request Forgery (CSRF): Penyerang memanfaatkan cookie yang otomatis dikirim browser untuk mengeksekusi aksi tanpa sepengetahuan user.
4. Cookie Manipulation: Data dalam cookie dapat diubah pengguna jika tidak dienkripsi/diberi tanda tangan.
Cara Django menangani hal tersebut:
1. HttpOnly: menandai cookie agar tidak dapat diakses lewat JavaScript, menekan risiko XSS.
2. Secure: memaksa pengiriman cookie hanya lewat HTTPS agar tidak bisa disadap.
3. CSRF Middleware + Token: mencegah Cross-Site Request Forgery yang memanfaatkan cookie secara otomatis.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat form dan fungsi registrasi, login, serta logout di views.py
2. Membuat berkas html untuk registrasi dan loginn di dalam main/templates untuk menampilkan halaman register dan login
3. Menambahkan button di main.html
4. Menambahkan fungsi yang telah dibuat dan path ke urls.py dalam direktori main
5. Menambahkan decorator @login_required pada fungsi show_main dan show_product di views.py untuk merestriksi
6. Menghubungkan product dengan user
7. Melakukan migrasi models
8. Memodifikasi fungsi create_product di views.py agar bisa assign user ke produk yang dibuat.
9. Menambahkan filtering di main page
10. Memodifikasi detail product agar menampilkan username user yang menambahkannya.
11. Menambahkan cookies: menyimpan cookies saat login, menghapus cookies saat logout, serta menampilkan last login di main page.
12. Menampilkan username yang sedang login di main page
13. Melakukan python manage.py runserver dan mencoba untuk membuat user dan menambahkan product untuk masin-masing user
14. Melakukan add, commit, push ke pws dan github

---

# Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS

## 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Dalam CSS, ketika ada beberapa selector yang menargetkan elemen HTML yang sama, maka browser akan menentukan prioritas (specificity). Urutannya seperti ini:

1. **Inline style** → ditulis langsung di elemen HTML dengan atribut `style="..."`.
2. **ID selector** → `#id`.
3. **Class, attribute, dan pseudo-class selector** → `.class`, `[type="text"]`, `:hover`.
4. **Element (tag) dan pseudo-element selector** → `div`, `p`, `h1`, `::before`.
5. **Universal selector** → `*` dan inheritance (gaya yang diwariskan dari parent).

Aturan tambahan:
- `!important` akan mengalahkan semua aturan di atas (sebaiknya jarang dipakai karena menyulitkan maintenance).
- Jika spesifisitas sama, maka aturan yang ditulis **terakhir** (paling bawah) dalam file CSS yang dipakai.


## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

**Responsive design** penting karena pengguna mengakses aplikasi web dari berbagai perangkat dengan ukuran layar berbeda (desktop, laptop, tablet, hingga smartphone).  

Tanpa responsive design:
- Tampilan web bisa berantakan.
- Teks sulit dibaca.
- Tombol terlalu kecil ketika diakses melalui perangkat mobile.  

Hal ini tentu mengurangi user experience dan bisa membuat pengguna enggan memakai aplikasi tersebut.  

Dengan responsive design:
- Tampilan aplikasi web menyesuaikan otomatis dengan ukuran layar perangkat.
- Teknik umum: **media queries** di CSS untuk styling berbeda berdasarkan lebar layar.
- Layout modern seperti **flexbox** dan **CSS grid** memudahkan pengaturan komponen agar tetap rapi di berbagai resolusi.

**Contoh aplikasi yang sudah menerapkan responsive design:**
- Shopee atau Tokopedia: tampilan menyesuaikan di desktop dan mobile, produk tetap mudah dicari, tombol tetap nyaman diklik.

**Contoh aplikasi yang belum menerapkan responsive design:**
- Beberapa website lama instansi pemerintah: biasanya fixed-width, di HP harus diperbesar atau digeser horizontal, tampilan kurang profesional, pengguna jadi kesulitan.

Responsive design bukan hanya soal estetika, tetapi juga meningkatkan **aksesibilitas** dan **kenyamanan penggunaan** di berbagai perangkat.


## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Dalam **CSS Box Model**, margin, border, dan padding menentukan bagaimana sebuah elemen HTML ditampilkan.  

### 1. Margin
- Ruang di luar elemen.
- Memberi jarak antara elemen dengan elemen lain.
- Transparan.
- Contoh:
  ```css
  .box {
    margin: 20px; /* memberi jarak 20px dari elemen lain */
  }


### 2. Border
- Garis tepian yang membungkus konten dan padding-nya.
- Bisa diatur ketebalan, jenis garis (solid, dashed, dotted), serta warna.
- Contoh implementasi:
    ```css
    .box {
    border: 2px solid black; /* border hitam, tebal 2px */
    }


### 3. Padding
- Mengosongkan area di sekitar konten (transparan)
- Biasanya digunakan agar isi elemen tidak terlalu mepet dengan border.
- Contoh implementasi:
    ```css
    .box {
    padding: 15px; /* memberi jarak 15px antara isi dan border */
    }


Urutan dari luar ke dalam:
Margin → Border → Padding → Content

Contoh lengkap implementasi:
    ```css
    .box {
        margin: 30px;             /* jarak antar elemen */
        border: 3px dashed blue;  /* border biru putus-putus */
        padding: 20px;            /* jarak isi dengan border */
    }

Dengan begitu, margin mengatur jarak antar elemen, border membungkus elemen, dan padding memberi ruang antara isi dengan batas elemen.

## 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

#### Flexbox (Flexible Box Layout)
- Digunakan untuk mengatur elemen secara **satu dimensi** (horizontal atau vertikal).
- Elemen di dalam container fleksibel dan bisa menyesuaikan ukuran layar.
- Cocok untuk membuat navbar, sidebar, atau alignment item dalam satu baris/kolom.
- Contoh implementasi:
  ```css
  .container {
    display: flex;
    justify-content: center;  /* mengatur posisi horizontal */
    align-items: center;      /* mengatur posisi vertikal */
  }


### Grid Layout
- Grid digunakan untuk mengatur elemen secara dua dimensi (baris dan kolom sekaligus).
- Memberikan kontrol penuh terhadap tata letak halaman yang kompleks.
- Cocok untuk membuat layout halaman utama, seperti galeri gambar atau dashboard.
- Contoh:
    ```css
    .container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr; /* 3 kolom sama besar */
    gap: 10px; /* jarak antar item */
    }

Singkatnya:
Flexbox: fokus satu dimensi (row atau column).
Grid: fokus dua dimensi (row dan column).

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. Membuat fungsi edit dan delete product di views.py dan membuat path nya di urls.py
2. Membuat direktori static dan membuat berkas global.css untuk styling nantinya
3. Membuat file html untuk edit product dan melakukan kostumisasi, serta menambahkan button delete ke main.html
4. Melakukan kustomisasi pada halaman login dan register.
5. Membuat navbar yang responsive untuk desktop dan mobile.
6. Membuat card_product.html untuk merapikan tampilan produk di main nanti.
7. Melakukan kostumisasi pada main.html untuk menampilkan product menggunakan card yang telah dibuat.
8. Melakukan kostumisasi pada halaman details, edit, dan create product. 

---

Sekian, Terimakasih

Yafi Alifuddin