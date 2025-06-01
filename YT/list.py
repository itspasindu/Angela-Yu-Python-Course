x = ["Kanampella","Nilamelage","Pasindu"]

y = [10,256,85,789,458,552,205,225]
z = [458,485,9658,7458,6589,5227,45,522,45]

a = y+z

'''
enter = input("do you need add middle name: ")


x = ["Pasindu", "Kavindu", "Supun"]  # Example list for context

if enter == "yes":
    x.insert(3, "Dewviman")  # Inserts "Dewviman" at index 3
elif enter == "2":
    x.append("Pushpakumara")  # Appends "Pushpakumara" to the end of the list
elif enter == "3":
    x.remove("Pasindu")  # Removes the first occurrence of "Pasindu"
else:
    x.pop(1)  # Removes the element at index 
    
print(x)
'''

available = 458 in a # Find available values with boolean
not_available = 458 not in a # Find not available values with boolean

print(available)
print(not_available)