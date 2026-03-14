class Kompyuter:
    number=0
    def __init__(self,protsessori,ozu,xotirasi,narxi):
        self.protsessori=protsessori
        self.ozu=ozu
        self.xotirasi=xotirasi
        self.narxi=narxi
        Kompyuter.number+=1
        self.__id=Kompyuter.number
        
    def malumot(self):
        full=f"Ma'lumot:{self.protsessori} {self.ozu}"   
        return full  
    def narx_yangilash(self,qiymat):
        self.narxi=qiymat
        
        
a1=Kompyuter("INTEL CORE i5","4GB","256 GB SSD",4200000) 

print(a1.narxi)   
a1.narx_yangilash(4500000)        
print(a1.narxi)
