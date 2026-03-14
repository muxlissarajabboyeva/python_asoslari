class Mahsulot:
    soni = 0  # class attribute, barcha mahsulotlar sonini hisoblash uchun

    def __init__(self, nomi, soni, narxi, mamlakat):
        self.nomi = nomi
        self.soni = soni
        self.__narxi = narxi  # private atribut
        self.mamlakat = mamlakat
        Mahsulot.soni += 1
        self.__id = Mahsulot.soni  # unik ID

    # Mahsulot haqida ma'lumot
    def get_info(self):
        return f"{self.nomi}, soni: {self.soni}, narxi: {self.__narxi}, mamlakat: {self.mamlakat}"

    # ID olish
    def get_id(self):
        return self.__id

    # Narxni yangilash
    def update_narx(self, n):
        if n >= 0:
            self.__narxi += n

    def __repr__(self):
        return self.nomi


class Dokon:
    def __init__(self, nomi, manzili, turi):
        self.nomi = nomi
        self.manzili = manzili
        self.turi = turi
        self.mahsulotlar = []

    # Dokon haqida ma'lumot
    def get_info(self):
        return f"{self.nomi}, manzil: {self.manzili}, turi: {self.turi}"

    # Mahsulot qo'shish
    def add_mahsulot(self, mahsulot):
        self.mahsulotlar.append(mahsulot)

    # Mahsulotlar ro'yxatini olish
    def get_mahsulotlar(self):
        return self.mahsulotlar

    # Mahsulotni o'chirish
    def remove_mahsulot(self, mahsulot):
        if mahsulot in self.mahsulotlar:
            self.mahsulotlar.remove(mahsulot)

    def __repr__(self):
        return self.nomi


# -------------------------
# Ob’ektlar yaratish
# -------------------------
m1 = Mahsulot("Cola", 200, 12000, "AQSh")
m2 = Mahsulot("Palto", 500, 900000, "Italiya")

d1 = Dokon("Sevinch", "Urganch", "Kiyim")
d2 = Dokon("IDEAL SARI", "Urganch", "Kompyuter dokon")

# Mahsulotlarni dokonga qo'shish
d1.add_mahsulot(m1)
d1.add_mahsulot(m2)

# Natijalarni tekshirish
print(d1.get_info())
print("Dokon mahsulotlari:", d1.get_mahsulotlar())

# ID va narxni yangilash
print("Mahsulot ID:", m1.get_id())
m1.update_narx(1000)
print("Yangilangan narx:", m1.get_info())
