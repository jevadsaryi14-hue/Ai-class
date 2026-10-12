
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


sentence = "I love python and AI"

translated_words = []
translated_count = 0
untranslated_count = 0

for word in sentence.split():
  
    clean_word = word.lower()
    
    if clean_word in words:
        translated_words.append(words[clean_word])
        translated_count += 1
    else:

        translated_words.append(f"[{word}]")
        untranslated_count += 1


print("خروجی ترجمه:")
print(" ".join(translated_words))
print()


print("--- بخش اضافه ---")
print(f"تعداد کلمات ترجمه‌شده: {translated_count}")
print(f"تعداد کلمات ترجمه‌نشده: {untranslated_count}")
