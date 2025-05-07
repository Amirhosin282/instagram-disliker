# Disliker Tool - ابزار دیس لایکر

## 📌 English Version

### 🚀 Overview
Disliker is a Python automation tool I created using Selenium to clean up my Instagram liked content. I noticed I had randomly liked too many posts (probably while mindlessly scrolling), so I developed this script to automatically unlike them all.

### ⚙️ How It Works
1. Logs into your Instagram account using Selenium automation
2. Navigates to your "Liked Posts" section
3. Automatically unlikes all posts one by one

### 🖥️ How to Run
1. Clone the repository
2. Install required packages:
   ```
    pip install selenium colorama pyfiglet khayyam rainbowtext platform time  
   ```
3. Download Chrome WebDriver and add it to your PATH
4. For Linux users: A virtual environment (.Venv) is provided - activate it using:
   ```
   source .venv/bin/activate
   ```
5. Run the script:
   ```
   python main.py
   ```
6. Enter your Instagram credentials when prompted

### ⚠️ Important Notes
- Built with Python Selenium for browser automation
- This tool may stop working if Instagram changes its algorithms or UI structure
- Use at your own risk
- Make sure you have Chrome WebDriver installed
- The tool includes a cool loading animation before starting

### ❓ Why I Built This
Honestly, I looked at my liked posts and realized most were random junk. Instead of manually unliking hundreds of posts, I automated the process using Selenium!

---

## 📌 نسخه فارسی

### 🚀 معرفی
دیس لایکر یک ابزار پایتونی هست که من با استفاده از سلنیوم برای پاک کردن لایک‌های اینستاگرامم ساختم. متوجه شدم کلی پست چرت و پرت رو لایک کرده بودم (احتمالا وقتی بی‌هدف اسکرول می‌کردم)، بنابراین این اسکریپت رو نوشتم تا به صورت خودکار همه‌شون رو آنلایک کنه.

### ⚙️ نحوه کار
1. با استفاده از سلنیوم وارد حساب اینستاگرام شما می‌شود
2. به بخش "پست‌های لایک شده" می‌رود
3. به صورت خودکار همه پست‌ها را یکی یکی آنلایک می‌کند

### 🖥️ نحوه اجرا
1. ریپازیتوری رو کلون کنید
2. کتابخانه‌های مورد نیاز رو نصب کنید:
   ```
   pip install selenium colorama pyfiglet khayyam rainbowtext platform time 
   ```
3. Chrome WebDriver رو دانلود کرده و به PATH اضافه کنید
4. برای کاربران لینوکس: یک محیط مجازی (.Venv) آماده شده - با دستور زیر فعالش کنید:
   ```
   source .venv/bin/activate
   ```
5. اسکریپت رو اجرا کنید:
   ```
   python main.py
   ```
6. وقتی خواست، اطلاعات ورود اینستاگرام رو وارد کنید

### ⚠️ نکات مهم
- ساخته شده با سلنیوم پایتون برای اتوماسیون مرورگر
- این ابزار ممکنه با تغییر الگوریتم‌ها یا ظاهر اینستاگرام از کار بیوفته
- استفاده از آن به عهده خود شماست
- مطمئن شوید Chrome WebDriver نصب شده
- ابزار شامل یک انیمیشن بارگذاری جالب قبل از شروع کار هست

### ❓ چرا این ابزار رو ساختم؟
راستش رو بخواید، یه روز دقت کردم دیدم کلی پست بی‌معنی رو لایک کردم. به جای اینکه صدها پست رو دستی آنلایک کنم، با استفاده از سلنیوم این فرآیند رو خودکار کردم!

---

**توجه**: این ابزار ممکنه نیاز به آپدیت داشته باشه اگر اینستاگرام تغییراتی ایجاد کنه.  
**Note**: This tool may need updates if Instagram makes changes to its platform.
