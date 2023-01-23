#x=lambda a:a+2
#print(x(5))
#x=lambda a,b:a+2
#print(x(6,5))
def multiply(n):
    return lambda a:a*n
num1=multiply(6)
num2=multiply(8)
print(num1(11))