from flask import Flask

app = Flask(__name__)


@app.route('/a1G/pure-function')
def multiply(a, b):
    return a * b


@app.route('/a1G/procedual-function')
def increase_counter(counter):
    counter += 1
    return counter


@app.route('/a1F/immutable-value')
def add_to_tuple(tup, value):
    return tup + (value,)


@app.route('/a1F/mutable-value')
def add_to_list(lst, value):
    lst.append(value)


@app.route('/a1E/oo')
def oo_class():
    class Greeter:
        def __init__(self, name):
            self.name = name

        def greet(self):
            return f"Hello, {self.name}!"

    call = Greeter("Maurizi")
    return call.greet()


@app.route('/b1G/algorithm')
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


unsorted_list = [5, 2, 9, 1, 5, 6]
sorted_list = bubble_sort(unsorted_list)
print(sorted_list)


@app.route('/b1F/algorithm-in-pieces')
def pieces():
    def swap_if_needed(arr, i, j):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

    def bubble_sort_step(arr, end):
        for i in range(end):
            swap_if_needed(arr, i, i + 1)

    def bubble_sort_in_piece(arr):
        n = len(arr)
        for end in range(n - 1, 0, -1):
            bubble_sort_step(arr, end)
        return arr

    unsorted_lst = [5, 2, 9, 1, 5, 6]
    sorted_lst = bubble_sort_in_piece(unsorted_lst)
    print(sorted_lst)


@app.route('/b1E/algorithm-combined')
def combined():
    def calculate_sum(numbers):
        total = 0
        for num in numbers:
            total += num
        return total

    def calculate_average(numbers):
        total = calculate_sum(numbers)
        return total / len(numbers)

    numbers = [5, 10, 15, 20]
    total_sum = calculate_sum(numbers)
    average = calculate_average(numbers)

    print("sum:", total_sum)
    print("average:", average)


@app.route('/b2G/calculator')
def calculator():
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def calculate(a, b, operation):
        return operation(a, b)

    operation_add = add
    operation_subtract = subtract

    result1 = calculate(10, 5, operation_add)
    result2 = calculate(10, 5, operation_subtract)

    print("addition:", result1)
    print("subtraction:", result2)


@app.route('/b2F/high-order-function')
def square(x):
    return x * x


numbers = [1, 2, 3, 4]
squared_numbers = map(square, numbers)
print(list(squared_numbers))


@app.route('/b2E/closure-function')
def multiplier(factor):
    def multiply_by(x):
        return x * factor

    return multiply_by


doubler = multiplier(2)
print(doubler(5))


@app.route('/b3G/lambda-function-1')
def lambda1():
    square = lambda x: x ** 2
    print(square(4))


@app.route('/b3G/lambda-function-2')
def lambda2():
    add = lambda x, y: x + y
    print(add(2, 3))


@app.route('/b3G/lambda-function-3')
def lambda3():
    data = [(1, 'banana'), (2, 'apple'), (3, 'cherry')]
    sorted_data = sorted(data, key=lambda item: item[1])
    print(sorted_data)


@app.route('/b4G/map')
def map_function():
    numbers = [1, 2, 3, 4]
    squared_numbers = map(lambda x: x ** 2, numbers)
    print(list(squared_numbers))


@app.route('/b4G/filter')
def filter_function():
    numbers = [1, 2, 3, 4, 5]
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    print(list(even_numbers))


@app.route('/b4G/reduce')
def reduce_function():
    from functools import reduce

    numbers = [1, 2, 3, 4]
    product = reduce(lambda x, y: x * y, numbers)
    print(product)


@app.route('/b4F/map-filter-reduce')
def map_filter_reduce_function():
    from functools import reduce

    numbers = [1, 2, 3, 4, 5, 6]

    even_numbers = filter(lambda x: x % 2 == 0, numbers)

    squared_even_numbers = map(lambda x: x ** 2, even_numbers)

    product = reduce(lambda x, y: x * y, squared_even_numbers)

    print(product)


@app.route('/b4E/map-filter-reduce-complex')
def map_filter_reduce_complex():
    from functools import reduce

    numbers = [-3, -1, 2, 3, 4, 5]

    positive_odd_numbers = filter(lambda x: x > 0 and x % 2 != 0, numbers)

    squared_positive_odd_numbers = map(lambda x: x ** 2, positive_odd_numbers)

    sum_of_squares = reduce(lambda x, y: x + y, squared_positive_odd_numbers)

    print(sum_of_squares)


@app.route('/c1/refactoring')
def refactoring():
    """
    Code-Beispiel Refactoring
    """
    TAX_RATE = 0.08

    def calculate_tax(price):
        """Berechnet die Steuer für einen gegebenen Preis."""
        return price * TAX_RATE

    def calculate_total_tax(data):
        """Berechnet die Gesamtsumme der Steuern für eine Liste von Preisen."""
        total_tax = 0
        for price in data:
            total_tax += calculate_tax(price)
        return total_tax

    data = [100, 200, 300]
    print(calculate_total_tax(data))


if __name__ == '__main__':
    app.run()
