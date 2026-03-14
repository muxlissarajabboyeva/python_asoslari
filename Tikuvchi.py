class Tikuvchi:
    soni = 0  # class attribute

    def __init__(self, ism, familiya, lavozim, staj):
        self.ism = ism
        self.familiya = familiya
        self.lavozim = lavozim
        self.staj = staj
        Tikuvchi.soni += 1
        self.__id = Tikuvchi.soni

    def get_info(self):
        return f"{self.ism} {self.familiya} {self.lavozim} {self.staj}"

    def get_id(self):
        return self.__id        

    def updete_lavozimi(self, yangi_lavozim):
        self.lavozim = yangi_lavozim

    def __repr__(self):
        return self.ism


# Tikuvchilar obyektlari
t1 = Tikuvchi("Malika", "Abdullayeva", "Malakali", 7)
t2 = Tikuvchi("Durdona", "Murodova", "Asistent", 3)


# Tikuvchilik sexi
class Tikuvchilik_sexi:
    def __init__(self, nomi, boshliq, ishchi_soni):
        self.nomi = nomi
        self.boshliq = boshliq
        self.ishchi_soni = ishchi_soni
        self.Tikuvchilar = []

    def get_info(self):
        return f"{self.nomi} {self.boshliq} {self.ishchi_soni}" 

    def add_Tikuvchilar(self, t):
        self.Tikuvchilar.append(t)

    def get_Tikuvchilar(self):
        return self.Tikuvchilar

    def remove_tikuvchi(self, tikuvchi):
        if tikuvchi in self.Tikuvchilar:
            self.Tikuvchilar.remove(tikuvchi)


# Sex obyektlari
s1 = Tikuvchilik_sexi("Mohir", "Abror Ro'zimov", 300)
s2 = Tikuvchilik_sexi("Chevar qollar", "Saida Odilova", 700)

# Tikuvchini sexga qo'shish
s1.add_Tikuvchilar(t1)
s1.add_Tikuvchilar(t2)

# Tekshirish
print(s1.get_info())        # Mohir Abror Ro'zimov 300
print(s1.get_Tikuvchilar()) # [Malika, Durdona]
