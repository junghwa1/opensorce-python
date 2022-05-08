i=0
for i in range(2,101):
    cont=0
    for k in range(2,i+1):
        if i%k==0:
            cont+=1
    if cont==1:
        print("%d"%i,end=" ")
            
            
    
