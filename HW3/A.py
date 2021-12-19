size = input()
print('size ="' + size + '"')
add_peperoni = input()
print('add_peperoni = "' + add_peperoni + '"')
extra_cheese = input()
print('extra_cheese ="' + extra_cheese + '"')
total = 0
if(size == "L"):
    total+=25
elif(size == "M"):
    total+=20
elif(size == "S"):
    total+=15
if((size =="L" or size =="M") and (add_peperoni == "Y")):
    total+=3
elif(size =="S" and add_peperoni=="Y"):
    total+=2
if(extra_cheese =="Y"):
    total+=1
print(total)