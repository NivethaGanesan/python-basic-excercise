for val in range(1,100): 
      
   # If num is divisible by any number   
   # between 2 and val, it is not prime  
   if val > 0: 
       for n in range(2,val): 
           if (val % n) == 0: 
               break
       else: 
           print(val) 