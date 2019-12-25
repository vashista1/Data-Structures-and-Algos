def printCountRec(dist): 
      
    if dist < 0: 
        return 0
          
    if dist == 0: 
        return 1
  
    return (printCountRec(dist-1) +
            printCountRec(dist-2) +
            printCountRec(dist-3)) 
  
dist = 4
print(printCountRec(dist)) 