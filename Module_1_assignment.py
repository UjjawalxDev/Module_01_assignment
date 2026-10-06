Name = input("Enter your name: ")
print("Name: ", Name)

Monthly_Expenses = int(input("Enter your Monthly expenses: "))
print("Monthly Expenses: ", Monthly_Expenses)

Rent = int(input("Enter your Rent: "))
print("Rent: ", Rent)

Food_Expenses = int(input("Enter your Food expenses: "))
print("Food Expenses: ", Food_Expenses)

Travel_Expenses = int(input("Enter your Travel expenses: "))
print("Travel Expenses: ", Travel_Expenses)

Entertainment_Expenses = int(input("Enter your Entertainment Expenses: "))
print("Entertainment Expenses: ", Entertainment_Expenses)

Other_Expenses = int(input("Enter your Other expenses: "))
print("Other Expenses: ", Other_Expenses)


Total_Expenses = Monthly_Expenses + Rent + Food_Expenses + Travel_Expenses + Entertainment_Expenses + Other_Expenses
print("Total Expenses: ", Total_Expenses)

Remaining_Balance = int(input("Enter your Monthly income: ")) - Total_Expenses
print("Remaining Balance: ", Remaining_Balance) 

Saving_Percentages = (Remaining_Balance / Monthly_Expenses) * 100
print("Saving Percentages: ", Saving_Percentages, "%")
