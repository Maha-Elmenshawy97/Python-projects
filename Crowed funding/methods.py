import re
import time

def check(mail):
    regex='^\w+([\.-]?\w+)*@\w+([\.-]?w+)*(\.\w{2,3})+$'
    if(re.search(regex,mail)):
        return True
    else:
        return False

def checkdate(date):
    regex='[\d]{1,2}/[\d]{1,2}/[\d]{4}'
    if(re.search(regex,date)):
        return True
    else:
        return False

def mailauth(email):
    with open("DataBase/users_table.txt","r") as data:
        for line in data:
            if email in line:
                return True
    return False

def passauth(password):
    with open("DataBase/users_table.txt","r") as data:
        for line in data:
            if password in line:
                return True
    return False



def donation(donar,project):
    print("Do you want to donate?(y|n)")
    while True:
        donate=input("Donate > ")
        if donate=="y":
            while True:
                amount=input("How much? ")
                if len(amount)==0:
                    print("Enter the amount!")
                else:
                    try:
                        v=int(amount)
                        break
                    except ValueError:
                        print("The amont must be number!")
             db=open("DataBase/donations_table.txt","w") #you must manually create a DataBase Folder
            db=open("DataBase/donations_table.txt","a")
            db.write("----------------------------------------------------------------------------")
            db.write("\nDonar_name: "+donar+" | Donation_amount: "+amount+" EGP |Project: "+project+"\n")
            db.close()
            time.sleep(1)
            print("The donation has been  saved.")
            break
        elif donate=="n":
            break



def delete_account(pas):
    with open("DataBase/users_table.txt","r+") as data:
        lines=data.readlines()
        data.seek(0)
        for line in lines:
            if pas not in line:
                data.write(line)
        data.truncate()
    

def delete_project(project):
    with open("DataBase/projects_table.txt","r+") as data:
        lines=data.readlines()
        data.seek(0)
        for line in lines:
            if project not in line:
                data.write(line)
        data.truncate()


