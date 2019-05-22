
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    value = 0
    try:
        if num == "done" : 
            break
        value = int(num)
            
        if (smallest == None):
            smallest = value
        elif (largest == None):
            largest = value
        elif (value < smallest):
            smallest = value
        elif (value > largest):
            largest = value
        
        
    except:
        print ("Invalid input")
        continue
        
    
  
    
    
    	
    
    
print ("Maximum is " + largest)
print ("Minimum is " + smallest)

