# Calculator

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}


def operations_list():
    for operand in operations:
        print(operand)


def calculator():
    first_num = float(input("what is the first number? "))
    operations_list()
    should_continue = True

    while should_continue:

        user_operand = input("pick an operation: ")

        second_num = float(input("what is the next number? "))

        calculate_function = operations[user_operand]
        answer = calculate_function(first_num, second_num)

        print(f"{first_num} {user_operand} {second_num} = {answer}")

        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' start a new calculation "
                                f"or "
                                f"'q' to quit: ")

        if should_continue == "n":
            should_continue = False
            calculator()
            operations_list()
        elif should_continue == "y":
            first_num = answer
            operations_list()
        else:
            should_continue = False
            print("INVALID OPTION!!!")


calculator()
