class Fan:
    def __init__(self,nomi,kredit):
        self.nomi=nomi
        self.kredit=kredit
        
    def get_info(self):
        return f"{self.nomi} {self.kredit}"
        
    def update_narx(self,n):
        self.kredit=self.kredit+n
        
    def __repr__(self):
        return self.nomi
            
            
obj1=Fan("Baza",6)
obj2=Fan("Elektronika",6)

class Talaba:
    def __init__(self,ism,familiya,guruh,shartnoma):
        self.ism=ism
        self.familiya=familiya
        self.guruh=guruh
        self.shartnoma=shartnoma
        self.fanlar=[]
        
    def get_info(self):
        return f"{self.ism} {self.familiya} {self.guruh} {self.shartnoma}" 

    def add_fanlar(self,T):
        self.fanlar.append(T)
        
    def get_fanlar(self):
        return self.fanlar
    
    def remove_fan(self,fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)

    
    
a1=Talaba("Muxlisa","Rajabboyeva","941-22","Kontrakt") 
a2=Talaba("Mashhura","Fayzullayeva","942-22","Kontrakt")   
   







        
