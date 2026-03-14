class Shaxs:
    def __init__(self,ism,familiya,ish_joyi):
        self.ism=ism
        self.familiya=familiya
        self.ish_joyi=ish_joyi
        
    def get_info(self) :
        return f"{self.ism} {self.familiya} {self.ish_joyi} "
    
    
    def __repr__(self):
        return self.ism
    
class Foydalanuvchi(Shaxs):
    def __init__(self,ism,familiya,ish_joyi,kasbi):
        super().__init__(ism,familiya,ish_joyi)
        self.kasbi=kasbi
    
    def get_info(self):
        full=super().get_info()
        full+=self.kasbi
        return full 

obj1=Foydalanuvchi("Muxlisa","Rajabboyeva","Ishsz","Student")   
 
class Admin(Foydalanuvchi):
    def __init__(self,ism,familiya,ish_joyi,kasbi,oylik):
        super().__init__(ism,familiya,ish_joyi,kasbi)
        self.oylik=oylik
    
    def get_info(self):
        full=super().get_info()
        full+=self.oylik
        return full 
    
    def ban_user(self):
        return "Foydalanuvchi bloklandi"

obj1 = Shaxs("Ali", "Valiyev", "Ishsiz")
obj2 = Foydalanuvchi("Muxlisa","Rajabboyeva","Ishsiz","Student")
obj3 = Admin("Botir","Karimov","Ishsiz","Student", "1000$")

# Polimorfizm ishlaydi:
print(obj1.get_info())  # Ali Valiyev Ishsiz
print(obj2.get_info())  # Muxlisa Rajabboyeva Ishsiz Student
print(obj3.get_info())  # Botir Karimov Ishsiz Student1000$
