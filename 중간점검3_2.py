
def User_Income ():
    income_check = False
    while income_check == False:
            income = float(input("\nEnter your monthly NET income: $"))

            if income < 500.00:
                print("ERROR: You must have a consistent monthly income of at least $500.00")
                continue

            elif 400000.00< income:
                print("ERROR: Liar! I'll believe you if you enter a value no more than $400000.00")
                continue

            else:
                income_check = True
    return income

def User_Wishlist ():
    wishlist_check = False
    while wishlist_check == False:
            howmany = int(input("\nHow many wish list items do you want to forecast?: "))

            if howmany < 1 or howmany > 10:
                print("ERROR: List is restricted to between 1 and 10 items.")
                continue
            
            else:
                wishlist_check = True
    return howmany

def Item_Details(wishlist):
    list_num = 0
    itemcost = 0
    checker = False
    wishlist_list = [] # 2차원 리스트 동적할당
    
    while list_num < wishlist:
        checker = False
        print("\nItem-{0} Details:".format(list_num+1))

        itemcost = float(input("Item cost: $"))
        while checker == False: 
                itemimportant = int(input("How important is it to you? [1=must have, 2=important, 3=want]: "))
                
                if itemimportant < 1 or itemimportant > 3:
                    print("     ERROR: Value must be between 1 and 3")
                    continue
                    
                else:
                    wishlist_list.append([]) # 2차원 리스트 동적 할당, 인덱스 추가
                    wishlist_list[list_num].append(itemcost)
                    wishlist_list[list_num].append(itemimportant)# 2차원 리스트에 요소 추가 
                    checker = True # while 탈출용 및 값 변경용
        
        checker = False

        while checker == False:
            YorN = str(input("Does this item have financing options? [y/n]: "))
            
            if YorN != "n" and YorN != "y" :
                print("     ERROR: Must be a lowercase 'y' or 'n'")
                continue
            
            else:
                wishlist_list[list_num].append(str(YorN))
                list_num = list_num + 1
                checker = True
    return wishlist_list


def menu(income,total):
    print("How do you want to forecast your wish list?\n 1. All items (no filter)\n 2. By priority\n 0. Quit/Exit")
    UserInput = input("Selection: ")
    total2 = 0
    global Item_list
    if UserInput == "1":
        print("\n====================================================")
        print("Filter:   All items\nAmount:   ${0}\nForecast: {1} years, {2} months\nNOTE: Financing options are available on some items.\n You can likely reduce the estimated months."
        .format(total, int((total//income)//12), int((total//income)%12)))
        print("====================================================\n")

    elif UserInput == "2":
        UserInput = input("\nWhat priority do you want to filter by? [1-3]: ")
        for x,y,z in Item_list:
            if UserInput in str(y):
                total2 = x + total2
        print("\n====================================================")
        print("Filter:   {0}\nAmount:   ${1}\nForecast: {2} years, {3} months\nNOTE: Financing options are available on some items.\n You can likely reduce the estimated months."
        .format(UserInput, total2,int(total2//income)//12, int(total2//income)%12))
        print("====================================================\n")
    elif UserInput == "0":
            quit()
    
    else:
        print("\nERROR: Invalid menu selection.\n")






#Variables
income = 0
wishlist = 0

print("+--------------------------+\n+ Wish List Forecaster |\n+--------------------------+")

income = User_Income()      # 사용자 총수입 입력 함수
wishlist = User_Wishlist()  # 사용자 위시리스트 개수 입력 함수

Item_list = Item_Details(wishlist)
num = 1
total = 0
print("\nItem Priority Financed        Cost \n---- -------- -------- -----------")
for x,y,z in Item_list:
    print(str(num).ljust(7),str(y).ljust(8), str(z).ljust(8), str(x)) # 2차원 리스트 요소 각개 출력법 
    num = num + 1
    total = x + total
print("---- -------- -------- -----------\n                       $ {0:.2f}".format(total))


while True:
    menu(income, total)