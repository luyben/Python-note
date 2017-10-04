# Handle single quantity
def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result

# convert xx.yy to xx dollar and yy cent
def convert(val):
    # split into dollars and cents
    dollars = int(val)
    cents = round((100*(val - dollars)))
    
    # convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")
    
    # return composite string
    if dollars == 0 and cents == 0:
        print "Broke!!"
    elif dollars == 0:
        print cents_string
    elif cents == 0:
        print dollars_string
    else:
        print dollars_string + " " + cents_string 

convert(12)
convert(0)
convert(0.1)
convert(12.34)
