def compound_interest(principle, rate, time): 
  
    # Calculates compound interest  
    CI = principle * (pow((1 + rate / 100), time)) 
    print("Compound interest is", CI) 
  
# Driver Code  
compound_interest(10000, 10.25, 5) 
  