class Shaxs:
    number = 0

    def __init__(self, ism, familiya, ish_joyi, JSHSHIR, passport="AD0463725"):
        self.ism = ism
        self.familiya = familiya
        self.ish_joyi = ish_joyi
        self.passport = passport
        self.JSHSHIR = JSHSHIR
        Shaxs.number += 1
        self.__id = Shaxs.number

    def get_id(self):
        return self.__id        

    def malumot(self):
        return f"Ma'lumot: {self.ism} {self.familiya} {self.ish_joyi}"

    def ish_joyi_yangi(self, qiymat):
        self.ish_joyi = qiymat


# Ob’ektlar yaratish
a1 = Shaxs("Muxlisa", "Rajabboyeva", "Ishsiz", 78889996543215)
a2 = Shaxs("Fotima", "Nurmetova", "Ishsiz", 12345678908765)
a3 = Shaxs("Nafosat", "Rustambekova", "Ishsiz", 34567890234579)

# Ma'lumotlarni tekshirish
print(a2.ism)                # Fotima
a2.ish_joyi_yangi("Universitet")
print(a2.ish_joyi)           # Universitet
print(a2.malumot())          # Ma'lumot: Fotima Nurmetova Universitet
print(a2.get_id())            # Ob’ekt ID: 2
