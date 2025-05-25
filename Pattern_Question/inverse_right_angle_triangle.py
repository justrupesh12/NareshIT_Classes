def inverse_right_angle_triangle(n):
    """
    Function to print an inverted right angle triangle pattern.
    
    :param n: The number of rows in the triangle.
    """
    for i in range (n,0,-1):
        print('* ' * i)
    
inverse_right_angle_triangle(5)