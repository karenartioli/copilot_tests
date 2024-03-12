def test_break_camel_case():
    """
    Test function for the break_camel_case function.

    This function tests the break_camel_case function by asserting the expected output
    for different input cases.

    Test cases:
    1. Single word: "hello" should return "hello"
    2. Camel case with two words: "helloWorld" should return "hello World"
    3. Camel case with three words: "helloWorldPython" should return "hello World Python"
    4. Camel case with numbers: "hello123World" should return "hello 123 World"
    5. Camel case with special characters: "hello@World" should return "hello @ World"
    6. Empty string: "" should return ""
    7. All uppercase: "HELLO" should return "H E L L O"
    """

    # Test case 1: Single word
    assert break_camel_case("hello") == "hello"

    # Test case 2: Camel case with two words
    assert break_camel_case("helloWorld") == "hello World"

    # Test case 3: Camel case with three words
    assert break_camel_case("helloWorldPython") == "hello World Python"

    # Test case 4: Camel case with numbers
    assert break_camel_case("hello123World") == "hello 123 World"

    # Test case 5: Camel case with special characters
    assert break_camel_case("hello@World") == "hello @ World"

    # Test case 6: Empty string
    assert break_camel_case("") == ""

    # Test case 7: All uppercase
    assert break_camel_case("HELLO") == "H E L L O"

    print("All test cases pass")

test_break_camel_case()