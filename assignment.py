def format_string(name, age):
    return f"My name is {name} and I am {age} years old"


def conditional_check(number):
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"


def loop_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i

    return sum


def list_operations(numbers):
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return (total, maximum, minimum)


def dict_operations(students_dict):
    list_students = []

    for name, score in students_dict.items():
        if score > 80:
            list_students.append(name)

    return list_students


def set_operations(list1, list2):
    return set(list1) & set(list2)


def arithmetic_ops(a, b):
    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    return {"sum": a + b, "difference": a - b, "product": a * b, "quotient": quotient}


def logical_ops(x, y):
    return {"and": x and y, "or": x or y, "not_x": not x}


def bitwise_ops(a, b):
    return {"and": a & b, "or": a | b, "xor": a ^ b}
