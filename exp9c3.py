num=int(input("enter a number:"))
original_num=num
num_digits=len(str(num))
sum_of_powers=0
while num>0:
    digit=num%10
    sum_of_powers+=digit**num_digits
    num=num//10
if sum_of_powers==original_num:
    print(f"{original_num} is an armstrong number")
else:
    print(f"{original_num} is not an armstrong number")
