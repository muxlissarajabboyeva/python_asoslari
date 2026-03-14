class Talaba:
    __talabalar_soni=0
    def __init__(self,ism,familiya,guruh,shartnoma):
        Talaba.__talabalar_soni+=1
        self.__id=Talaba.__talabalar_soni
        self.ism=ism
        self.familiya=familiya
        self.guruh=guruh
        self.shartnoma=shartnoma
        
    def change_id(self,new):
        self.__id=new
        
        
    def get_id(self):
        return self.__id
    
    @classmethod
    def get_count(cls):
        return cls.__talabalar_soni
        
    def get_info(self):
        return f"{self.ism} {self.familiya} {self.guruh}"
    
obj1=Talaba("Muxlisa","Rajabboyeva","941-22","Kontrakt")
obj2=Talaba("Fotima","Nurmetova","941-22","Kontrakt")
obj3=Talaba("Nafosat","Rustambekova","941-22","Kontrakt")
        
