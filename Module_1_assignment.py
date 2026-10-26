Name=input("Enter Your name")
print("Name:",Name)

Monthly_Expenses=int(input("Enter your Monthly Expensee"))
print("Monthly_Expenses:",Monthly_Expenses)

Rent=int(input("Enter Your Rent"))
print("Rent:",Rent)

Food_Expenses=int(input("Enter your Food Expenses"))
print("Food_Expenses:",Food_Expenses)

Travel_Expenses=int(input("Enter your Travel Expenses"))
print("Travel_Expenses:",Travel_Expenses)

Entertainment_Expenses=int(input("Enter your Entertainment Expenses"))
print("Entertainment_Expenses:",Entertainment_Expenses)

Other_Expenses=int(input("Enter your other expenses"))
print("Other_Expenses:",Other_Expenses)

Total_Expenses=Monthly_Expenses+Rent+Food_Expenses+Travel_Expenses+Entertainment_Expenses+Other_Expenses
print("Total_Expenses:",Total_Expenses)

Remaining_Balance=int(input("Enter your Monthly Expensee"))-Total_Expenses
print("Remaining_Balance:",Remaining_Balance)

Saving_Percentages=(Remaining_Balance/Monthly_Expenses)*100
print("Saving_percentage:",Saving_Percentages,"%")

