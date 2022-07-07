class StudentHeight :
    
    def __init__ (self,name,height) :
        self.name=name
        self.height=height
        self.space=" "*(20-len(self.name))
    
    def __str__(self):
        return self.name+self.space+str(self.height)+"cms"
    
    def __lt__(self,other) :
        return self.height < other.height
    def __gt__(self,other):
        return self.height < other.height

condition=True
student_data=[]

while condition :
    
    print("\n enter 1 to add student \n enter 2 to display the student list \n enter 3 to exit")
    
    def inputfunc() :
        global input_value
        try :
            input_value = int(input("choose an option: "))
            assert 0 < input_value < 4 
        
        except :
            print("enter valid input")
            inputfunc()
        return input_value
    
    input_value = inputfunc()    
    
    if input_value == 1 :
        name = input("enter the name of the student: ")
        
        def heightfunc():
            global height
            try :    
                height = int(input("enter the height of the student in cms: "))
                assert height > 0 
            except :
                print("enter valid height")
                heightfunc()
            return height
        
    
            
        s1 = StudentHeight(name,heightfunc())
        student_data.append(s1)
        
    elif input_value == 2 :
        
        
        if len(student_data) >0:
            print("")
            print("name"+" "*15+"height")
            print("")
            for i in sorted(student_data,reverse=false) :
                print(i)
        else :
            print("no record found")
    elif input_value == 3 :
        print("exiting the code")
        condition = False
            
