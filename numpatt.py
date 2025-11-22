for i in range(10):
    s=5
    if i==0:
        for j in range(1,6):
            print(j,end=" ")
    if i!=0:
        if i%2!=0:
            print(j+s,end=' ')
            for k in range(4):
                s-=1
                print(j+s,end=' ')
               
                
            j=j+s
            
        if i%2==0:
            print(j+s,end=' ')
            for l in range(4):
                s+=1
                print(j+s,end=' ')
                
            
            j=j+s  
              
                
    
    print("\n")
    