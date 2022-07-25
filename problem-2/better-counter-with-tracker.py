
loop= True
cont = 0

while loop == True:
    msg = input("Input \"i\" for \"increase\", \"d\" for \"decrease\" and \"q\" for \"quit\": ")
    if msg=="q":
        break
    elif msg=='i':
        cont=cont+1
        print("Counter : ", cont)
    elif msg == "d":
        cont=cont-1
        print("Counter : ", cont)
    else:
        print("enter proper value")