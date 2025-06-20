from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from textwrap import wrap

# File path
file_path = "/mnt/data/laporan_palindrom.pdf"

# Create canvas
c = canvas.Canvas(file_path, pagesize=A4)
width, height = A4

# Helper for writing wrapped text
def draw_wrapped_text(text, x, y, max_width, line_height=14, font_name="Helvetica", font_size=12):
    c.setFont(font_name, font_size)
    for line in wrap(text, width=int(max_width / (font_size * 0.6))):
        c.drawString(x, y, line)
        y -= line_height
    return y

# Title
c.setFont("Helvetica-Bold", 16)
c.drawString(72, height - 72, "Laporan Program Pengenal String Palindrom")
c.setFont("Helvetica", 12)
c.drawString(72, height - 90, "Dibuat dengan Bahasa Pemrograman Python")

current_y = height - 120

sections = [
    ("1. Deskripsi Masalah", 
     "Buatlah program komputer yang dapat mengenali string–string palindrom. "
     "Himpunan input string dibentuk dari pola (letter + digit)*, yaitu kombinasi huruf (a‑z, A‑Z) "
     "dan angka (0‑9). Program harus menentukan apakah string yang dimasukkan merupakan palindrom "
     "dengan mengabaikan perbedaan huruf kapital dan huruf kecil."),
    ("2. Algoritma", 
     "• Normalisasi: ubah seluruh karakter huruf menjadi huruf kecil.\n"
     "• Pemeriksaan: bandingkan string dengan versi terbalik (s[::-1]). Jika sama ► palindrom.\n"
     "• Kompleksitas Waktu: O(n) dengan n = panjang string.\n"
     "• Kompleksitas Memori: O(1) (hanya membutuhkan variabel penampung string terbalik)."),
    ("3. Implementasi Kode", 
     "```python\n"
     "import re\n\n"
     "def is_palindrome(text: str) -> bool:\n"
     "    \"\"\"Mengembalikan True jika `text` adalah palindrom (alfanumerik).\"\"\"\n"
     "    # Filter hanya huruf & digit, lalu ubah menjadi huruf kecil\n"
     "    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())\n"
     "    return cleaned == cleaned[::-1]\n\n"
     "def main():\n"
     "    print('=== Pengecekan Palindrom ===')\n"
     "    print('Masukkan string alfanumerik (enter kosong untuk keluar)')\n"
     "    while True:\n"
     "        s = input('Input > ').strip()\n"
     "        if not s:\n"
     "            break\n"
     "        if is_palindrome(s):\n"
     "            print('✔ \"{}\" adalah palindrom.'.format(s))\n"
     "        else:\n"
     "            print('✘ \"{}\" BUKAN palindrom.'.format(s))\n\n"
     "if __name__ == '__main__':\n"
     "    main()\n"
     "```"),
    ("4. Contoh Input & Output",
     "```\n"
     "=== Pengecekan Palindrom ===\n"
     "Masukkan string alfanumerik (enter kosong untuk keluar)\n"
     "Input > a1B2b1A\n"
     "✘ \"a1B2b1A\" BUKAN palindrom.\n"
     "Input > 12321\n"
     "✔ \"12321\" adalah palindrom.\n"
     "Input > Madam\n"
     "✔ \"Madam\" adalah palindrom.\n"
     "Input > \n"
     "```\n"),
    ("5. Cara Menjalankan Program", 
     "1. Pastikan Python (≥ 3.7) terinstal.\n"
     "2. Simpan kode di atas sebagai `palindrom.py`.\n"
     "3. Jalankan perintah: `python palindrom.py`.\n"
     "4. Masukkan string sesuai instruksi."),
    ("6. Lisensi & Kredensial", 
     "Kode ini dirilis dengan lisensi MIT dan dapat langsung disalin ke repositori GitHub Anda.")
]

margin_x = 72
max_text_width = width - 2*margin_x

for title, body in sections:
    c.setFont("Helvetica-Bold", 13)
    c.drawString(margin_x, current_y, title)
    current_y -= 18
    current_y = draw_wrapped_text(body, margin_x, current_y, max_text_width)
    current_y -= 12
    if current_y < 100:
        c.showPage()
        current_y = height - 72

# Finalize
c.save()

file_path
