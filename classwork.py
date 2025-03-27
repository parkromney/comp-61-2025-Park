# list=[]

# def menuoption():
#     print("Menu:")
#     print("1. Add item to the end of the list")
#     print("2. Remove item from the end of the list")

# input=1
# while(input == 1 or input == 2):
#     menuoption()
#     input=input("Input your choice here: ")
#     if(input==1):
#         inputnum=input("What would you like to add to the end of the list?")
#         list.append(inputnum)
#         (f'Now you have {list}')
#     elif(input==2):
#         list.pop()
#         (f'Now you have{list}')


# class MenuProgram:
#     def __init__(self):
#         self.list = []
#         self.input = 1
#     def showmenu(self):
#         print("Menu:")
#         print("1. Add item to the end of the list")
#         print("2. Remove item from the end of the list")
#         self.input=int(input("Input your choice here: "))
#     def displayoutput(self):
#         (f'Now you have{self.list}')
#     def run(self):
#         while(self.input == 1 or self.input == 2):
#             self.showmenu()
#             if(self.input==1):
#                 inputnum=input("What would you like to add to the end of the list?")
#                 self.list.append(inputnum)
#                 self.displayoutput()
#             if(self.input==2):
#                 self.list.pop()
#                 self.displayoutput()

# menu_program = MenuProgram
# menu_program.run()

# from time import sleep

# counter = 10

# def count_down(count):
#     global counter
#     sleep(0.3)
#     if count == 0:
#         counter = count
#         print("Done Counting Down!")
#     else:
#         print(count)
#         count_down(count-1)

# def count_up(count):
#     sleep(0.3)
#     if count == 11:
#         print("Done Counting Up!")
#         print("Finished!")
#     else:
#         print(count)
#         count_up(count+1)
     
     
    
# count_down(counter)
# count_up(counter)



from time import sleep


def count(coun,cou):
    sleep(0.3)
    if coun == 0:
        cou = False
        count(coun-1)
        print(coun)
    else:
        cou ==10
        coun = False
        count(cou+1)
        print(cou)
        print("Finished")
count(10,True)

