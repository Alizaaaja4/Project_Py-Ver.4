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
    nim_input = input("|| NIM : ")
    email_input = input("|| Email : ")
    print('--------------------------------------------------------------------')
    password_input = input("|| Password : ")
    print('--------------------------------------------------------------------')
    
    databaseStudents = []
    with open("Database Students Telkom.csv", 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            databaseStudents.append({'email': row[3], 'nim': row[1], 'password': row[4]})
            
    datalogin = []
    for i in databaseStudents:
        if email_input == i['email'] and nim_input == i['nim'] and password_input == i['password']:
            datalogin.append(i)
            print("\n Berhasil Login !!")
            os.system('pause')
            os.system('cls')
            dashboard_menu()
            return  # Keluar dari fungsi sign_in() setelah berhasil login
            
    if len(datalogin) == 0:
        print("Akun anda belum terdaftar !! ")
    
    os.system('pause')
    os.system('cls')
    menu()
     
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

def user_account():
    print_header()
    nim_input = input("Enter your NIM: ")
    
    with open("Database Students Telkom.csv", 'r') as file:
        csv_reader = csv.reader(file)
        found = False
        
        for row in csv_reader:
            if row[1] == nim_input:
                found = True
                print('---------------------------------------------------------------------')
                print(f"|| Nama Lengkap : {row[0]}{' ' * (29-len(row[0]))} | Email : {row[3]}{' ' * (30 - len(row[3]))}")
                print('---------------------------------------------------------------------')
                print(f"|| Jurusan : {row[2]}{' ' * (73 - len(row[2]))}    | NIM   : {row[1]}{' ' * (30 - len(row[1]))}")
                print('---------------------------------------------------------------------')
                break
        
        if not found:
            print('Akun tidak ditemukan')
    
    os.system('pause')
    os.system('cls')
    dashboard_menu()

def to_do_list():
    print('print')
    
def dashboard_menu():
    print_header()
    
    print('---------------------------------------------------------------------')
    print('|| [1]. Lihat Akun       [2]. Website Learning Management System   ||')
    print('|| [3]. To Do List       [4]. Keluar                               ||')
    print('---------------------------------------------------------------------')
    pilihan = input("\> ")
    print('\n')
    
    if pilihan == '1':
        os.system('cls')
        user_account()
    
    elif pilihan == '2':
        os.system('cls')
        print('Continue to visit the site ?')
        os.system('pause')
        webbrowser.open('https://lms.telkomuniversity.ac.id/my/')
        
        dashboard_menu()
    
    elif pilihan == '3':
        os.system('cls')
        to_do_list()
    
    elif pilihan == '4':
        os.system('cls')
        menu()
    
    else:
        print("Your selection is not in the menu !!")
        os.system('cls')
        dashboard_menu()
        
# all function
menu()
