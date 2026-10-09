# loop to print the i 4 times 
# for i in range(4):
 #   print(i)


#loop will start printng from 2 and ends at 5 
#for i in range(2,6):
 #   print(i)

#loop with range and increment 

#for i in range(2,10,2):
    #print(i)
     
#rpint the data from the list 
#orders = ["order1", "order2", "order3"]

#for order in orders:
#    print(order)

#for loop with if 
orders1 = [500,1500,800,2500]

for order in orders1:
    if order > 1000:
        print(order)
print("############################")
#Break statement 
for i in range(5):
    if i ==3:
        break
    print(i)  

print("######################")
#continue 
for i in range(5):
    if i==3:
        continue
    print(i)      
print("#########################")

#while loop

count = 1
while count<=5:
    print(count)
    count += 1 
print("##########################")

count1 = 1
while count1 <=5:
    if count1 ==3:
        break
    print(count1)
    count1 += 1 
print("###########################")

for i in range(3):
    pass

print("Done")

