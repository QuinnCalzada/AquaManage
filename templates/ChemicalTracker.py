#Kristen Vigna
#Aquamanage
#October 02, 2023
#Create an array that stores user inputed information

#set up for Columns: Chemical Name, Low Value, High Value, Current Value
col = 4
print(col)

#Rows give the number of chemicals being tracked
while True:
    try:
        rows = int(input('How many Chemicals would you like to add? '))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        #rows was successfully parsed!
        #we're ready to exit the loop.
        break
#print(rows)

#Create Array
Chemicals = [[0] * col for i in range(rows)]

for i in range(rows):
# loop will run for the length of the inner lists
    Chemicals[i][0] = input("What is the name of the chemical? ")
   
   #Test user input for proper values
    while True:
        try:
            Chemicals[i][1] = float(input("What is the lower limit for this chemical? "))
        except ValueError:
            print("Sorry, I didn't understand. Please try again.")
            continue
        else:
            #input was valid
            break

   #Test user input for proper values
    while True:
        try:
            Chemicals[i][2] = float(input("What is the upper limit for this chemical? "))
        except ValueError:
            print("Sorry, I didn't understand. Please try again.")
            continue
        else:
            #input was valid
            break

   #Test user input for proper values
    while True:
        try:
            Chemicals[i][3] = float(input("What is the current value for this chemical? "))
        except ValueError:
            print("Sorry, I didn't understand. Please try again.")
            continue
        else:
            #input was valid
            break
    i+1

print(Chemicals)

def ChemLevels(Chemicals):
    status = False
#create comparison for user input of chemicals and of given limits
    while True:
        if Chemicals[i][3]>Chemicals[i][1] or Chemicals[i][3]<Chemicals[i][2]:
            status = True
        else:
            break
    if i != len(Chemicals):
        i+1
    else:
        False
    return status



