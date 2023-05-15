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

def value(colors):
    """Fuction calculated the resistance value of resistor

    Args:
        colors (list): List of first and second colors that appearance on resistor

    Returns:
        integer: Value of first color concatenate of value second color
    """
    return int(str(value_colors[colors[0]]) + str(value_colors[colors[1]]))

print(value(["blue", "grey"]))