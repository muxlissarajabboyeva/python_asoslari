class Ishchi:
    def __init__(self, ismi, guruh_raqami, staji):
        self.ismi = ismi
        self.guruh_raqami = guruh_raqami
        self.staji = staji  # ish staji yillarda

    def get_info(self):
        return f"{self.ismi}, guruh: {self.guruh_raqami}, staji: {self.staji} yil"

    def update_malaka(self, m):  # eski: updete_malaka → update_malaka
        self.staji += m  # stajni oshirish

    def __repr__(self):
        return self.ismi


class Korxona:
    def __init__(self, nomi, firma_raqami, manzili):
        self.nomi = nomi
        self.firma_raqami = firma_raqami
        self.manzili = manzili
        self.ishchilar = []  # instance atributlari kichik harf bilan

    def get_info(self):
        return f"{self.nomi}, firma raqami: {self.firma_raqami}, manzil: {self.manzili}"

    def add_ishchi(self, ishchi):
        self.ishchilar.append(ishchi)

    def get_ishchilar(self):
        return self.ishchilar

    def remove_ishchi(self, ishchi):
        if ishchi in self.ishchilar:
            self.ishchilar.remove(ishchi)
            
    def umumiy_staj(self):
        return sum(i.staji for i in self.ishchilar)  # Korxona ishchilari staji yig'indisi


# -------------------------
# Ob’ektlar yaratish va ishlatish
# -------------------------

i1 = Ishchi("Sarvar", 6, 2)
i2 = Ishchi("Komiljon", 4, 3)

k1 = Korxona("Avtosalon", 897899900, "Xorazm viloyati")
k2 = Korxona("Neft zavodi", 12345668, "Navoiy viloyati")

# Ishchilarni korxonalarga qo'shish
k1.add_ishchi(i1)
k1.add_ishchi(i2)

# Natijalarni tekshirish
print(k1.get_info())
print(k1.get_ishchilar())
print("Korxona ishchilari umumiy staji:", k1.umumiy_staj())

print(k2.get_info())
print(k2.get_ishchilar())
print("Korxona ishchilari umumiy staji:", k2.umumiy_staj())
