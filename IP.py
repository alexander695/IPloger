import os 
from colorama import Fore 
import webbrowser
import time

#banner#
def menu():
     print (Fore.LIGHTYELLOW_EX + '  ▄█   █████████▄ ')          
     print (Fore.LIGHTYELLOW_EX + '  ██   ██      ██ ')                   
     print (Fore.LIGHTYELLOW_EX + '  ██   ██      ██ ')          
     print (Fore.LIGHTYELLOW_EX + '  ██   ██████████ ')                      
     print (Fore.LIGHTYELLOW_EX + '  ██   ██         ')                
     print (Fore.LIGHTYELLOW_EX + '  ██   ██         ')                                
     print (Fore.LIGHTYELLOW_EX + '  ██   ██         ')                    
     print (Fore.LIGHTYELLOW_EX + '  ██   ██         ')

     print (Fore.LIGHTRED_EX + '\nopcions')
     print (Fore.LIGHTGREEN_EX + "\t1 start")
     print (Fore.LIGHTGREEN_EX + "\t2 install")
while True:
    
 menu()
   
 opcionMenu = input("select a opcion >>")

 if opcionMenu=="1":
     if opcionMenu=="1":
         print ("starting ngrok")
         os.system("chmod 777 ngrok")
         os.system("cp -a site/index.html /var/www/html/index.html")
         os.system("xterm -hold -e ./ngrok http 8080")
         webbrowser.open("http://127.0.0.1:4040", new=2, autoraise=True)
         print("If ngrok don't start run install")
         print("If web browser don't open go to http://127.0.0.1:4040")
         input("\npress enter to stop server")
         os.system("clear")
     

 if opcionMenu=="2":
     os.system("sudo dpkg --configure -a")
     os.system("sudo apt-get install unzip -y")
     os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
     os.system("unzip ngrok-stable-linux-amd64.zip")
     os.system("apt install xterm")
     os.system("pip install colorama")
     os.system("clear")
     print("\nrequirements installed")
     time.sleep(2)
     os.system("clear")
 
 else:
     input("An error was ocurred press enter to back")
     os.system("clear")


