def convert_units(amount, us_unit, metric_unit):
    conversion_factors = {
        ("pound", "kilogram"): 0.45,                           # 1 pound = 0.45 kilograms
        ("mile", "kilometer"): 1.61,                          # 1 mile = 1.61 kilometers
        ("fahrenheit", "celsius"): lambda f: (5 / 9) * (f - 32),  # Fahrenheit to Celsius conversion
        ("gallon", "liter"): 3.79                             # 1 gallon = 3.79 liters
    }


#    if not (isinstance(amount, int) or isinstance(amount, float)):
#        raise Exception("Amount must be a number.")
    
#    if not (amount < 0):
#        raise Exception("Amount must be a non-negative number.")
    
    # Check if amount is a non-negative number
    if not (isinstance(amount, int) or isinstance(amount, float)) or amount < 0:
        raise Exception("Amount must be a non-negative number.")

    # Check if unit names are valid strings
    if not isinstance(us_unit, str) or not isinstance(metric_unit, str):
        raise Exception("Unit names must be strings.")

    # Convert unit names to lowercase and form a key
    key = (us_unit.lower(), metric_unit.lower())

    # Check if the unit conversion is valid
    if key not in conversion_factors:
        raise Exception("Invalid unit conversion. Allowed conversions are: pound to kilogram, mile to kilometer, fahrenheit to celsius, gallon to liter.")

    # Perform the conversion based on the type of the conversion factor
    conversion_factor = conversion_factors[key]
    if isinstance(conversion_factor, float):
        return amount * conversion_factor
    else:
        # If it's a function, apply the function to the amount
        return conversion_factor(amount)
    
    