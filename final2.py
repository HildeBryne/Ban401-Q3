numbers = [0,4,8,1,3,10,11,2,5,8,8,12,13,23,24,25,26,27,28,29,30]

list1 = [] #Creating a new list
for i in numbers:
    list1 = [x for x in list1 if i > x] + [i] + [x for x in list1 if i <= x]
print(list1) #Remember to delete this line

list2 = []
for i in list1:
    if i not in list2:
        list2.append(i) #Remmoving duplicates
print(list2) #Remember to delete this line

list3 = list() #Creating a new empty list
list4 = list() #Creating a new empty list
list3.append(list4) #Adding list4 into end of list 3


i = 0 #Starting from value equal to 0

while i < len(list2): #Whithin the length of list2

    if i > 0: #If i is greater than 0
        if list2[i - 1] == list2[i] or list2[i - 1] + 1 == list2[i]: #Checking for increasing values in list2
            list4.append(list2[i]) #Adding values to list4

        else: #If the increasing value is not found in list2
            list4 = list() #Nested list4
            list4.append(list2[i]) #Adding values from list2 into list4
            list3.append(list4) #Adding list4 within list3

    else: #If i is equal or less than 0
        list4.append(list2[i]) #Adding this value into list4

    i = i + 1 #Move to next index in list2

print("This is list3:",list3)

for new_list in list3: #For every value in list3
    longest_list = list3[0] #Giving the first index in list3 name longest_list
    if len(longest_list) < len(new_list): #if the length of list in first index is lower than the next list
        longest_list = new_list #Giving longest_list a new value
        print("longest list1", longest_list) #Printing the longest list

    if len(longest_list) > len(new_list): #If first in first index is higher than next list
        print("longest list2", longest_list) #Prinstin the longest list
        



