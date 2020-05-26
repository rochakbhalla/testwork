# name= 'rochak'
# val =10

# print("Thsi si the place {} if rhehe {}".format('rochak',12))

import re

only_num = re.compile("[^A-z]+")
flag = re.search(only_num, "rocj23s")
print(flag)