def pretty_price(gross_price, extension):
    if isinstance(extension, int):
        extension = extension/100
    return int(gross_price) + extension


print(pretty_price(3.50, 0.95))
print(pretty_price(3.50, 95))