from tokenize import Double


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
        print("Item-{0} Details:".format(list_num+1))

        itemcost = float(input("Item cost: $"))
        itemimportant = int(input("How important is it to you? [1=must have, 2=important, 3=want]: "))
        
        if itemimportant < 1 or itemimportant > 3:
            print("     ERROR: Value must be between 1 and 3")
            continue
            
        else:
            wishlist_list.append([]) # 2차원 리스트 동적 할당, 인덱스 추가
            wishlist_list[list_num].append(itemcost)
            wishlist_list[list_num].append(itemimportant) # 2차원 리스트에 요소 추가
            # while 탈출용 및 값 변경용

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


#Variables
income = 0
wishlist = 0

print("+--------------------------+\n+ Wish List Forecaster |\n+--------------------------+")

income = User_Income()      # 사용자 총수입 입력 함수
wishlist = User_Wishlist()  # 사용자 위시리스트 개수 입력 함수

print(Item_Details(wishlist))



