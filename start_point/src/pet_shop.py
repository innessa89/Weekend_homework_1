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


