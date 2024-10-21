color_inp=input("enter color(comma_seperated):")
color_list=[color.split() for color in color_inp.split(',')]
if color_list:
    print("first color:",color_list[0])
    print("last color:",color_list[-1])
else:
    print("no colors were enterd")
