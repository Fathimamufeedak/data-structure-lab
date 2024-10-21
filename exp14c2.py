input_string=input("enter a string:")
if input_string[-3:]=='ing':
    result=input_string+'ly'
else:
    result=input_string+'ing'
print(result)

