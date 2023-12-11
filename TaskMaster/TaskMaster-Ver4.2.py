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
        csv_reader = csv.reader(file, delimiter=',')
        
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
                print(f"|| Jurusan : {row[2]}{' ' * (29 - len(row[2]))}      | NIM   : {row[1]}{' ' * (30 - len(row[1]))}")
                print('---------------------------------------------------------------------')
                break
        
        if not found:
            print('Akun tidak ditemukan')
    
    os.system('pause')
    os.system('cls')
    dashboard_menu()

class Task:
    def __init__(self,title,description,due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.is_completed = False
    
    def complete(self):
        self.is_completed = True
        
class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add_task(self,title,description,due_date):
        task = Task(title,description,due_date)
        self.tasks.append(task)
    
    def view_task(self):
        if not self.tasks:
            print("Tugas tidak ditemukan !!")
        else:
            print('Tasks: ')
            for index,task in enumerate(self.tasks, start=1):
                status = "Selesai" if task.is_completed else "Belum Selesai"
                print(f"{index}, {task.title} - Due: {task.due_date} - Status: {status}")
                
    def complete_task(self,task_index):
        if 0 <= task_index< len(self.tasks):
            self.tasks[task_index].complete()
            print("Tugas telah selesai")
        
        else:
            print("Tugas tidak dikerjakan")


def save_tasks_to_file(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task.title},{task.description},{task.due_date},{task.is_completed}\n")

def load_tasks_from_file():
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                data = line.strip().split(',')
                title, description, due_date, is_completed = data
                is_completed = is_completed == "True"  # Convert string to boolean
                task = Task(title, description, due_date)
                task.is_completed = is_completed
                tasks.append(task)
    except FileNotFoundError:
        pass
    return tasks

def to_do_list():

    task_manager = TaskManager()
    task_manager.tasks = load_tasks_from_file()

    while True:
        print_header()
        print('---------------------------------------------------------------------')
        print('|| [1]. Tambahkan Tugas           | [2]. Lihat Deadline Tugas      ||')
        print('|| [3]. Selesaikan Tugas          | [4]. Keluar                    ||')
        print('---------------------------------------------------------------------')
        pilihan = input("\> ")
        print('\n')

        if pilihan == '1':
            os.system('cls')
            print_header()
            title = input('|| Judul Tugas : ')
            description = input('|| Deskripsi Tugas : ')
            due_date = input("|| Tanggal Deadline (YYYY-MM-DD) : ")
            task_manager.add_task(title, description, due_date)
            save_tasks_to_file(task_manager.tasks)
            print("-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("   > TUGAS BERHASIL DI UPDATE <  ")
            print('\n')
            
            os.system('pause')
            os.system('cls')

        elif pilihan == '2':
            os.system('cls')
            print_header()
            task_manager.view_task()
            
            print('\n')
            
            os.system('pause')
            os.system('cls')

        elif pilihan == '3':
            print_header()
            task_index = int(input("|| Masukan Index Tugas Untuk Diselesaikan : ")) - 1
            task_manager.complete_task(task_index)
            save_tasks_to_file(task_manager.tasks)
            
            os.system('pause')
            os.system('cls')

        elif pilihan == '4':
            print_header()
            
            os.system('cls')
            dashboard_menu()
            break  # Keluar dari loop dan program

        else:
            print_header()
            print("Pilihan Anda tidak ada dalam menu!")
            
            os.system('cls')
            to_do_list()
            
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
if __name__ == "__main__":
    menu()
