import serial

print("Welcome to Cimplify, the solution to Cisco Brainmelt!")
print(" ")
print(" ")
print("[1] Create Router Configuration")
print(" ")
print("[2] Create Switch Configuration")
print(" ")
print("[3] Exit")
print(" ")

userSel = input("Select an option:")

if userSel == "1":
	print("Router Config Selected!")
	username = input("Username:")
	secret = input("Password (encrypted by default):")
	print("Privilege set to 15 by default.")
	domainname = input("Domain-Name:")
	hostname = input("Hostname:")
	cryptoBits = input("Select key length of 512-2048 for SSH:")
	print ("username "+username+"privilege 15 secret "+secret)
	print("conf t")
	print("ip domain-name "+domainname)
	print("hostname "+hostname)
	print("crypto key generate rsa")
	print(cryptoBits)








