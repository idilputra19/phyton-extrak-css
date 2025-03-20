# 🔥 Pemisahan HTML dan CSS dengan Python

Skrip Python ini dirancang untuk secara otomatis mengekstrak kode CSS dari file HTML yang mengandung elemen `<style>` dan menyimpannya dalam file terpisah. Dengan pendekatan ini, Anda dapat meningkatkan keterbacaan dan pengelolaan kode proyek web Anda.

---

## 🚀 Fitur Utama

✅ Memisahkan kode CSS dari file HTML dengan cepat dan efisien.  
✅ Menyimpan HTML yang telah dibersihkan dalam file terpisah.  
✅ Tidak memodifikasi struktur HTML selain menghapus tag `<style>`.  
✅ Mendukung berbagai format HTML.

---

## 📌 Cara Penggunaan

1. Simpan skrip Python dalam file, misalnya `split_html_css.py`.
2. Pastikan Anda memiliki file HTML yang ingin diproses, misalnya `input.html`.
3. Jalankan skrip dengan perintah berikut:
   ```bash
   python split_html_css.py
   ```
4. Setelah proses selesai, Anda akan mendapatkan dua file output:
   - `output.html` (file HTML tanpa kode CSS)
   - `styles.css` (file yang berisi CSS yang diekstrak dari HTML)

---

## 📋 Persyaratan

- Python 3.x harus terinstal di sistem Anda.
- File `input.html` harus berisi kode HTML dengan elemen `<style>` yang ingin diekstrak.

---

## ✨ Contoh Input & Output

### 🔹 Input: `input.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Contoh</title>
    <style>
        body { background-color: lightgray; }
        h1 { color: blue; }
    </style>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
```

### 🔹 Output:
**`output.html`**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Contoh</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
```

**`styles.css`**
```css
body { background-color: lightgray; }
h1 { color: blue; }
```

---

## 📜 Lisensi

Skrip ini dapat digunakan, dimodifikasi, dan didistribusikan tanpa batasan lisensi. Silakan gunakan sesuai kebutuhan Anda! 🎯

---

💡 **Ingin fitur tambahan atau modifikasi lebih lanjut? Jangan ragu untuk menyesuaikan skrip sesuai kebutuhan proyek Anda!**

---

❤️ *Made with love for developers everywhere!*

---

📄 **README.md**

