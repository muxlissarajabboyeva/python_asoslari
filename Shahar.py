class Shahar:
    soni = 0  # class attribute, barcha shaharlar sonini hisoblash uchun

    def __init__(self, tuman_nomi, huquqiy_holati):
        self.tuman_nomi = tuman_nomi
        self.huquqiy_holati = huquqiy_holati
        Shahar.soni += 1
        self.__id = Shahar.soni  # unik ID

    # Shahar haqida ma'lumot
    def get_info(self):
        return f"{self.tuman_nomi}, huquqiy holati: {self.huquqiy_holati}"

    # ID olish
    def get_id(self):
        return self.__id

    # Holatni yangilash
    def update_holat(self, h):
        self.huquqiy_holati = h  # avvalgi holatni o‘zgartirish

    def __repr__(self):
        return self.tuman_nomi


class Viloyat:
    def __init__(self, nomi, yer_maydon, aholisi, respublika):
        self.nomi = nomi
        self.yer_maydon = yer_maydon
        self.aholisi = aholisi
        self.respublika = respublika
        self.shaharlar = []  # Viloyatga tegishli shaharlar ro'yxati

    # Viloyat haqida ma'lumot
    def get_info(self):
        return f"{self.nomi}, yer maydon: {self.yer_maydon}, aholisi: {self.aholisi}, respublika: {self.respublika}"

    # Shahar qo'shish
    def add_shahar(self, shahar):
        self.shaharlar.append(shahar)

    # Shaharlar ro'yxatini olish
    def get_shaharlar(self):
        return self.shaharlar

    # Shaharni o'chirish
    def remove_shahar(self, shahar):
        if shahar in self.shaharlar:
            self.shaharlar.remove(shahar)

    def __repr__(self):
        return self.nomi


# -------------------------
# Ob’ektlar yaratish
# -------------------------
sh1 = Shahar("Xiva", "Yaxshi")
sh2 = Shahar("Toshkent", "Yaxshi")

v1 = Viloyat("Xorazm", "6.1 ming km^2", "1958.2 ming kishi", "O'zbekiston")
v2 = Viloyat("Toshkent", "15.3 ming km^2", "3 mln", "O'zbekiston")

# Shaharlarni viloyatlarga qo'shish
v1.add_shahar(sh1)
v2.add_shahar(sh2)

# Natijalarni tekshirish
print(v1.get_info())
print("Viloyat shaharlar:", v1.get_shaharlar())

print(v2.get_info())
print("Viloyat shaharlar:", v2.get_shaharlar())

# Shahar ID va holatni yangilash
print("Shahar ID:", sh1.get_id())
sh1.update_holat("A'lo")
print("Yangilangan holat:", sh1.get_info())
