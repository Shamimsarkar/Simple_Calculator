from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operation_list = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}
def calculator():

    should_continue = True

    first_number = float(input("What's the first number?: "))

    while should_continue:

        for operation in operation_list:
            print(operation)

        operation_pick = input("Pick an operation: ")

        second_number = float(input("What's the next number?: "))

        result = operation_list[operation_pick](first_number,second_number)
        print(f"{first_number} {operation_pick} {second_number} = {result}")


        continue_operation = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation: ")

        if continue_operation == "y":
            first_number = result
        else:
            should_continue = False
            print("\n"*20)
            calculator()
calculator()