import re
"""Function for indentificated if word is isogram
    """
def is_isogram(string):
    """Identificated if the word is a isogram

    Args:
        string (string): A word or phrase

    Return:
        Boolean
    """
    for letter in re.sub('[^A-Za-z0-9]+', '', string):
        if string.lower().count(letter.lower()) > 1:
            return False
    return True

print(is_isogram(""))
#"thumbscrew-jappingly"
