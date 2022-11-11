def fib(n):
    if n == 1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return(fib(n-1) + fib(n-2))
inPut = int(input("For fibonacci numbers, Please Enter value of n? "))
if inPut < 1:
    print("Plese enter a valid number")
else:
    print("The Fibonacci numbers are:")
for i in range(1,inPut+1):
    print(fib(i))

