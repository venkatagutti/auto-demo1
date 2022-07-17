def are_equal(expected_result: object, actual_result: object):
    if expected_result == actual_result:
        pass
    else:
        print(f'Test failed - Expected: {expected_result}, Actual: {actual_result}')
        raise AssertionError()


def text_contains(text_to_find: str, full_text: str):
    if text_to_find.lower() in full_text.lower():
        pass
    else:
        print(f'Test failed - Full text "{full_text}" does not contain "{text_to_find}"')
        raise AssertionError()


def is_greater_than(number1: float, number2: float):
    if number1 > number2:
        pass
    else:
        print(f'Test failed - {number1} not greater than {number2}')
        raise AssertionError()
