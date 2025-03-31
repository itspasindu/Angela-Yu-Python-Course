import random

names = ["Sudhara", "Sindupa", "Chanuka"]
places = ["Peradeniya", "Katugasthota", "Poojapitiya"]

names_list = []

names_list.append(random.choice(names))

names_list.append(random.choice(places))

random.shuffle(names_list)

gangster_name = " ".join(names_list) 

print(gangster_name)