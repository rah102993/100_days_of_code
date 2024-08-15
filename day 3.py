print("Welcome to Heemah's Salads and smoothie Bar!")
order = input("What would you like to order? Smoothie, Juice, Fries, Salad ")
smoothie = 50
juice = 45
fries = 60
salad = 70
vat = 0

if order == "Smoothie":
    vat = 15
    print(f"Your Total Bill is {smoothie + vat} Ghana Cedis")
elif order == "Juice":
    vat = 15
    print(f"Your Total Bill is {juice + vat} Ghana Cedis")
elif order == "Fries":
    vat = 15
    print(f"Your Total Bill is {fries + vat} Ghana Cedis")
else:
    vat = 15
    print(f"Your Total Bill is {salad + vat} Ghana Cedis")