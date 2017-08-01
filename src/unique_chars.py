"""Find unique characters from a list of similar characters."""


def find_uniq(list_input):
    """Find unique characters from a list of similar characters."""
    if type(list_input) not in (tuple, list) or len(list_input) < 3:
        raise ValueError('Please enter a list containing two or more strings.')
    _validate_item(list_input[0])
    start = set(list_input[0].replace(' ', '').lower())
    for i in range(len(list_input)):
        _validate_item(list_input[i])
        if set(list_input[i].replace(' ', '').lower()) != start:
            if i < len(list_input) - 1:
                _validate_item(list_input[i + 1])
                if set(list_input[i + 1].replace(' ', '').lower()) == start:
                    return list_input[i]
                else:
                    return list_input[i - 1]
            else:
                return list_input[i]
    return


def _validate_item(item):
    """Ensure item is a string."""
    if type(item) is not str:
            raise ValueError('This list contains one or more items that are not strings.')
