available_toppings = ["potato","onion","pineapple","pork","sausage","mushroom"]

pizza = []

anchor = True

while anchor:
    topping = input("please enter the toppings you want, enter quit to finish your order : ")
    if topping in available_toppings:
        print("ok we have added %s" %(topping))
        pizza.append(topping)
    elif topping == "quit":
        anchor = False
        print("done! here is your order :" + str(pizza))
    else:
        print(" your topping is not available. ")
        continue




