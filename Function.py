#------------------------------------------Normal functions
def EvenNumber (num):
    if num == 0:
        print("this number is Zero")
    elif num % 2 ==0:
        print("this number is Even")
    else:
        print("this number is odd")

EvenNumber(8)

# -----------------------------------------lambda functions
g = lambda x: x * x * x
print(g(2))

#------------------------------lambda functions with filter
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)

#---------------------------------lambda functions with map
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2 , li))
print(final_list)

# ---------------------------------------------------------
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)
