# q4_report_card.py
# تمرین ۴: کارنامه کلاس

# دیکشنری نمرات دانشجویان
scores = {
    "Ali": 18,
    "Sara": 20,
    "Reza": 9,
    "Mina": 14,
    "Omid": 11.5
}

passed_students = []

# الف) تعیین وضعیت هر دانشجو بر اساس نمره
for name, score in scores.items():
    if score >= 17:
        status = "عالی"
    elif score >= 14:
        status = "خوب"
    elif score >= 10:
        status = "قبول"
    else:
        status = "مردود"
    
    print(f"{name}: {score} → {status}")
    
    # ب) جمع‌آوری دانشجویان با نمره ۱۰ و بالاتر
    if score >= 10:
        passed_students.append(name)

# ب) چاپ لیست افراد قبولی
print(f"قبول‌شده‌ها: {passed_students}")

# ج) محاسبه و چاپ میانگین کلاس
average = sum(scores.values()) / len(scores)
print(f"میانگین کلاس: {average}")

# د) پیدا کردن و چاپ نام نفر اول کلاس
top_student = max(scores, key=scores.get)
print(f"نفر اول: {top_student}")
