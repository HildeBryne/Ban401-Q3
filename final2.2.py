numbers = [0,4,8,1,3,10,14,11,2,8,12,8,12,13,14,18,19,23,21,22,24,25,27,20,26]

new_list = []
short_list = []

while numbers:
    min = numbers[0]
    for x in numbers:
        if x < min:
            min = x
    new_list.append(min)
    numbers.remove(min)

    if min not in short_list:
        short_list.append(min)

print(new_list)
print(short_list)

list3 = list() #Creating a new empty list
list4 = list() #Creating a new empty list
list3.append(list4) #Adding list4 into end of list 3


i = 0 #Starting from value equal to 0

while i < len(short_list): #Whithin the length of short_list

    if i > 0: #If i is greater than 0
        if short_list[i - 1] == short_list[i] or short_list[i - 1] + 1 == short_list[i]: #Checking for increasing values in list2
            list4.append(short_list[i]) #Adding values to list4

        else: #Adding the lowest value in nested list
            list4 = list() #Nested list4
            list4.append(short_list[i]) #Adding values from short_list into list4
            list3.append(list4) #Adding list4 within list3

    else: #If i is equal or less than 0
        list4.append(short_list[i]) #Adding this value into list4

    i = i + 1 #Move to next index in short_list

print("This is list3:",list3)

longest_list = list3[0]
for new_list in list3:
    new_list[0:]
    if len(longest_list) < len(new_list):
        longest_list = new_list

print("longest list", longest_list)

print("")
#syntax: reversed_list = os[start:stop:step]
reversed_list = list3[::-1] #Reversing list3
print(reversed_list)

new = reversed_list[0]
for extra in reversed_list:
    extra[0:]
    if len(new) < len(extra):
        new = extra

print("longest list1", new)