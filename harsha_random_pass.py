import random

str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str3 = "!@#$%^&*()"
str4 = "0123456789"
complete_list=list(str1+str2+str3+str4)
x=True
def random_passowrd_generator():
    try :
        required_length_of_pass = int(input("enter the required length of password"))
        assert required_length_of_pass > 0
        randompassword=[]
        for i in range(required_length_of_pass) :
            randompassword.append(random.choice(complete_list))
        print("".join(randompassword))
    except:
        print("enter valid input")
        global x
        x= False
    
while x :
    random_passowrd_generator()
