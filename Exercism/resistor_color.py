""" Calculate a resistance values of resistors
"""
value_colors = {'black': 0, 
                'brown': 1, 
                'red': 2, 
                'orange': 3, 
                'yellow': 4, 
                'green': 5, 
                'blue': 6, 
                'violet': 7, 
                'grey': 8, 
                'white': 9}


def color_code(color):
    """Function to return numeric value for colors on resistors

    Args:
        color (string): Color on resistor

    Returns:
        Integer: Integer value to color on resistor
    """

    return value_colors[color]

def colors():
    """Function return list of numeric values of colors on resistors

    Returns:
        List: Numeric values
    """

    return list(value_colors.keys())

#print(color_code('Orange'))

print(colors())