#1
def countdown(a):
    listNew = []
    for x in range(a,-1,-1):
        listNew.append(x)
    return listNew

z = countdown(5)
print(z)

#2
def print_and_return(list):
        print(list[0])
        return list[1]
z = print_and_return([2,9])
print(z)

#3
def first_plus_length(list):
    sum = list[0] + len(list)
    return sum

z = first_plus_length([1,2,3,4,5])
print(z)

#4
def values_greater_than_second(list):
    newlist = []
    counter = 0
    for x in list:
        if len(list)<2:
            return False
        elif x>list[1]:
            newlist.append(x)
            counter += 1
    print(counter)
    return newlist
z = values_greater_than_second([5,2,3,2,1,4])
print(z)

#5
def length_and_value(size, value):
    newlist = []
    for x in range(size):
        newlist.append(value)
    
    return newlist

z = length_and_value(6,2)
print(z)

