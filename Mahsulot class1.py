class Mahsulot:
    soni = 0  # class attribute, umumiy soni hisoblash uchun

    def __init__(self, nomi, soni, narxi, mamlakat):
        self.nomi = nomi
        self.soni = soni
        self.__narxi = narxi      # private atribut
        self.mamlakat = mamlakat
        Mahsulot.soni += 1
        self.__id = Mahsulot.soni  # unik ID

    # Malumot olish (getter)
    def get_info(self):
        return f"{self.nomi}, soni: {self.soni}, narxi: {self.__narxi}, mamlakat: {self.mamlakat}"

    # ID olish
    def get_id(self):
        return self.__id        

    # Narxni o‘zgartirish (setter)
    def set_narx(self, x):
        if x >= 0:
            self.__narxi += x

    def __repr__(self):
        return self.nomi


# -------------------------
# Ob’ektlar yaratish
# -------------------------
m1 = Mahsulot("Cola", 200, 12000, "AQSh")
m2 = Mahsulot("Palto", 500, 900000, "Italiya")

# Tekshirish
print(m1.get_info())
print("ID:", m1.get_id())

m1.set_narx(1000)
print("Yangilangan narx:", m1.get_info())

print(m2.get_info())
print("ID:", m2.get_id())
