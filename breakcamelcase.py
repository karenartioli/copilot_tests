def break_camel_case(string):
    """
    Breaks up camel casing by inserting a space between words.

    Parameters:
    string (str): The input string in camel case format.

    Returns:
    str: The input string with spaces inserted between words.

    Examples:
    >>> break_camel_case("helloWorld")
    'hello World'

    >>> break_camel_case("helloWorldPython")
    'hello World Python'
    """
    words = []
    current_word = ""

    for char in string:
        if char.isupper():
            if current_word:
                words.append(current_word)
            current_word = char
        else:
            current_word += char

    if current_word:
        words.append(current_word)

    return " ".join(words)

