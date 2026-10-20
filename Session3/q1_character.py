# تمرین ۱: گسترش کلاس Character

class Character:
    def __init__(self, name, power, health, coins):
        self.name = name
        self.power = power
        self.health = health
        self.coins = coins
        self.level = 1  # ویژگی جدید لول با مقدار اولیه ۱

    def show_info(self):
        """چاپ تمام اطلاعات کاراکتر در یک خط"""
        print(f"{self.name} | Level: {self.level} | Power: {self.power} | Health: {self.health} | Coins: {self.coins}")

    def is_alive(self):
        """بررسی زنده بودن کاراکتر بر اساس سلامت"""
        return self.health > 0

    def attack(self, other):
        """حمله به کاراکتر دیگر و کم کردن از سلامت او"""
        other.health -= self.power
        print(f"{self.name} attacked {other.name}. {other.name}'s health: {other.health}")

    def earn_coins(self, amount):
        """اضافه کردن سکه به کاراکتر"""
        self.coins += amount
        print(f"{self.name} earned {amount} coins. Total coins: {self.coins}")

    def buy_potion(self):
        """خرید معجون در صورت داشتن حداقل ۲۰ سکه"""
        if self.coins >= 20:
            self.coins -= 20
            self.health += 30
            print(f"{self.name} bought a potion! (+30 Health, -20 Coins)")
        else:
            print("Not enough coins")

    def level_up(self):
        """ارتقای لول و افزایش قدرت کاراکتر"""
        self.level += 1
        self.power += 5
        print(f"{self.name} reached level {self.level}. New power: {self.power}")


# --- بخش تست و اجرای خواسته شده در صورت سوال ---
if __name__ == "__main__":
    print("=== تست تمرین ۱ (Character) ===")
    
    # ساخت دو کاراکتر
    c1 = Character("Arya", power=15, health=100, coins=50)
    c2 = Character("Bran", power=10, health=90, coins=15)

    print("\n--- اطلاعات اولیه ---")
    c1.show_info()
    c2.show_info()

    print("\n--- مبارزه و حمله ---")
    c1.attack(c2)
    c2.attack(c1)
    c1.attack(c2)

    print("\n--- خرید معجون و ارتقای لول ---")
    # کاراکتر اول معجون می‌خرد
    c1.buy_potion()
    # کاراکتر دوم سعی می‌کند معجون بخرد (چون ۱۵ سکه دارد خطا می‌دهد)
    c2.buy_potion()
    # کاراکتر دوم لول‌آپ می‌کند
    c2.level_up()

    print("\n--- اطلاعات نهایی هر دو کاراکتر ---")
    c1.show_info()
    c2.show_info()
