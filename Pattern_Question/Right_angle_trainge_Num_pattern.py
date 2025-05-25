for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()    
    
    
    #another way to print the same pattern
    
for i in range(1,6):
    print(' '.join(str(x) for x in range(1, i + 1)))  