class RestaurantMenu :
    
    menu = [{"veg machuria":290,"panner 65":240,"chilly mushroom":320},{"chicken 65":320,"crispy prawns":350,"apollo fish":330},{"veg biryani":330,"kaju biryani":360},{"chicken biryani":360,"mutton biryani":390}]
  
    def add_items(self) :
        
        print("enter 1 to add starters_veg \n enter 2 to add starters_nonveg \n enter 3 to add biryani_veg \n enter 4 to add biryani_nonveg")
        
        def inputfunc2() :
            
            try : 
                self.input_value =int(input())
                assert 0 < self.input_value < 5 

            except :
                print("enter valid input")
                inputfunc2()
                
        inputfunc2()
            
        self.item_name = input("enter the name of item to be added :")
        
        
        def pricefunc() :
            try :
                self.item_price = int(input("enter the price of item  :"))
                assert self.item_price > 0 
            except :
                print("enter the valid amount")
                pricefunc()
            return self.item_price
        
        self.menu[self.input_value-1][self.item_name]=pricefunc()

        
    def remove_items(self) :
        self.item_name = input("enter the name of item to be removed :")
        self.condition1 = True
        for i in self.menu :
            if self.item_name in i.keys() :
                self.condition1 = False
                del i[self.item_name]
                break
    
        if self.condition1 :
            print("item not found in menu to remove")
            

    def modify_items(self):
    
        self.conditon2 =True
        self.item_name = input("enter the name of item to be modified :")
        
        def pricefunc() :
            try :
                self.item_price = int(input("enter the price of item  :"))
                assert self.item_price > 0 
            except :
                print("enter the valid amount")
                pricefunc()
            return self.item_price
        
        for i in self.menu :
            
            if self.item_name in i.keys() :
                self.conditon2 = False
                i[self.item_name]= pricefunc()
                break
            
        if self.conditon2 :
            print("item not found in menu to update price")
            
            
            
rest_obj = RestaurantMenu()
condition3=True

while condition3 :
    
    print("\n enter 1 to view menu card \n enter 2 to add items \n enter 3 to remove items \n enter 4 to update price of existing item \n enter 5 to exit ")
    
    def inputfunc() :
        try :
            input_value2 =int(input())
            assert 0 < input_value2 < 6 
        
        except :
            print("enter valid input")
            inputfunc()
        return input_value2
    
    input_value2=inputfunc()    
    
    if input_value2 == 1 :
        menu_list=["veg_starters:","nonveg_starters:","veg_biryani:","nonveg_biryani:"]
        for i in range(4) :
            print(menu_list[i])
            for key in rest_obj.menu[i] :
                print(key,"------  ₹",rest_obj.menu[i][key])
            
            
    elif input_value2 == 2 :
        rest_obj.add_items()
        
    elif input_value2 == 3 :
        rest_obj.remove_items()
        
    elif input_value2 == 4 :
        rest_obj.modify_items()
        
    elif input_value2 == 5 :
        condition3 = False
