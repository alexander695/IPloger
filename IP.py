import os 
from colorama import Fore 
import webbrowser
import time

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
         os.system("cp -a site/index.html /var/www/html/index.html")
         os.system("chmod 777 ngrok")
         os.system("xterm -hold -e ./ngrok http 8080")
         webbrowser.open("http://127.0.0.1:4040", new=2, autoraise=True)
         print("If you don't have any idea of ngrok go to https://github.com/alexander695/IPloger")
         print("If web browser don't, open and go to http://127.0.0.1:4040")
         input("\npress enter to back")
         os.system("clear")
     

 if opcionMenu=="2":
     os.system("sudo apt-get install unzip -y")
     os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
     os.system("unzip ngrok-stable-linux-amd64.zip")
     print("Ngrok was installed")
     time.sleep(3)
 
 else:
     input("An error was ocurred press enter to back")


