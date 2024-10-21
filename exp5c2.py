name=input("enter first names seperated by commas:").split()
count_a=sum(name.lower().count('a')for name in name)
print(f"the letter 'a'occurs{count_a}times in the list of names")
