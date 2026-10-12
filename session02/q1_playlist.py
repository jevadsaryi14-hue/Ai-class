# q1_playlist.py
# تمرین ۱: پلی‌لیست من

# لیست اولیه آهنگ‌ها
playlist = ["Shape of You", "Blinding Lights", "Believer", "Perfect"]

print("--- پلی‌لیست اولیه ---")
print(playlist)
print()

# الف) تعداد آهنگ‌ها
print(f"الف) تعداد آهنگ‌ها: {len(playlist)}")

# ب) اولین و آخرین آهنگ
print(f"ب) اولین آهنگ: {playlist[0]}")
print(f"   آخرین آهنگ: {playlist[-1]}")

# ج) اضافه کردن آهنگ Dynamite به انتهای لیست
playlist.append("Dynamite")
print(f"ج) لیست بعد از اضافه شدن Dynamite: {playlist}")

# د) حذف آهنگ Believer از لیست
playlist.remove("Believer")
print(f"د) لیست بعد از حذف Believer: {playlist}")

# ه) مرتب‌سازی به ترتیب الفبا و چاپ آن
playlist.sort()
print(f"ه) لیست مرتب‌شده به ترتیب الفبا: {playlist}")
print()

# و) چاپ هر آهنگ با شماره با استفاده از حلقه for و enumerate
print("و) خروجی مورد انتظار:")
for index, song in enumerate(playlist, start=1):
    print(f"{index}. {song}")
