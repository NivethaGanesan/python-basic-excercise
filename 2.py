# Python 3 program to find  
# factorial of given number 
#
  
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
num = 9;
print("Factorial of",num,"is",
factorial(num)) 
#print(f"the factorail of {num} is factorail(num)")