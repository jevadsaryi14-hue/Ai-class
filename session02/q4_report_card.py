# q4_report_card.py
# تمرین ۴: کارنامه کلاس


scores = {
    "Ali": 18,
    "Sara": 20,
    "Reza": 9,
    "Mina": 14,
    "Omid": 11.5
}

passed_students = []


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
    if score >= 10:
        passed_students.append(name)


print(f"قبول‌شده‌ها: {passed_students}")


average = sum(scores.values()) / len(scores)
print(f"میانگین کلاس: {average}")


top_student = max(scores, key=scores.get)
print(f"نفر اول: {top_student}")
