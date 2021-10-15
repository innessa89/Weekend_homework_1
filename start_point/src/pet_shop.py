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


       
             


    



