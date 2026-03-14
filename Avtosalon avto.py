class Avtosalon:
    def __init__(self, nomi, soni, turi, narxi):
        self.nomi = nomi
        self.soni = soni
        self.turi = turi
        self.narxi = narxi

    def get_info(self):
        return f"Salon: {self.nomi}, Model: {self.turi}, Soni: {self.soni}, Narxi: {self.narxi} mln"

    def update_narx(self, n):
        self.narxi = self.narxi + n


a1 = Avtosalon("Asaka", 900, "Jentra", 170)
a2 = Avtosalon("Hyundai", 1000, "Malibu", 250)


class Avto:
    def __init__(self, nomi, manzili, xizmat_korsatish):
        self.nomi = nomi
        self.manzili = manzili
        self.xizmat_korsatish = xizmat_korsatish
        self.avtomobillar = []

    def get_info(self):
        return f"{self.nomi}, {self.manzili}, {self.xizmat_korsatish}"

    def __repr__(self):
        return self.nomi

    def __call__(self, avt):
        self.avtomobillar.append(avt)

    def __getitem__(self, index):
        return self.avtomobillar[index]

    def get_avtomobil(self):
        return self.avtomobillar


d1 = Avto("Avtomoyka", "Urganch", "Avtomobil yuvish")
d2 = Avto("Zapravka", "Xiva", "Moy yangilash")

d1(a1)
d1(a2)

print(d1[0].get_info())
