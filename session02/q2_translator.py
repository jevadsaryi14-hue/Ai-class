# q2_translator.py
# تمرین ۲: مترجم کوچولو

# ۱. دیکشنری لغات (حداقل ۸ کلمه انگلیسی به فارسی)
words = {
    "i": "من",
    "love": "دوست دارم",
    "python": "پایتون",
    "code": "کد",
    "computer": "کامپیوتر",
    "learn": "یادگیری",
    "book": "کتاب",
    "programming": "برنامه‌نویسی"
}

# جمله مورد نظر برای ترجمه
sentence = "I love python and AI"

translated_words = []
translated_count = 0
untranslated_count = 0

# شکستن جمله به کلمات مجزا
for word in sentence.split():
    # کوچک کردن حروف برای مقایسه با کلیدهای دیکشنری
    clean_word = word.lower()
    
    if clean_word in words:
        translated_words.append(words[clean_word])
        translated_count += 1
    else:
        # اگر کلمه در دیکشنری نبود، داخل کروشه قرار می‌گیرد
        translated_words.append(f"[{word}]")
        untranslated_count += 1

# چاپ خروجی ترجمه شده
print("خروجی ترجمه:")
print(" ".join(translated_words))
print()

# بخش اضافه: آمار کلمات ترجمه شده و نشده
print("--- بخش اضافه ---")
print(f"تعداد کلمات ترجمه‌شده: {translated_count}")
print(f"تعداد کلمات ترجمه‌نشده: {untranslated_count}")
