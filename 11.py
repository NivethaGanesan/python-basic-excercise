def isFibonacci(n): 
  
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
    # is a perferct square 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
     
# A utility function to test above functions 
for i in range(1,11): 
     if (isFibonacci(i) == True): 
         print i,"is a Fibonacci Number"
     else: 
         print i,"is a not Fibonacci Number "
