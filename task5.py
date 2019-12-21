def string_length(bar):
    return(len(bar))

def test_string_length():
    assert string_length('hello!') == 6
    assert string_length('banana') == 6
    assert string_length('8') == 1
    assert string_length('funnyguys') == 9
    assert string_length('101') == 3
    print("YOUR CODE IS CORRECT!")

#test your code by un-commenting the line(s) below
test_string_length()