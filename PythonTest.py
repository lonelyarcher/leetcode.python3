import datetime
x = 3 and 1 # and first judge if the first argument is None, '' or 0, if yes then return it, if not return the second argument
print("{}".format("3.1"))
print("{:s}".format("abc"))
print("{:f}".format(3.14))
print("{:%m/%d/%Y %H:%M}".format(datetime.datetime(2018,4,11,9,53)))
print("{}/{}/{} {}:{}".format(2018,4,11,9,53))

a = [[0, 1], [1, 3]]
b = [[2, 4]]
a += b
print(a) # list add list = new combined list


dict = {None: 2}
# print(dict.setdefault(None, None.left)) # fail, because setdefault always execute the default first

def f1(x):
    if x:
        print("f1: " + str(x))
        f2(x+1)

x = 2

def f2(x):
    print("f2: " + str(x))

f1(5) # works because python define functions regardless of the order

for i in range(5):
    xx = i
print(xx) # variable can live outside of loop

print(5/2) # divide / in python3 return float, while // return int