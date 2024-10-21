integers_list=list(map(int,input("enter integers seperated by space:").split()))
odd_numbers=[]
for number in integers_list :
    if number  %2!=0 :
        odd_numbers.append(number)
print("list of odd integers",odd_numbers)    
