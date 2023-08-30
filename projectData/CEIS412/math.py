from flask import Flask, request, current_app




app = Flask(__name__)

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

if __name__ == '__main__':
    app.run()