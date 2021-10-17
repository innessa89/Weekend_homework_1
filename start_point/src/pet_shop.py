def get_pet_shop_name(shop):
   return shop["name"]

def get_total_cash(cash):
   return cash["admin"]["total_cash"]

def add_or_remove_cash(shop, cash):
    shop["admin"]["total_cash"]+=cash
    
def get_pets_sold(pets):
    return pets["admin"]["pets_sold"]

def increase_pets_sold(shop, pets):
    shop["admin"]["pets_sold"]+=pets

def get_stock_count(stock):   
    return len(stock["pets"])


def get_pets_by_breed(shop, breed):
    cats_list=[]
    for cat in shop["pets"]:
        if cat["breed"] == breed:
            cats_list.append(cat)
    return cats_list   

def find_pet_by_name(shop,name):
    for pet in shop["pets"]:
        if pet["name"]==name:       
           return pet        

def remove_pet_by_name(shop,name):
   for pet in shop["pets"]:
        if pet["name"]==name:   
            shop["pets"].remove(pet)
            return

def add_pet_to_stock(shop,new_pet):
   shop["pets"].append(new_pet)
   return shop    
     
def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"]-=cash

def get_customer_pet_count(customer):
    return len(customer["pets"])   
    
def add_pet_to_customer(customer,pet):
    customer['pets'].append(pet)       
             
def customer_can_afford_pet(customer, pet):
    if customer["cash"]>=pet["price"]:
        return True
    else:
        return False    

def sell_pet_to_customer(shop, pet, customer):   
    if pet!= None and shop!=None and customer!=None and customer["cash"]>=pet["price"]:
        customer["cash"]-=pet["price"]
        shop["admin"]["total_cash"]+=pet["price"]
        customer["pets"].append(pet)
        shop["admin"]["pets_sold"]+=1
        
     





