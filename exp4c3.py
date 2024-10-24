def even_digit_perfect_squares(start,end):
    even_digit_squares=[]
    for num in range(start,end+1):
        if len(str(num))== 4 and all(int(digit)%2==0 for digit in str(num)):
            root=int(num**0.5)
            if root*root==num:
                even_digit_squares.append(num)
    return even_digit_squares
print(even_digit_perfect_squares(1000,9999))
