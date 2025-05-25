for i in range(5, 0, -1):
    for j in range(1,i+1):
        print(j, end='')
    print()  
    
    
##another way
for i in range(5, 0, -1):
    print(''.join(str(j) for j in range(1, i + 1)))
      