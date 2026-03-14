class Futbolchi:
    gollar_soni_total = 0  # class darajasida barcha futbolchilarning gollari

    def __init__(self, ismi, yoshi, pozitsiya, gollar_soni):
        self.ismi = ismi
        self.yoshi = yoshi
        self.pozitsiya = pozitsiya
        self.gollar_soni = gollar_soni

        Futbolchi.gollar_soni_total += gollar_soni
        self.__id = Futbolchi.gollar_soni_total  # unik ID

    def get_info(self):
        return f"{self.ismi}, {self.yoshi} yosh, {self.pozitsiya}, gollar: {self.gollar_soni}"

    def update_gollar(self, g):
        self.gollar_soni += g
        Futbolchi.gollar_soni_total += g  # class umumiy gol sonini yangilash

    def __repr__(self):
        return self.ismi


class Jamoa:
    def __init__(self, nomi, galaba_soni, maglubiyat_soni):
        self.nomi = nomi
        self.galaba_soni = galaba_soni
        self.maglubiyat_soni = maglubiyat_soni
        self.futbolchilar = []

    def get_info(self):
        return f"{self.nomi}: {self.galaba_soni} g'alaba, {self.maglubiyat_soni} mag'lubiyat"

    def add_futbolchi(self, futbolchi):
        self.futbolchilar.append(futbolchi)

    def get_futbolchilar(self):
        return self.futbolchilar

    def remove_futbolchi(self, futbolchi):
        if futbolchi in self.futbolchilar:
            self.futbolchilar.remove(futbolchi)

    def umumiy_gollar(self):
        return sum(f.gollar_soni for f in self.futbolchilar)
        


# Ob’ektlar yaratish va ishlatish

f1 = Futbolchi("Ronaldo", 38, "Hujumchi", 757)
f2 = Futbolchi("Messi", 36, "Hujumchi", 671)

j1 = Jamoa("Real Madrid", 95, 2)
j2 = Jamoa("Barselona", 91, 3)

# Futbolchilarni jamoalarga qo'shish
j1.add_futbolchi(f1)
j2.add_futbolchi(f2)

# Natijalarni tekshirish
print(j1.get_info())
print(j1.get_futbolchilar())
print("Jamoaning umumiy gollari:", j1.umumiy_gollar())

print(j2.get_info())
print(j2.get_futbolchilar())
print("Jamoaning umumiy gollari:", j2.umumiy_gollar())
