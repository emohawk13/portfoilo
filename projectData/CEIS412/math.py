from flask import Flask, request, current_app
import time
app = Flask(__name__)

# week 1 Math for sales app
def get_sales(monthArray, monthlySales):
    for i, month in enumerate(monthArray):
        sales = request.form.get(month)
        if sales is not None:
            monthlySales[i] = float(sales)

def compute_total_sales(monthlySales):
    total = sum(monthlySales)
    return total

def compute_average_sales(monthlySales):
    total = compute_total_sales(monthlySales)
    average = total / len(monthlySales)
    formatted_average = "{:.2f}".format(average)
    return formatted_average

def compute_highest_month(monthlySales):
    highest_index = monthlySales.index(max(monthlySales))
    return highest_index

def compute_lowest_month(monthlySales):
    lowest_index = monthlySales.index(min(monthlySales))
    return lowest_index

# Week 2 math for patterns
def generate_pattern(pattern_function, numRows):
    pattern_lines = pattern_function(numRows).split('\n')[:-1]  # Split by newline and remove the last empty string
    return pattern_lines
        
def patA(numRows):
    result = ""
    for i in range(1, numRows + 1):
        result += '*' * i + '\n'
    return result

def patB(numRows):
    result = ""
    for i in range(numRows, 0, -1):
        result += '*' * i + '\n'
    return result

def patC(numRows):
    result = ""
    for i in range(1, numRows + 1):
        result += ' ' * (i - 1) + '*' * (numRows - i + 1) + '\n'
    return result

def patD(numRows):
    result = ""
    for i in range(numRows, 0, -1):
        result += ' ' * (i - 1) + '*' * (numRows - i + 1) + '\n'
    return result

if __name__ == '__main__':
    app.run()