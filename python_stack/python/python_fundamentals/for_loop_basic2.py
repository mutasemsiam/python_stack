#1
def biggie_size(list):
    for x in range(len(list)):
        if list[x]>0:
            list[x] = "big"
    return list

z = biggie_size([-1, 3, 5, -5])
print(z)

#2
def count_positives(list):
    count = 0
    for x in list:
        if x>0:
            count+=1
    list[len(list)-1] = count
    return list

z = count_positives([1,6,-4,-2,-7,-2])
print(z)

#3
def sum_total(list):
    sum = 0
    for num in list:
        sum += num
    return sum

z = sum_total([6,3,-2])
print(z)

#4
def average(y):
    sum = 0
    for num in y:
        sum += num
    avg = sum/len(y)
    return avg

z = average([1,2,3,4]) 
print(z)

#5
def length(y):
    return len(y)

z = length([])
print(z)

#6
def minimum(list):
    if len(list) == 0:
        return False
    min = list[0]
    for x in list:
        if x < min:
            min = x
    return min
z = minimum([4,3,2,-5])
print(z)

#7
def maximum(list):
    if len(list) == 0:
        return False
    max = list[0]
    for x in list:
        if x > max:
            max = x
    return max
z = maximum([])
print(z)

#8
def ultimate_analysis(list):

    sum = 0
    min = list[0]
    max = list[0]
    length = len(list)

    for x in list:
        sum+=x
        if x<min:
            min = x
        if x>max:
            max = x
    avg = sum/length
    dict = {'sumTotal': sum, 'average': avg, 'minimum': min, 'maximum': max, 'length': length }
    return dict

z = ultimate_analysis([37,2,1,-9])
print(z)

#9
def reverse_list(list):
    n = len(list)
    for x in range(int(n/2)):
        holder = list[x]
        list[x] = list[n-x-1]
        list[n-x-1] = holder
    return list

z = reverse_list([37,2,1,-9])
print(z)


