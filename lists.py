myList = []
length = int(input("Enter number of elements : "))
for i in range(0, length):
    value = int(input())
    myList.append(value)
print("All positive numbers of the list : ")
for ele in myList:
	if ele >= 0:
	    print(ele, end = " ")