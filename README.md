# 🍳 Resep Hemat - Aplikasi Web Resep Makanan untuk Anak Kos

[![Django](https://img.shields.io/badge/Django-6.0-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Project UAS Dasar-Dasar Pemrograman - Kelompok 12**  
> Aplikasi web berbasis Django untuk membantu mahasiswa dan anak kos menemukan resep makanan hemat, mudah, dan lezat.

---

## 📋 Daftar Isi

- [Tentang Project](#-tentang-project)
- [Fitur Utama](#-fitur-utama)
- [Teknologi yang Digunakan](#-teknologi-yang-digunakan)
- [Struktur Project](#-struktur-project)
- [Instalasi & Setup](#-instalasi--setup)
- [Cara Menjalankan](#-cara-menjalankan)
- [Screenshot](#-screenshot)
- [Kontribusi](#-kontribusi)
- [Lisensi](#-lisensi)
- [Developer](#-developer)

---

## 🎯 Tentang Project

**Resep Hemat** adalah aplikasi web yang dirancang khusus untuk membantu mahasiswa dan anak kos dalam memasak makanan yang:
- 💰 **Hemat**: Semua resep di bawah Rp 20.000
- ⚡ **Cepat**: Maksimal 30 menit memasak
- 🍽️ **Enak**: Tetap lezat meski hemat

Project ini dibuat sebagai bagian dari tugas **Ujian Akhir Semester (UAS) Dasar-Dasar Pemrograman** dengan fokus pada:
- Implementasi **Django Framework**
- Penerapan **Responsive Web Design (RWD)** menggunakan Bootstrap
- Pengolahan data dinamis dengan **Python**
- Manajemen database dengan **SQLite**

---

## ✨ Fitur Utama

### 🏠 Halaman Utama (Home)
- Hero section dengan background gambar menarik
- Tampilan resep populer
- Quick access ke fitur-fitur utama
- Responsive design untuk mobile dan desktop

### 📖 Daftar Resep
- Grid view dengan card design modern
- Filter berdasarkan:
  - Budget (Rp 5.000 - Rp 20.000)
  - Waktu memasak (8 - 30 menit)
- Search functionality
- Informasi lengkap setiap resep

### 🔍 Detail Resep
- Foto makanan berkualitas tinggi
- Estimasi budget yang akurat
- Daftar bahan-bahan
- Langkah-langkah memasak yang jelas
- Tips & tricks memasak

### 💵 Kalkulator Budget
- Hitung budget belanja mingguan
- Rekomendasi resep berdasarkan budget
- Kategori: Super Hemat, Hemat, Standar, Premium

### ✍️ Submit Resep
- Form untuk user mengirim resep mereka
- Validasi input lengkap
- Notifikasi sukses/error

### ℹ️ Halaman About
- Informasi tentang aplikasi
- Tujuan dan manfaat
- Kontak developer

---

## 🛠️ Teknologi yang Digunakan

### Backend
- **Python 3.12** - Bahasa pemrograman utama
- **Django 6.0** - Web framework
- **SQLite** - Database

### Frontend
- **HTML5** - Struktur halaman
- **CSS3** - Styling
- **Bootstrap 5.3** - Responsive framework
- **Bootstrap Icons** - Icon library
- **JavaScript** - Interaktivitas

### Tools & Libraries
- **Django Template Engine** - Template rendering
- **Django Messages Framework** - Notifikasi
- **Django Session** - Data persistence

---

## 📁 Struktur Project

```
my_django_app/
├── aplikasi/                    # Main Django app
│   ├── migrations/              # Database migrations
│   ├── templates/               # HTML templates
│   │   ├── about.html
│   │   ├── base.html
│   │   ├── budget_calculator.html
│   │   ├── home.html
│   │   ├── index.html
│   │   ├── recipe_detail.html
│   │   ├── recipes.html
│   │   └── submit_recipe.html
│   ├── static/                  # Static files (CSS, JS, Images)
│   ├── __init__.py
│   ├── admin.py                 # Django admin configuration
│   ├── apps.py
│   ├── models.py                # Data models
│   ├── tests.py                 # Unit tests
│   └── views.py                 # View functions (logic)
│
├── my_django_app/               # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              # Project settings
│   ├── urls.py                  # URL routing
│   └── wsgi.py
│
├── db.sqlite3                   # SQLite database
├── manage.py                    # Django management script
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
```

---

## 🚀 Instalasi & Setup

### Prerequisites
Pastikan Anda sudah menginstall:
- Python 3.12 atau lebih tinggi
- pip (Python package manager)
- Git

### Langkah Instalasi

1. **Clone Repository**
   ```bash
   git clone https://github.com/username/resep-hemat.git
   cd resep-hemat
   ```

2. **Buat Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Database**
   ```bash
   python manage.py migrate
   ```

5. **Buat Superuser (Opsional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect Static Files (Production)**
   ```bash
   python manage.py collectstatic
   ```

---

## 💻 Cara Menjalankan

### Development Server

```bash
# Jalankan server
python manage.py runserver

# Buka browser dan akses:
# http://127.0.0.1:8000/
```

### Akses Admin Panel (Jika sudah buat superuser)
```
http://127.0.0.1:8000/admin/
```

### Available URLs
| URL | Deskripsi |
|-----|-----------|
| `/` | Homepage |
| `/recipes/` | Daftar semua resep |
| `/recipe/<id>/` | Detail resep |
| `/about/` | Tentang aplikasi |
| `/budget-calculator/` | Kalkulator budget |
| `/submit-recipe/` | Form submit resep |
| `/admin/` | Admin panel |

---

## 📸 Screenshot

### 🏠 Homepage
![Homepage](docs/screenshots/homepage.png)
*Tampilan homepage dengan hero section dan featured recipes*

### 📖 Daftar Resep
![Recipes List](docs/screenshots/recipes.png)
*Grid view dengan filter dan search*

### 🔍 Detail Resep
![Recipe Detail](docs/screenshots/detail.png)
*Detail lengkap dengan bahan dan langkah memasak*

### 💵 Budget Calculator
![Calculator](docs/screenshots/calculator.png)
*Kalkulator budget dengan rekomendasi resep*

---

## 🎓 Fitur Pembelajaran (Educational Aspects)

Project ini mendemonstrasikan pemahaman tentang:

✅ **Django Framework**
- URL routing dan views
- Template engine
- Forms processing
- Session management
- Messages framework

✅ **Responsive Web Design**
- Bootstrap grid system
- Mobile-first approach
- Flexbox & CSS Grid
- Media queries

✅ **Python Programming**
- Functions dan classes
- Data structures (lists, dictionaries)
- Conditional statements
- Loops dan iterations
- Error handling

✅ **Web Development Concepts**
- Client-server architecture
- HTTP methods (GET, POST)
- Static vs dynamic content
- User input validation
- Database operations

---

## 🤝 Kontribusi

Kontribusi sangat diterima! Jika Anda ingin berkontribusi:

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

---

## 📝 To-Do List (Future Improvements)

- [ ] Implementasi database MySQL/PostgreSQL
- [ ] User authentication & registration
- [ ] Rating & review system
- [ ] Bookmark favorite recipes
- [ ] Shopping list generator
- [ ] Nutrition calculator
- [ ] Recipe video tutorials
- [ ] Multi-language support

---

## 📄 Lisensi

Project ini dilisensikan di bawah [MIT License](LICENSE).

```
MIT License

Copyright (c) 2025 Mumtaaz Shidqon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 👨‍💻 Developer

**Kelompok 12**
- Mumtaaz Abdurrahman - 0110225164
- Muhammad Ilyas Adityarahamn - 0110225172
- Wahyu Irawan Saputra - 0110225168
- Azzidan al'fatio syachputra - 0110225173
- Indah Nurul Ayni Hasibuan - 0110225121

---



<div align="center">

### ⭐ Star this repository if you find it helpful!

**Made with ❤️ for UAS DDP Semester 1**

© 2025 Mumtaaz Shidqon. All Rights Reserved.

</div>
