import time
import serial.tools.list_ports

global dataSet

def main():
    serialConf()
    welcome()
    prompt()
    
def welcome():
    print("Welcome to Cimplify, the solution to Cisco Brainmelt!")
    print(" ")
    print(" ")
    print("[1] Create Router Configuration")
    print(" ")
    print("[2] Create Switch Configuration")
    print(" ")
    print("[3] Exit")
    print(" ")

def serialConf():
    comPorts = list(serial.tools.list_ports.comports())
    print (comPorts)
    
def prompt():

    userSel = input("Select an option:")

    if userSel == "1":
        print("Router Config Selected!")
        username = input("Username:")
        secret = input("Password (encrypted by default):")
        print("Privilege set to 15 by default.")
        domainname = input("Domain-Name:")
        hostname = input("Hostname:")
        cryptoBits = input("Select key length of 512-2048 for SSH:")

        dataSet = [
            "en",
            "conf t",
            "username "+username+" privilege 15 secret "+secret,
            "ip domain-name "+domainname,
            "hostname "+hostname,
            "crypto key generate rsa",
            cryptoBits,
            "line vty 0 4",
            "transport input ssh",
            "login local"]
        
        print("EXPORT THROUGH SERIAL")
        baud = input("Select Baudrate (Press Enter for default of 9600):")
        if baud ==(""):
            baud = (9600)
        print("Baudrate set to "+str(baud)+("."))
        cont = input("Make sure you're in global config. Press enter when you are ready.")
        print(" ")
        print(" ")
        print(" ")
        print(*dataSet, sep = "\n") 

main()








