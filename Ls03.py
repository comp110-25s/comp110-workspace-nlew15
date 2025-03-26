def celsius_to_fahrenheit(degrees: int) -> float:
    """Convert degrees Celsius to degrees Fahrenheit"""
    return (degrees * 9 / 5) + 32


print(celsius_to_fahrenheit(degrees=0))
print(celsius_to_fahrenheit(degrees=10))


def perimeter(length: float, width: float) -> float:
    return 2 * length + 2 * width


print(perimeter(length=10.0, width=8.0))
