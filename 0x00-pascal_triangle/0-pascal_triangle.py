#!/usr/bin/python3
"""0-pascal_triangle
"""


def pascal_triangle(n):
    """_summary_

    Args:
        n (integer): number of rows

    Returns:
        list: paslcal triangle
    """
    if n <= 0:
        return []
    out = [[1]]
    for i in range(n - 1):
        temp = [0] + out[-1] + [0]
        row = []
        for j in range(len(out[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        out.append(row)
    return out
