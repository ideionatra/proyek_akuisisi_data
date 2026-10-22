# Proyek Akuisisi dan Manajemen Data
Mata kuliah : BIFP-243 Akuisisi dan Manajemen Data  
Nama / NIM : I Made Dio Kartiana Putra / 2501010142  
Tujuan : ....................  


## Struktur Folder
- data/raw : data mentah hasil akuisisi (READ-ONLY)
- data/interim : hasil antara (cleaning, transformasi)
- data/processed : dataset final siap analisis
- notebooks : notebook praktikum
- src : script Python yang dapat digunakan ulang
- docs : data dictionary dan metadata
- reports : laporan kualitas data


## Cara Menjalankan Ulang
1. pip install -r requirements.txt
2. Jalankan notebook di folder notebooks secara berurutan

```python
(ROOT / "README.md").write_text(readme, encoding="utf-8")
print((ROOT / "README.md").read_text(encoding="utf-8")[:300])
```

## Tugas Modul 2
1. Kode dan hasil dataframe dapat dilihat pada file lifecycle.ipynb dan hasil .csv dapat dilihat pada docs/lifecycles.csv
2. Struktur Folder dan README.md sudah di persiapkan dengan baik, sekaligus memperlihatkan semua folder yang tidak terlihat sebelumnya kerana tidak memiliki file sebelumnya. (Cek commit 2abb1ce "docs: changing dummy.md into .gitkeep for better use of git features")
3. Jawaban tertulis pada file latihan_modul_2.


## Tugas Modul 3
1. File jawaban terletak pada folder assigments/pertemuan3/analisis_kebutuhan_storage.md