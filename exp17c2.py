my_dict={}
n=int(input("enter the number of items in the dictionary:"))
for i in range(n):
    key=input("enter key:")
    value =int(input("enter value:")) 
    my_dict[key]=value
print("sorted by key(asending):",dict(sorted(my_dict.items())))
print("sorted by keys(desendng):",dict(sorted(my_dict.items(),reverse=True)))
print("sorted by value(asending):",dict(sorted(my_dict.items(),key=lambda item:item[1])))
print("sorted by values (desendig):",dict(sorted(my_dict.items(),key=lambda item:item[1],reverse=True)))
