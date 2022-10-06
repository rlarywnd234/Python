from calendar import month_name
from pickle import FALSE
from telnetlib import SE


print("General Well-being Log\n======================")
Set_Value = False
while Set_Value == False:
    year, month = map(int, input("Set the year and month for the well-being log (YYYY MM): ").split())

    if (month > 12 or month < 1) and year > (2021 or year < 2018):
        print("     Year and Month'value, both value setted wrong ")
        print("     ERROR: The year must be between 2018 and 2021 inclusive")
        print("     ERROR: Jan.(1) - Dec.(12)")  
        continue

    elif year > 2021 or year < 2018:
        print("     ERROR: The year must be between 2018 and 2021 inclusive")
        continue

    elif month > 12 or month < 1:
        print("     ERROR: Jan.(1) - Dec.(12)")
        continue # continue 처리로 바로 다음 반복으로 돌아가 처음에 존재하는 input문으로 복귀
    
    Set_Value = True
    print("\n\n*** Log date set! ***\n\n")

Month_Intial = {1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 7:"Jul", 8:"Aug", 9:"Sep",10:"Oct", 11:"Nov", 12:"Dec"}
Day = 1

moring_rating = 0
Total_Morning = 0

evening_rating = 0
Total_Evening = 0

for Day in range(1,4):
    print("{0}-{1}-0{2}".format(year, Month_Intial[month],Day))
    
    Set_Value = False
    while Set_Value == False:
        moring_rating = float(input("Morning rating (0.0-5.0): "))
        if 5.0 < moring_rating or moring_rating < 0.0:
            print("     ERROR: Rating must be between 0.0 and 5.0 inclusive!")
            continue
        Set_Value = True

    Total_Morning = Total_Morning + moring_rating

    Set_Value = False
    while Set_Value == False:
        evening_rating = float(input("Evening rating (0.0-5.0):  "))
        if 5.0 < evening_rating or evening_rating < 0.0:
            print("     ERROR: Rating must be between 0.0 and 5.0 inclusive!")
            continue
        Set_Value = True
    Total_Evening = Total_Evening + evening_rating
    


print("Summary\n=======\n")
print("Morning total rating: {0:.2f}\nEvening total rating: {1:.2f}\n---------------------------\nOverall total rating: {2:.2f}".format(Total_Morning,Total_Evening,Total_Morning+Total_Evening))