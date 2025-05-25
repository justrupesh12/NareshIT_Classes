#print right angle star pattern
for i in range(1,6):
    print('* ' * i)
    
    
    
    
def right_angle_star_pattern(n):
    """
    Function to print a right angle star pattern.
    
    Parameters:
    n (int): The number of rows in the pattern.
    
    Returns:
    None
    """
    for i in range(1, n + 1):
        print('* ' * i)

right_angle_star_pattern(5)            
    