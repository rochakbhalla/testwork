# import re

# inp = input("Enter the string : ")
# count = 0
# m = [(x.start(),x.end()) for x in re.finditer(r"(\w)\1{1, }", inp)]
# print(m)


# new_lst = []
# for i in range((len(inp)-1)):
#     if inp[i]==inp[i+1]:
#         new_lst.append(inp[i])
# print(new_lst)
# unq_lst = set(new_lst)
# print(unq_lst)
# old_lst = list(unq_lst)
# val = [new_lst.count(i) for i in unq_lst]
# val = list(val)
# print(val)
# for i in range(len(val)):
#     if val[i]%2 !=0:
#         print("{} - {}".format(old_lst[i], val[i]+1))
#     else:
#         print("{} - {}".format(old_lst[i], val[i]))
# print({i: "2" for i in set(new_lst)})
# suces, " ", su  es, su!!es, SUcceSS
# import os

# print(os.path.splitext(os.path.basename(__file__)))  #Output => ('test', '.py') 
# print(os.listfi())
#shutil module for copying and moving files
#os.path.splitdrive  -> This splits irrespective of windows or mac
#pyftpsyc #pypdf2



inpt_str = "HACK 3"
val = inpt_str.split(' ')
test_str = list(val[0])
obj_len = int(val[1])
final= []

for i in range(len(test_str)):
    for j in range(0, obj_len):
        if test_str[i] == test_str[j]:
            pass
        else:
            final.append(test_str[i]+test_str[j])
final = sorted(final)
print(final)


# inp = "1,0,3,2,0,2,6,0,2,10,5,7"
# index_lst=[]
# count = 0
# index_lst = inp.split(",")

# for item in index_lst:
#     if item == '0': 
#         index_lst.remove(item)
#         count = count+1
# for i in range(count):
#     index_lst.extend("0")

# print(index_lst)
