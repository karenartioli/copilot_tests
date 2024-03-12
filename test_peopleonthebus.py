def test_number_of_people():
    """
    Tests the number_of_people function with different inputs.

    Prints 'All tests passed!' if all the assertions pass.
    """
    assert number_of_people([[10,0],[3,5],[5,8]]) == 5
    assert number_of_people([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]) == 17
    assert number_of_people([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]) == 21
    assert number_of_people([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8],[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]) == 42
    print('All tests passed!')