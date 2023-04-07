import os
import subprocess
import re


host = str(input ("Please enter the name of the host \n"))
adresa = str(input ("Enter an IP address \n"))

print ("Checking if the host and IP address already exist")

file = open("/home/your_user/.ssh/config", "r")
for line in file:
    if re.search(host, line):
        print (line)
    if re.search(adresa, line):
        print(line)
        print ("Do you want me to proceed further?")

user = str(input ("Enter the username \n"))
port = str(input("Enter the port \n"))


with open("/home/your_user/.ssh/config", "a") as ssh_config:
        ssh_config.write("\n" + "Host " + host + "\n" + "Hostname " + adresa + "\n" + "User " + user + "\n" + "Port " + port )
ssh_config.close()

command = "ssh-copy-id -p %s %s@%s" % (port, user, adresa)
subprocess.call(command, shell=True)

