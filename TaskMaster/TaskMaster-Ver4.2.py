import os
import csv
import webbrowser

def print_header():
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('||                            Task Master                          ||')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('||                 Developer by Aliza Nurfitrian [ALL]             ||')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    
def sign_up():
    print_header()
    
    print('--------------------------------------------------------------------')
    name = input("|| Nama Lengkap :")
    nim = input('|| NIM : ')
    jurusan = input('|| Jurusan : ')
    print('--------------------------------------------------------------------')
    email = input('|| Email : ')
    password = input('|| Password : ')
    print('--------------------------------------------------------------------')
    
    databaseStudents = []
    
    with open ("Database Students Telkom.csv", 'r') as file:
        csv_reader = csv.reader(file, delimiter='|')
        
        for row in csv_reader:
            databaseStudents.append({'name' : row[0], 'nim' : row[1], 'jurusan' : row[2], 'email' :row[3], 'password' : row[4]})
            
    nim_ada = False

    for account in databaseStudents :
        if nim == account['nim']:
            print("NIM sudah digunakan, silahkan periksa kembali NIM anda !!")
            nim_ada = True
            break
        
    if nim_ada == False:
        newdata = {'name': name, 'nim': nim, 'jurusan': jurusan, 'email' : email, 'password': password}
        with open('Database Students Telkom.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=newdata.keys())
            writer.writerow(newdata)
            
    print('  > SINKRONSASI DATA TELAH SESUAI DENGAN Learning Management System < ')
    
    os.system('pause')
    os.system('cls')
    menu()
    
def sign_in():
    print_header()
    
    print('--------------------------------------------------------------------')
    email_input = input("|| Email : ")
    nim_input = input("|| NIM : ")
    print('--------------------------------------------------------------------')
    
    databaseStudents = []
    with open("Database Students Telkom.csv", 'r') as file:
        csv_reader = csv.reader(file, delimiter= '|')
        for row in csv_reader:
            databaseStudents.append({'email' : row[3], 'nim' : row[1]})
            
    datalogin = []
    for i in databaseStudents:
        if email_input == i['email'] and nim_input ==
     
def logout():
    print('Success Logout !!!')

def menu():
    print_header()
    
    print('---------------------------------------------------------------------')
    print('|| [1]. Sign Up for Students                                       ||')
    print('|| [2]. Sign In for Students                                       ||')
    print('|| [3]. Logout                                                     ||')
    print('---------------------------------------------------------------------')
    pilihan = input('/> ')
    print('\n')
    
    if pilihan == '1':
        os.system('cls')
        sign_up()
        
    elif pilihan == '2':
        os.system('cls')
        sign_in()
    
    elif pilihan == '3':
        os.system('cls')
        logout()
    
    else: 
        print("Your selection is not in the menu !!")
        os.system('cls')
        menu()
    
# all function
menu()
