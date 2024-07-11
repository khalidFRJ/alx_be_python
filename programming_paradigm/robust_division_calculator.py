def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: you can not devide by zero"
    except ValueError:
        return "Error: Please enter numeric values ."


