from methods import *
import time
import re

# Register
def register():
    print("_____REGISTER_____")
    while True:
        firstname = input("First Name: ")
        if not len(firstname)>0:
            print("Enter the Firstname!")
        else:
            break
    while True:
        lastname = input("Last Name: ")
        if not len(lastname) > 0:
            print("Enter thr Lastname!")
        else:
            break
    name=firstname+" "+lastname
    
    while True:
        email = input("Email: ")
        if not len(email) > 0:
            print("Enter the Email!")
        else:
            if not check(email):
                print("Enter the correct format!")
            else:
                break
            
    while True:
        password = input("Password: ")
        if len(password) < 6:
            print("Password can't less than 6 or blank")
        else:
            break
        
    while True:
        confirm = input("Confirm_Password: ")
        if (len(confirm)==0 or
            confirm!=password):
            print("Re Enter the password!")
        else:
            break
        
    while True:
        phone = input("Mobile: +20")
        if len(phone)!=10:
            print("The phone_number must be 10 digits!")
        else:
            try:
                v=int(phone)
                break
            except ValueError:
                print("The phone_number must be 10 digits!")
        

    print("Creating account...")
    user = {"name":name,
            "mail":email,
            "password":password,
            "phone":"+20"+phone}
    data=open("DataBase/users_table.txt","w") #you must manually create a DataBase Folder 
    while True:
        data=open("DataBase/users_table.txt","r") 
        if name in data.read():
            print("this Name is used before!")
            data.close()
            break
        else:
            data=open("DataBase/users_table.txt","r") 
            if phone in data.read():
                print("this Number is used before!")
                data.close()
                break
            else:
                data=open("DataBase/users_table.txt","r") 
                if email in data.read():
                    print("this Email is used before!")
                    data.close()
                    break
            
        data=open("DataBase/users_table.txt","a")
        data.write("--------------------------------------------------------------------------------------------------------------------------------------------")
        data.write("\n"+str(user)+"\n")
        data.close()
        time.sleep(1)
        print("Account has been created")
        return profile(email.split("@")[0])
    
# Login
def login():
    print("_____LOGIN_____")
    
    while True:
        email = input("Email: ")
        if not len(email) > 0:
            print("Enter the Email!")
        else:
            if not check(email):
                print("Enter the correct format!")
            else:
                break
    while True:
        password = input("Password: ")
        if  len(password) < 6:
            print("Password can't be less than 6 or blank")
        else:
            break
    if(mailauth(email) and passauth(password)):
        with open("DataBase/users_table.txt","r") as data:
            for line in data:
                if email in line:
                    if password in line:
                        print("Login Successful")
                        return profile(email.split("@")[0])
                    print("\nInvalid email or password")
                    login()
    else:
        print("\nError! There is no account like this!!")
        print("Please Register...")
        reegister()
        


# Create a Project      
def create_project(username,Id):
    print("_____NEW PROJECT_____")
    while True:
        title = input("Title: ")
        if not len(title) > 0:
            print("Enter the title of project!")
        else:
            data=open("DataBase/projects_table.txt","r") 
            if title in data.read():
                print("this Title is used before!")
                data.close()
            else:
                break
    while True:
        details = input("Details: ")
        if not len(details) > 50:
            print("The description must be more than 50 Char!")
        else:
            break
        cat=["Art","Fashion","Food","Film&Video","Photography","Technology","Education","Medical"]
        print("Choose one of theese Categories:")
        print(" Art | Fashion | Food | Film&Video | Photography | Technology | Education | Medical")
        category = input("Category: ")
        if not len(category) > 0:
            print("Choose the category")
        else:
            if category in cat:
                break
    while True:
        target = input("Total target(EGP): ")
        if not len(target) > 0:
            print("Enter the target")
        else:
            try:
                v=int(target)
                break
            except ValueError:
                print("The target must be number!")

    while True:
        start = input("From: ")
        if not len(start) > 0:
            print("Enter the date")
        else:
            if not checkdate(start):
                print("Enter the correct format(d/m/y)!")
            else:
                break
    while True:
        end = input("To: ")
        if not len(end) > 0:
            print("Enter the date")
        else:
            if not checkdate(end):
                print("Enter the correct format(d/m/y)!")
            else:
                break
                
    print("Creating...")
    project=["ID: "+str(Id),"Title: " + title,
             "Details: " + details,
             "Category: " + category,
             "From "+start+" To "+end,
             "Total target: "+target+" EGP"]
    user_projects="User: "+username+" | "+"Project: "+str(project)
    data=open("DataBase/projects_table.txt","w") #You must manually create a DataBase Folder 
    data=open("DataBase/projects_table.txt","a")
    data.write("-----------------------------------------------------------------------------------------------------------------------------------------")
    data.write("\n"+str(user_projects)+"\n")
    data.close()
    time.sleep(1)
    print("Project has been created")

 
# User Account
def profile(username):
    Id=0
    print("Welcome to your account, "+username)
    print("Options: (P)profile | (S)start project | (F)fund | (D)delete | (L)logout ")
    while True:
        option = input(username+" > ")
        if option == "P":
            print("________Profile_______")
            user=[]
            with open("DataBase/users_table.txt","r") as db:
                print("Your Info......\n")
                for line in db.readlines():
                    if username in line:
                        user.append("Name:"+line.split(",")[0].split("{")[1].split(":")[1])
                        user.append("E-mail:"+line.split(",")[1].split(":")[1])
                        user.append("Phone:"+line.split(",")[3].split(":")[1].split("}")[0])
            for u in user:
                print(" "+u)
                
            with open("DataBase/projects_table.txt","r") as d:
                print("_____________________")
                print("Your Projects......\n")
                money=0
                pro=open("DataBase/projects_table.txt","r")
                for line in pro.readlines():
                    if username in line.split("|")[0]:
                        print(line.split("|")[1])
                        with open("DataBase/donations_table.txt","r") as ddb:
                                for dline in ddb.readlines():
                                    if "----" not in dline:
                                        if line.split("|")[1].split(",")[1].split("'")[1] in dline :
                                            print(dline.split("|")[1])
                                            money+=int(dline.split("|")[1].split(":")[1].split(" ")[1])
                        print(" Total: "+str(money)+" EGP")
                        money=0
                        print("--------------------------------------------------------------------------")
           
            with open("DataBase/donations_table.txt","r") as db:
                print("_____________________")           
                print("Your Donations......\n")
                for line in db.readlines():
                    if "----" not in line:
                        if username in line.split("|")[0] :
                            print("Donated_Project:"+line.split("|")[2].split("\n")[0])
                            print(line.split("|")[1])
                            print("--------------------------------------------------------------------------")
                          
        elif option == "S":
            Id=1
            pro=open("DataBase/projects_table.txt","r")
            for line in pro.readlines():
                if username in line:
                    if str(Id) in line:
                        Id+=1
            create_project(username,Id)
                        
        elif option == "L":
            print("Logging out...")
            break
        
        elif option == "D":
            print("(1)project | (2)account")
            opt=input("Delete > ")
            if opt=="1":
                while True:
                    num=input("Enter the ID of project: ")
                    if not len(num) > 0:
                         print("Enter the Id")
                    else:
                        with open("DataBase/projects_table.txt","r") as pro:
                            for line in pro.readlines():
                                if "-------" not in line:
                                    if num in line.split("|")[1].split(",")[0].split(":")[2].split("'")[0].split(" ")[1]:
                                        delete_project(line)
                                        print("Deleting project number"+num+"......")
                                        time.sleep(1)
                                        print("The project has been deleted")
                        break
                               
            elif opt=="2":
                while True:
                    ans=input("Are you sure? (y|n): ")
                    if(ans=="y"):
                        pas=input("Enter your password: ")
                        if passauth(pas):
                            data=open("DataBase/users_table.txt","r")
                            for line in data.readlines():
                                if pas in line:
                                    if username in line:
                                        delete_account(pas)
                                        pro=open("DataBase/projects_table.txt","r")
                                        for line in pro.readlines():
                                            if username in line:
                                                delete_project(line)
                                                print("Deleting Account......")
                                                time.sleep(1)
                                                print("The Account has been deleted\n")
                                                login()    
                            break
                        else:
                            print("\t\t Wrong Password!")
                            profile(username)
                    elif(ans=="n"):
                        break
            else:
                print(option + " is not an option")
        
        elif option == "F":
            print("Options: (1)search| (2)show_all")
            opt = input("Found > ")
            if opt=="1":
                search=input("By_Date: ")
                print("\t\t Search_Result")
                print()
                with open("DataBase/projects_table.txt","r") as pt:
                    for line in pt.readlines():
                        if search in line:
                            print(line)
                            donated=[line.split("|")[1].split(",")[1].split("'")[1],line.split("|")[1].split(",")[4].split("'")[1],line.split("|")[1].split(",")[5].split("]\n")[0].split("'")[1]]
                            donation(username,str(donated))
            elif opt=="2":
                with open("DataBase/projects_table.txt","r") as pt:
                    for line in pt.readlines():
                        if "----" not in line:
                            print(line)
                            donated=[line.split("|")[1].split(",")[1].split("'")[1],line.split("|")[1].split(",")[4].split("'")[1],line.split("|")[1].split(",")[5].split("]\n")[0].split("'")[1]]
                            donation(username,str(donated))
            else:
                print(opt + " is not an option")
            
        else:
            print(option + " is not an option")


print("\n\t\t\t",end="")
print("|__Crowd Fnding__|")
print("Welcome to our website.")
print("Please (1)Register OR (2)Login ")
while True:
    option = input("> ")
    if option == "1":
        register()
        
    elif option == "2":
        login()
    else:
        print(option + " is not an option")

        
