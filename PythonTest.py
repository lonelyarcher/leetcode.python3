import datetime
x = 3 and 1
print("{}".format("3.1"))
print("{:s}".format("abc"))
print("{:f}".format(3.14))
print("{:%m/%d/%Y %H:%M}".format(datetime.datetime(2018,4,11,9,53)))
print("{}/{}/{} {}:{}".format(2018,4,11,9,53))

a = [[0, 1], [1, 3]]
b = [[2, 4]]
a += b
print(a)


dict = {None: 2}
print(dict.setdefault(None, None.left))