# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#"Декораторы"


def is_prime(func):
# внутренняя функция wrapper в is_prime
    def wrapper(*args, ** kwargs):
        result = func(*args, ** kwargs)
        sum_ = sum(args)
        k = 0
        for i in range(2, sum_ // 2 + 1):
            if sum_ % i == 0:
                k = k +1
        if k <= 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

# @is_prime - декоратор для функции sum_three
@is_prime
# Функция, которая складывает 3 числа (sum_three)
def sum_three(*args):
    return sum(args)



result = sum_three(2, 3, 6)
print(result)
