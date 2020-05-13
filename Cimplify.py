import time
import serial
import paramiko 
from paramiko import SSHClient


global dataSet

def main():
    welcome()
    
def welcome():
    print("Welcome to Cimplify, the solution to Cisco Brainmelt!")
    print(" ")
    print(" ")
    print("[1] Create Initial Configuration")
    print(" ")
    print("[2] Configure other settings")
    print(" ")
    print("[3] Configure Serial")
    print(" ")
    print("[4] Configure SSH")
    print(" ")
    print("[5] Exit")

    userSel = input("Select an option:")

    if userSel == "1":
        initConf()
    if userSel == "2":
        additConf()
    if userSel == "3":
        print("Not develped yet.")
    if userSel == "4":
        sshConf()

def initConf():

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
    print(" ")
    userSel = input("Press Q to go home or Enter to continue configuring this device:")
    if userSel == ("Q"):
        welcome()
    if userSel == (""):
        additConf()

def vlan():
    portSpeed = 0 
    userSel = input("Is this a Gigabit, or Fastethernet switch? [G/F]")
    if userSel == "G":
        portSpeed = ("GigabitEthernet")
    if userSel == "F":
        portSpeed = ("FastEthernet")
    print("Port set to "+portSpeed+".")
    vlanID = input("VLAN ID Number: ")
    vlanName = input("VLAN Name: ")
    firstPort = input("Select first port in range: ")
    lastPort = input("Select last port in range: ")
    confirmGlobal = input("Press Enter when you are in global config.")
    if confirmGlobal =="":
        print("en")
        print("conf t")
        print("vlan "+vlanID)
        print("vlan name "+vlanName)
        print("no shut")

def switchConf():
    print("Switch Configuration")
    print("Use 'help' for options")
    print(" ")
    def command():
        userSel = input(">")
        if userSel == ("help"):
            print("Options are:")
            print("vlan,    etherchannel,    ")
            print("")
            command()

        if userSel == ("vlan"):
            vlan()
    command()

def additConf():
    devSel = input("Additional Configuration for which device?[R]outer/[S]witch: ")
    print("[R]outer")
    print(" ")
    print("[S]witch")
    if devSel == "R":
        routerConf()
    if devSel == "S":
        switchConf()

def sshConf():
    print("SSH Configuration")
    sshIp = input("IP Address: ")
    sshUser = input("Username: ")
    sshPass = input("Password: ")
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(sshUser+"@"+sshIp)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('?')
    print(ssh_stdout) #print the output of ls command

main()








