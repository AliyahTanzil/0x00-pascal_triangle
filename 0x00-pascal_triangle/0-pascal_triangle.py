#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""


def pascal_triangle(n):
     """
    Generates Pascal's triangle up to the given number of rows.
    
    Args:
        n (int): The number of rows in the Pascal's triangle.
        
    Returns:
        List[List[int]]: Pascal's triangle as a list of lists of integers.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # Start with the first row containing just 1
    
    for i in range(1, n):
        prev_row = triangle[i - 1]  # Retrieve the previous row
        current_row = [1]  # Initialize the current row with 1
        
        for j in range(1, i):
            # Calculate each element in the current row based on the previous row
            current_row.append(prev_row[j - 1] + prev_row[j])
            
        current_row.append(1)  # Add the last element to the current row
        triangle.append(current_row)  # Add the current row to the triangle
    
    return triangle

