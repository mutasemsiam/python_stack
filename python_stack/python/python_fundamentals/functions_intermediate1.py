import random
def randInt(min= 0  , max= 100  ):
    num = random.random() * max + min
    if min>max and max<0:
        return "min can't be greater than max and max can't be negative"
    if min>max:
        return "min can't be less than max"
    elif max<0:
        return "max can't be less than 0"
    elif num<max:
        return int(num)
    else:
        num -=min
        return int(num)

print(randInt()) 		# should print a random integer between 0 to 100
print(randInt(max=50)) 	# should print a random integer between 0 to 50
print(randInt(min=50)) 	   # should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

