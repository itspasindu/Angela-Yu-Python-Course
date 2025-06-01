x = {"1000": "colombo", "2000": "moratuwa", "3000": "kandy", "4000": "galle"}
x["5000"] = "jaffna"
x[0] = 'zero'
x['cities'] = {"avissawella", "kottawa", "maharagama", "pannipitiya"}

print(x)
print(x.keys())
print(x.values())

y = x["cities"]
print(y)

del x[0]
del x["2000"]
x.clear()

print(x)