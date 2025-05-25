# def pyramid_pattern(n):
#     """
#     Function to print a pyramid pattern of stars.
    
#     :param n: Number of rows in the pyramid
#     """
#     for i in range(n):
#         # Print leading spaces
#         print(' ' * (n - i - 1), end='')
#         # Print stars
#         print('* ' * (i + 1))
# pyramid_pattern(5)        




for i in range(1,6):
    print(''*(5-i)+'* '*(2*i-1))