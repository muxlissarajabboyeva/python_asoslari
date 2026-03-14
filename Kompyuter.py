class Kompyuter:
    def __init__(self, nomi, xotirasi, protsessori, narxi):
        self.nomi = nomi
        self.xotirasi = xotirasi
        self.protsessori = protsessori
        self.narxi = narxi

    def get_info(self):
        return f"{self.nomi}, {self.xotirasi}, {self.protsessori}, narxi: {self.narxi} so'm"

    def update_narx(self, n):  # eski: updete_narx → update_narx
        self.narxi += n

    def __repr__(self):
        return self.nomi


class KompyuterDokon:
    def __init__(self, nomi, manzili, telefon):
        self.nomi = nomi
        self.manzili = manzili
        self.telefon = telefon
        self.kompyuterlar = []

    def get_info(self):
        return f"{self.nomi}, manzil: {self.manzili}, telefon: {self.telefon}"

    def add_kompyuter(self, komp):  # __call__ o‘rniga aniq nomli metod qulayroq
        self.kompyuterlar.append(komp)

    def __getitem__(self, index):
        return self.kompyuterlar[index]

    def get_kompyuterlar(self):
        return self.kompyuterlar

    def __repr__(self):
        return self.nomi


# -------------------------
# Ob’ektlar yaratish
# -------------------------

obj1 = Kompyuter("Tecno", "512 GB", "Intel Core i5", 6000000)
obj2 = Kompyuter("Asus", "256 GB", "Intel Core i5", 5500000)

dokon1 = KompyuterDokon("IBM", "Urganch 5 blok", "+99891234444")
dokon2 = KompyuterDokon("Ideal Sari", "Urganch", "+998973331221")

# Kompyuterlarni dokonga qo'shish
dokon1.add_kompyuter(obj1)
dokon1.add_kompyuter(obj2)

# Natijalarni tekshirish
print(dokon1.get_info())
print("Dakon kompyuterlar:", dokon1.get_kompyuterlar())

# Indeks bo‘yicha olish
print("Birinchi kompyuter:", dokon1[0].get_info())
