class Talaba:
    number = 0

    def __init__(self, ism, familiya, guruh, shartnoma="Kontrakt"):
        self.ism = ism
        self.familiya = familiya
        self.guruh = guruh
        self.shartnoma = shartnoma
        Talaba.number += 1
        self.__id = Talaba.number

    # ID olish
    def get_id(self):
        return self.__id

    # Malumot
    def malumot(self):
        return f"Ma'lumot: {self.ism} {self.familiya} {self.guruh}"

    # Guruhni yangilash
    def guruh_yangi(self, qiymat):
        self.guruh = qiymat


# Ob’ektlar yaratish
a1 = Talaba("Muxlisa", "Rajabboyeva", "941-22")
a2 = Talaba("Fotima", "Nurmetova", "941-22")
a3 = Talaba("Nafosat", "Rustambekova", "941-22")

# Tekshirish
print(a1.ism)          # Muxlisa
a1.guruh_yangi("942-22")
print(a1.guruh)         # 942-22
print(a1.malumot())     # Ma'lumot: Muxlisa Rajabboyeva 942-22
print(a1.get_id())      # 1
