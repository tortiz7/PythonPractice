# Reminder: Lists use [] , Tuples use ( ), and Dicts use { }
# We create a simple list below with 10 integers, and then we multiple each item in the list by 2 in the "BiggerList" variable below, then print that new list
NumberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
BiggerList = [x * 2 for x in NumberList]
print(BiggerList)