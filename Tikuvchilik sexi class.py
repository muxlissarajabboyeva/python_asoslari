class Tikuvchilik_sexi:
    def __init__(self,ismi,boshliq,ishchi_soni,zavod):
        self.ismi=ismi
        self.boshliq=boshliq
        self.ishchi_soni=ishchi_soni
        self.zavod=zavod
      
        
    def get_info(self):
        return f"{self.ismi} {self.boshliq} {self.ishchi_soni}" 

        
    def set_Ishchi_soni(self,i):
        self.ishchi_soni=self.ishchi_soni+i
    

s1=Tikuvchilik_sexi("Mohir","Abror Ro'zimov",300,"COLA zavod")
s2=Tikuvchilik_sexi("Chevar qollar", "Saida Odilova", 700,"Kiyim-kechak")
