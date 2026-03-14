class Shaxs:
    __odamlar_soni=0
    def __init__(self,ism,familiya,ish_joyi,JSHSHIR):
        Shaxs.__odamlar_soni+=1
        self.__JSHSHIR=JSHSHIR
        self.ism=ism
        self.familiya=familiya
        self.ish_joyi=ish_joyi
        
    def change_JSHSHIR(self,new):
        self.__JSHSHIR=new
        
            
        
    def get_JSHSHIR(self):
        return self.__JSHSHIR
    
    @classmethod
    def get_count(cls):
        return cls.__odamlar_soni
        
    def get_info(self):
        return f"{self.ism} {self.familiya} {self.ish_joyi}"
    
obj1=Shaxs("Muxlisa","Rajabboyeva","Ishsiz",78889996543215)
obj2=Shaxs("Fotima","Nurmetova","Ishsiz",12345678908765)
obj3=Shaxs("Nafosat","Rustambekova","Ishsiz",34567890234579)

print(obj1.get_info())       # Muxlisa Rajabboyeva Ishsiz
print(obj1.get_JSHSHIR())    # 78889996543215

obj1.change_JSHSHIR(98765432101234)
print(obj1.get_JSHSHIR())    # 98765432101234

print(Shaxs.get_count())     # 3
        
