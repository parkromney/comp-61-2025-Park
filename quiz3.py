list=[]

def menuoption():
    print("Menu:")
    print("1. Add item to the end of the list")
    print("2. Remove item from the end of the list")

menuoption()
input=input("Input your choice here: ")
while(input == 1 or input == 2):
    if(input==1):
        inputnum=input("What would you like to add to the end of the list?")
        list.append(inputnum)
        (f'Now you have {list}')
    elif(input==2):
        inputnum2=input("")
        list.remove(inputnum2)
        (f'Now you have{list}')
    else:
        print("Invalid option.")
        break