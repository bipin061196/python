a=int(input("enter value of which table you want : "))
b=int(input(f"enter value till which you table of {a}: "))

factor=1
for i in range(1,b+1):
    if factor is not b+1:
        print(f"{a} *   {factor}\t = {a * factor}")
        factor = factor + 1
    else:
        break
