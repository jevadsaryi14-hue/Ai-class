class Student:
    def __init__(self, esm, shomare_daneshjoo, reshte):
        self.esm_daneshjoo = esm
        self.shomare = shomare_daneshjoo
        self.reshte_tahsili = reshte

    def chape_moshakhasat(self):
        print(f"نام: {self.esm_daneshjoo} | شماره: {self.shomare} | رشته: {self.reshte_tahsili}")


daneshjoo1 = Student("جواد", "401123", "کامپیوتر")
daneshjoo2 = Student("رضا", "402987", "مکانیک")

daneshjoo1.chape_moshakhasat()
daneshjoo2.chape_moshakhasat()

