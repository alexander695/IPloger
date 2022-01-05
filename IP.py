import os 
from colorama import Fore 

#banner#
def menu():
     print (Fore.YELLOW + '  ▄█   █████████▄ ')          
     print (Fore.YELLOW + '  ██   ██      ██ ')                   
     print (Fore.YELLOW + '  ██   ██      ██ ')          
     print (Fore.YELLOW + '  ██   ██████████ ')                      
     print (Fore.YELLOW + '  ██   ██         ')                
     print (Fore.YELLOW + '  ██   ██         ')                                
     print (Fore.YELLOW + '  ██   ██         ')                    
     print (Fore.YELLOW + '  ██   ██         ')

     print ('opcions')
     print ("\t1 start")
     print ("\t2 install ngrok")
while True:
    
 menu()
   
 opcionMenu = input("select a opcion >>")

 if opcionMenu=="1":
     if opcionMenu=="1":
         print ("starting ngrok")
         os.system("sudo service apache2 start")
         os.system("chmod 777 ngrok")
         os.system("cp -a site/index.html. /www/html/")
         os.system("xterm -hold -e ./ngrok http 80 & xterm -hold -e python Cat.py")
         input("\npress enter to back")
         os.system("clear")
     
 else:
     print("A problem was ocurred, ngrok was installed?")       
     os.system("clear")

 if opcionMenu=="2":
     os.system("sudo apt-get install unzip -y")
     os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
     os.system("unzip ngrok-stable-linux-amd64.zip")
     input("\npress enter to back")
     os.system("clear")
 
 else:
     print("an error was ocurred with the installation :c")
     os.system("clear")

