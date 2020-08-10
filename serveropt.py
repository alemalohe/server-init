import os 
   
username = str(input("Username (jhon): "))

os.system("adduser")
os.system("id " + username)
os.system("usermod -aG sudo " + username)
os.system("id " + username)
os.system("sudo su - " + username)
os.system("whoami")
os.system("mkdir ~/.ssh")
os.system("chmod 700 ~/.ssh")

print("\nsudo nano authorized_keys and then paste the public key from under Comment -> to the end with ==")
print("example")
print("\nssh-rsa AAAB3NzaC1yc2EAAAABJQAAAQEAuAxkZNgIOFPV6g6bqxK0J9mKqsZZjTqTKpUJqs5zvO4TDUeqVb1kFuXFW1HBD+lgpo+4Z0uTJPSzDfuxxFSwSZAzJi4yXBEjsSEiLF3+LoQm7mswTXLI8ev9US9JNMS6vM5oxn5Yfwx9J5HZjFfalASpILgX94PWqppzJtGccehIaMSxeiAYBi7UhP18rzXcPfDAVCRd8dtrkDNSvSR7grhleHfQxL8I+NRrKe5ZGnsWW5vPE")

input("/nPress Enter to continue...")

os.system("nano ~/.ssh/authorized_keys")
os.system("chmod 600 ~/.ssh/authorized_keys")
os.system("sudo service ssh restart")

print("then login with the new user as username as >> " + username)
