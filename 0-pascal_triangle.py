#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the given number of rows.
    
    Args:
        n (int): The number of rows in the Pascal's triangle.
        
    Returns:
        List[List[int]]: Pascal's triangle as a list of lists of integers.
        
    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []  # Return an empty list if n <= 0
    
    triangle = [[1]]  # Initialize the triangle with the first row [1]
    
    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])  # Calculate each element in the row
        
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)  # Add the row to the triangle
        
    return triangle


