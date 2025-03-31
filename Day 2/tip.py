print ("Welcome to TIP calculator")
bill = float(input("What was the total bill $: "))
tip = int(input("Enter your tip value $(5, 10, 15, 20): "))
people = int(input("How many peoples to split the bill: "))

bill_with_tip = tip + bill
bill_per_person = bill_with_tip / people

print(f"Bill value with tip {bill_with_tip}")
print(f"Bill value for 1 people {bill_per_person}")