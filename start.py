item =" ice cream "
price = 30
rating = 4.5
is_veg=True
menu=["Dosa" , "idly" , "Samosa"]
print(type(item))
print(type(price))
print(type(rating))
print(type(is_veg))
print(type(menu))
print(menu[0])
print(menu[1])
print(menu[2])
menu.append("Vada")
print(menu)
print(item)
print(price)
print(item, "cost =",price)
menu[1] = "Puri"
menu[2] = "Egg puff"
print(menu)
menu.remove("Dosa")
print(menu)
working_days = ("Monday", "Tuesday" , "Wednesday" , "Thrusday" , "Friday")
print(working_days[2])
prices = {
    "Dosa":40,
    "Idli":30,
    "Samosa":15
}
print(prices["Dosa"])
print(prices["Samosa"])
prices["Vada"]=25
prices.pop("Samosa")
print(prices)