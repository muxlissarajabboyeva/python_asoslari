class Kitob:
    def __init__(self, nomi):
        self.nomi = nomi
        # Faylni yaratish
        with open(self.nomi, "w") as fayl:
            pass

    # Faylga yozish (avvalgi matnni o'chirib yozadi)
    def yozish(self, matn):
        with open(self.nomi, "w") as fayl:
            fayl.write(matn)

    # Fayldan o'qish
    def uqish(self):
        with open(self.nomi, "r") as fayl:
            return fayl.read()

    # Fayl oxiriga matn qo'shish
    def add_text(self, matn):
        with open(self.nomi, "a") as fayl:
            fayl.write(matn)

    # Fayldagi birinchi qatorni o'qish
    def first_row(self):
        with open(self.nomi, "r") as fayl:
            return fayl.readline()

    # Fayl nomini chiqarish
    def __repr__(self):
        return f"Kitob({self.nomi})"


# Ishlatish misoli
file = Kitob("myfile.txt") 

file.yozish("Kelajak\n")          # Faylga yozish
file.add_text("Bilim\n")          # Fayl oxiriga qo'shish

print(file.uqish())               # Fayldagi hamma matnni o'qish
print(file.first_row())           # Fayldagi birinchi qator
print(file)                       # Kitob(myfile.txt)
