a=int(input("enter valur of a to calculate its factorial: "))

fact = 1
for i in range(1,a+1):
   fact = fact * i

print(f"factorial of {a} is : {fact}")
