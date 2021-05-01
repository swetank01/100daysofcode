# List

states = ["Rajasthan", "Uttrakhand", "Goa", "Maharastra"]
print(states[0])


list = ["python", "Shell", "LxC", "kubernetes", "GCP", "Hashicorp"]

# append(x)  : add item to the end
append_list = list.append("SoC")
print(list)

# extend(iterable)  : 
extend_list = list.extend(["AWS","Azure"])
print(list)

# insert(i, x)
insert_list = list.insert(3, "docker-microservice")
print(list)

# remove(x)
remove_list = list.remove("LxC")
print(list)

# pop([i])
pop_list = list.pop(0)
print(list)
