# 🟡 بازی Pac-Man

<p align="center">
<strong>🇮🇷 فارسی</strong> •
<a href="./README.md">🇺🇸 English</a>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.6.1-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

</p>

---

<p align="center">
<img src="docs/screenshots/gameplay.gif" width="800">
</p>

## 🎮 گیم‌پلی

این پروژه بازسازی بازی کلاسیک **Pac-Man** با استفاده از **Python** و **Pygame** است.

هدف بازیکن جمع‌آوری تمام نقطه‌های داخل هزارتو و فرار از دست روح‌ها است. با خوردن **Power Pellet**، پک‌من برای مدت کوتاهی قدرت می‌گیرد و می‌تواند روح‌ها را از بین ببرد.

در طول بازی، با افزایش شماره مرحله، تعداد دشمنان و هوش مصنوعی آن‌ها نیز پیشرفته‌تر شده و بازی به‌تدریج چالش‌برانگیزتر می‌شود.

---

## 📖 درباره پروژه

این پروژه با هدف یادگیری و تمرین توسعه بازی‌های دوبعدی طراحی شده است و علاوه بر بازسازی مکانیک‌های اصلی Pac-Man، امکانات جدیدی نیز به آن اضافه شده است.

مباحثی که در توسعه این پروژه روی آن‌ها تمرکز شده است:

* برنامه‌نویسی شی‌گرا (OOP)
* توسعه بازی با Pygame
* هوش مصنوعی دشمن‌ها
* الگوریتم مسیر‌یابی BFS
* طراحی ساختار ماژولار پروژه
* مدیریت منابع (تصاویر، صداها و فایل‌های ذخیره)

---

## ✨ امکانات

* ۶ مرحله با افزایش تدریجی سختی
* سه نوع هوش مصنوعی برای روح‌ها

  * حرکت تصادفی (Random)
  * هوش ترکیبی (Mixed AI)
  * مسیر‌یابی هوشمند با BFS
* آیتم‌های Power Pellet
* تم رنگی متفاوت برای هر مرحله
* اسپرایت‌های اختصاصی Pixel Art
* حرکت نرم روی گرید
* منوی Pause
* ذخیره خودکار رکورد (High Score)
* افکت‌های صوتی و موسیقی
* صفحه برد و باخت
* فایل اجرایی مستقل (Standalone EXE)

---

## 📸 تصاویر

### منوی اصلی

![](docs/screenshots/menupage.png)

---

### حالت Power

![](docs/screenshots/power_mode.png)

---

### صفحه پیروزی

![](docs/screenshots/winner.png)

---

## 🎮 کنترل‌ها

| کلید    | عملکرد            |
| ------- | ----------------- |
| ← ↑ ↓ → | حرکت              |
| ESC     | توقف بازی (Pause) |
| SPACE   | شروع بازی         |
| R       | شروع دوباره       |

---

## 📁 ساختار پروژه

```text
assets/
core/
game/
screens/
docs/
main.py
README.md
README_FA.md
```

---

## 🚀 اجرای پروژه

```bash
git clone https://github.com/mahdifarahanicode/PacMan-Game.git

cd PacMan-Game

pip install pygame

python main.py
```

یا می‌توانید نسخه آماده اجرا را از بخش **Releases** دریافت کنید و بدون نیاز به نصب Python بازی را اجرا کنید.

---

## 👨‍💻 توسعه‌دهنده

**مهدی فراهانی (Mahdi Farahani)**

این پروژه به عنوان یک پروژه شخصی و آموزشی با استفاده از **Python** و **Pygame** توسعه داده شده است.
