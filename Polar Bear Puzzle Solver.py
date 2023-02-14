dies = []

for i in range (6):
    cur = i + 1
    die = int(input("Enter the number for die "+str(cur)+": "))
    if die < 1 or die > 6:
        print ("The number on a die can only be from 1 to 6. Try Again.")
        exit ()
    dies.append (die)

#Level 1 - Polar Bears
temppolar = 0

#check for specific dies (3 and 5)
temppolar3 = dies.count(3)
temppolar += temppolar3 * 2

temppolar5 = dies.count(5)
temppolar += temppolar5 * 4


#Level 2 - Fish
tempfish = 0

#check for specific dies (1, 3, and 5)
tempfish1 = dies.count(1)
tempfish += tempfish1 * 6

tempfish3 = dies.count(3)
tempfish += tempfish3 * 4

tempfish5 = dies.count(5)
tempfish += tempfish5 * 2


#Level 3 - Plankton
tempplank = 0

#check for specific dies (2, 4, and 6)
tempplank2 = dies.count(2)
tempplank += tempplank2 * 2

tempplank4 = dies.count(4)
tempplank += tempplank4 * 4

tempplank6 = dies.count(6)
tempplank += tempplank6 * 6

tempplank = tempplank * 7

tempplank2b = dies.count(2)
tempplank += tempplank2b * 5

tempplank4b = dies.count(4)
tempplank += tempplank4b * 3

tempplank6b = dies.count(6)
tempplank += tempplank6b * 1

print()
print ("In "+str(dies)+", there are: ")
print()
print (str(temppolar)+" polarbears, "+str(tempfish)+" Fish, and "+str(tempplank)+" plankton.")