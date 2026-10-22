# Analisis Kebutuhan Storage
## Tema: Dokumentasi Lontar & Aksara Bali


### Daftar jenis data yang dibutuhkan
- Gambar dokumentasi lontar 
- Isi transkripsi lontar  
- Terjemahan lontar dalam bentuk teks 
- Gambar ilustrasi 47 Aksara Bali 
- Audio pengucapan aksara bali
- Metadata dokumen


### Karkteristik tiap jenis data
#### What
- Jenis data dan format yang saya gunakan
    - Gambar: .png, .jpg, .jpeg, .gif
    - Transkrip dan Terjemahan: .md, .pdf, .json
    - Audio: .mp3, .waw
    - Metadata: .csv, .xlsx
#### Who
Siapa yang mengumpulkan data dan menggunakan datanya

Data dikumpulkan melalui lembaga riset dan pelestarian budaya. Hingga nantinay dapat digunakan oleh kalangan pelajar.

#### Why
Data dikumpulkan untuk mendigitalisasi arsip kebudayaan Bali. Agar data kebudayaan tidak terdegradasi atau rusak oleh waktu dan tetap bisa dilihat oleh generasi selanjutnya.

#### When
Kapan data dikumpulkan dan kapan akan diperbaharui?

Data pertama dikumpulkan pada tanggal .... dan akan diperbaharui apabila ditemukannya lontar-lontar baru serta perubahan pada penulisan aksara bali.

#### Where
Dimana data disimpan?

Data disimpan pada server pribadi yang dikelompokan berdasarkan bentuk datanya. Structured, Semi-structured dan Unstructure.


### Asumsi Jumlah Unit dan Ukuran Rata-rata
- Gambar dokumentasi lontar = 500 jilid x 30 lembar = 15.000 x 3MB = 45.000MB = 45GB 
- Isi transkripsi lontar  = 500 jilid x 30 lembar = 15.000 x 20KB = 300.000KB = 300MB (0.3GB)
- Terjemahan lontar dalam bentuk teks = 500 jilid x 30 lembar = 15.000 x 18KB = 270.000KB = 270MB (0.27GB)
- Gambar ilustrasi 47 Aksara Bali = 47 x 1 file = 47 x 3MB = 141 MB = 0.141GB
- Audio pengucapan aksara bali = 47 x 1 file = 47 x 500KB = 23.500KB = 23.5MB (0.0235GB)
- Metadata dokumen =  500 File lontar + 47 aksara + 1 database = 548 file x 50kb = 27.400KB = 27.4MB (0.027GB)
= Total keseluruhan adalah 45.7615GB
### Asumsi Storage + Cadangan 30%
Estimasi storage = 45.7615 + 30% = 59.48995 GB -> 60GB
