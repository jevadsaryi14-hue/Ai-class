# q3_cinema.py
# تمرین ۳: گیشه سینما

age = int(input("سن : "))
day = input("روز : ").strip()


if age < 5:
    print("ورود رایگان!")
else:
    if 5 <= age <= 12:
        price = 50000
    elif age >= 60:
        price = 60000
    else:
        price = 100000

   
    if "سه" in day and "شنبه" in day:
        price = int(price * 0.8)

    print(f"قیمت بلیط : {price} تومان")
