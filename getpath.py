import subprocess
import os
import sys

if os.name=='posix':
    user=(os.environ['USER'])
    home=(os.environ['HOME'])
    os.chdir(home+'/.config/google-chrome/Default/')
    data_path=os.getcwd()
    
else:
    print("MADE ONLY FOR LINUX")
    sys.exit()

