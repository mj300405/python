masterPassword=input('Master password: ')

def view():
    f=open("passwords.txt", 'r')
    for line in f.readlines():
        print(line.rstrip())

def add():
    name=input('Account name: ')
    password=input('Password: ')
        
    f=open('passwords.txt', 'a')
    f.write(name + '|' + password +'\n')
    f.close()
    #with open('passwords.txt', 'a') as f:
        #f.write(name + '|' + password +'\n')



while True:
    mode=input('Would you like to add a new password or view existing ones? (view, add, q)')
    if mode=='q':
        break
    
    if mode=='view':
        view()
    elif mode=='add':
        add()
    else:
        print('Invalid mode!')
        continue
    