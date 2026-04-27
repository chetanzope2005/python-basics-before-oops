data = [("Rahul", 80), ("Simran", 95), ("Amit", 75)]
# print (data)
print (type(data))
print (type(data[0]))

data.sort(key=lambda x: x[1], reverse=True)
print(data)

print (data[0][1])