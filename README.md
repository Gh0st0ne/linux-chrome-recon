# linux-chrome-recon

"linux-chrome-recon" is a Information gathering tool used to enumerate all possible data about an user from Google-Chrome browser from any Linux distribution

## Intro
1.Loots possible data from Google-Chrome
2.Launches HTTP Server on /tmp directory (Usefull)
3.Simple script to receive data from Victim(One time run)
4.Clears the /tmp data when server is closed...

## Files retrieved :
1. History
2. Login Creds ( Cannot grab passwds , because its encrypted )
3. Keywords Searched
4. Autofill Data
5. Download History
6. Top Sites
7. User Profile Images

## Installation
```
https://github.com/monishmonish/linux-chrome-recon/
cd linux-chrome-recon/
pip3 install pandas
pip3 install wget
```
## To Run

1.On Victim Machine
```
python3 server.py
```

2.On Attacking Machine
```
python3 receivedata.py
```
Here the RHOST value must be the IP of the Victime machine

Incase if you get any permission error while writing the data on attacker side
Try,
```
sudo chmod 777 linux-chrome-recon
```

## To-Dos
If your are reading this...
Make sure you can add more modules to this script and notify me..
Dont forget to star and follow.


