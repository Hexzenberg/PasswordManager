from cryptography.fernet import Fernet
'''
def wk():
    k=Fernet.generate_key()
    with open("key.key","wb") as key_file:#Write in bytes is wb
        key_file.write(k)
wk()
Since we have created the key already we have to comment this function out so as to not create multiple keys evevrytime we run the code
'''
def lk():
    f=open("key.key",'rb')#read in bytes
    k=f.read()
    f.close()#Since we did not use with here we have to close the file
    return k
pwd=input("Enter the master password:\n")
k=lk()+pwd.encode()
fer=Fernet(k)#Initialising the encryption module
def view():
    with open('passwords.txt','r') as f:#With automatically closes the file for us!
        for l in f.readlines():
            d=l.rstrip()#Removes the invisible '\n'
            n,pw=d.split('|')
            print("Account name: ",n,"\nPassword: ",fer.decrypt(pw.encode()).decode())
def add():
    name=input("Account name:\n")
    p=input("Password:\n")
    with open('passwords.txt','a') as f:#Unlike write or read 'a' helps to create the file if not already made
        f.write(name+' | '+fer.encrypt(p.encode()).decode() +'\n')#Encoding the password into bytes and then encrypting it and decoding
while True:
    mode=input("Would you like to enter a new password or view the existing password?(view,add),press q to quit.\n").lower()
    if mode=="q":
        break
    elif mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid input!")