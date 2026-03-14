class Ishchi:
    def __init__(self, ism, firma_raqam, staj):
        self.ism = ism
        self.firma_raqam = firma_raqam
        self.staj = staj  # ishchi staji yillarda

    def get_info(self):
        return f"{self.ism}, firma raqami: {self.firma_raqam}, staji: {self.staj} yil"

    def update_staji(self, s):  # stajni oshirish
        self.staj += s

    def __repr__(self):
        return self.ism


# -------------------------
# Ob’ektlar yaratish
# -------------------------
i1 = Ishchi("Sarvar", 87654322345, 2)
i2 = Ishchi("Komiljon", 434569002, 3)

# Ishchilar haqida ma’lumot
print(i1.get_info())
print(i2.get_info())

# Stajni yangilash
i1.update_staji(1)
print("Yangilangan staj:", i1.get_info())
