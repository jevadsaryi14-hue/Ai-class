
playlist = ["Shape of You", "Blinding Lights", "Believer", "Perfect"]

print("--- پلی‌لیست اولیه ---")
print(playlist)
print()

print(f"الف) تعداد آهنگ‌ها: {len(playlist)}")

print(f"ب) اولین آهنگ: {playlist[0]}")
print(f"   آخرین آهنگ: {playlist[-1]}")


playlist.append("Dynamite")
print(f"ج) لیست بعد از اضافه شدن Dynamite: {playlist}")


playlist.remove("Believer")
print(f"د) لیست بعد از حذف Believer: {playlist}")


playlist.sort()
print(f"ه) لیست مرتب‌شده به ترتیب الفبا: {playlist}")
print()


print("و) خروجی مورد انتظار:")
for index, song in enumerate(playlist, start=1):
    print(f"{index}. {song}")
