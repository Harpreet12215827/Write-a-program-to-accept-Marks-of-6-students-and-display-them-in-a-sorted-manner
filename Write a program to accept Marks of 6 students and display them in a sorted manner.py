#Write a program to accept Marks of 6 students and display them in a sorted manner...

a = int(input("Marks of 1st student out of 70:  "))
b = int(input("Marks of 2nd student out of 70:  "))
c = int(input("Marks of 3rd student out of 70:  "))
d = int(input("Marks of 4th student out of 70:  "))
e = int(input("Marks of 5th student out of 70:  "))
f = int(input("Marks of 6th student out of 70:  "))
M = [a,b,c,d,e,f]
M.sort()
print(M)