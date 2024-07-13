a = ["abdul kader","osama","kabir","nabil"]
newlis = [x.upper() for x in a ]
print(newlis)
newlist2 = ['hello' for x in a]
print(newlist2)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist3 = [x if x != "cherry" else "orange" for x in fruits]
print(newlist3)
# newlist = [x for x in range(1,11)]
# print(newlist)
# newlist = [x for x in a] 
# print(newlist)

# newlist = [x for x in a if "b" in x]
# print(newlist)
# newlist = []
# for x in a:
#     if "b" in x:
#        newlist.append(x)
# print(newlist)