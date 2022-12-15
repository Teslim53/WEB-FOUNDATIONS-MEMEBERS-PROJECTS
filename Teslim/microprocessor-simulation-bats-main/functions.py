# Processor Operations
def noop():
    """Do nothing, print empty line"""
    print()


def add(first_number, second_number) -> int:
    """Add arguments"""
    total = (first_number + second_number)
    return total


def mul(first_number, second_number) -> int:
    """Multiply arguments"""
    total = (first_number * second_number)
    return total


def gt(first_number, second_number) -> int:
    """Check if first number is greater than second number"""
    if first_number > second_number:
        return 1
    else:
        return 0


def or_func(first_number, second_number) -> int:
    """Logical or(that is,)"""
    if (first_number > 0) or (second_number > 0):
        return 1
    else:
        return 0


def nand(first_number, second_number) -> int:
    """Logical nand ("not and")"""
    multiplied = (first_number * second_number)
    if multiplied == 0:
        return 1
    else:
        return 0


def min_func(numbers) -> list:
    """Find the minimum value of arguments"""
    return min(numbers)


def shift(first_number, second_number) -> int:
    """Shift left by a number of bits"""
    result = first_number << second_number
    return result


def invalid(operation) -> str:
    """Any non-valid operations"""
    print(f'invalid operation {operation}')
    return (f'invalid operation {operation}')


def check_if_integer(first_item, second_item=0) -> str:
    """Checks if two items are integers"""
    try:
        first_item = float(first_item)
        second_item = float(second_item)
        # Check if numbers have no remainder after division by 1
        if (first_item % 1) == 0.0 and (second_item % 1) == 0.0:
            return True
        else:
            return -1
    except:
        return -1


def check_if_decimal(first_item, second_item) -> str:
    """Checks if two items are decimal(0-9)"""
    if (first_item.isdecimal()) and (second_item.isdecimal()):
        return True
    else:
        return -1


def validate_operation(operation) -> str:
    """Check what is inputted and validate it or return an error"""

    VALID_OPERATIONS = ['noop', 'add', 'mul',
                        'gt', 'or', 'nand', 'min', 'shift']
    TWO_ARGUMENTS_FUNCTIONS = ['add', 'mul', 'gt', 'or', 'nand', 'shift']
    length_operation = len(operation)

    if length_operation == 0:
        invalid(operation)

    else:
        operation_list = operation.split(' ')
        length_operation = len(operation_list)
        first_item = operation_list[0]
        if length_operation > 2:
            second_item = operation_list[1]
            third_item = operation_list[2]

        # Check where first_item falls in
        if first_item in VALID_OPERATIONS:
            if first_item in TWO_ARGUMENTS_FUNCTIONS and (length_operation > 3 or length_operation < 3):
                invalid(operation)

            elif first_item == 'noop':
                if length_operation == 1:
                    noop()
                else:
                    invalid(operation)

        # Use strict conditions to validate various types of operations
            elif first_item == 'add':
                if length_operation == 3 and length_operation == 3:
                    if check_if_integer(second_item, third_item) == True:
                        print(add(int(second_item), int(third_item)))
                        return add(int(second_item), int(third_item))
                    else:
                        invalid(operation)

            elif first_item == 'mul' and length_operation == 3:
                if check_if_integer(second_item, third_item):
                    print(mul(int(second_item), int(third_item)))
                    return mul(int(second_item), int(third_item))
                else:
                    invalid(operation)

            elif first_item == 'gt' and length_operation == 3:
                if check_if_integer(second_item, third_item):
                    print(gt(int(second_item), int(third_item)))
                    return gt(int(second_item), int(third_item))
                else:
                    invalid(operation)

            elif first_item == 'or' and length_operation == 3:
                if check_if_integer(second_item, third_item):
                    print(or_func(int(second_item), int(third_item)))
                    return or_func(int(second_item), int(third_item))

                else:
                    invalid(operation)

            elif first_item == 'nand' and length_operation == 3:
                if check_if_integer(second_item, third_item):
                    print(nand(int(second_item), int(third_item)))
                    return nand(int(second_item), int(third_item))

                else:
                    invalid(operation)

            elif first_item == 'min':
                for number in operation_list[1:]:
                    result = check_if_integer(number)
                    if result != True:
                        invalid(operation)
                        return -1
                # Convert numbers(in string type) to int type
                numbers_list = [int(number) for number in operation_list[1:]]
                print(min_func(numbers_list))
                return min_func(numbers_list)

            elif first_item == 'shift':
                if (check_if_decimal(second_item, third_item)) and (length_operation == 3):
                    if (int(second_item) > 0) and (int(third_item) > 0):
                        print(shift((int(second_item)), (int(third_item))))
                        return shift(int(second_item), int(third_item))
                    elif (int(second_item) == 0) or (int(third_item) == 0):
                        invalid(operation)
                    else:
                        return invalid(operation)
                else:
                    return invalid(operation)

        elif first_item not in VALID_OPERATIONS:
            invalid(operation)
