"""
This module contains functions for converting
between degrees Fahrenheit and degrees Celsius
"""

def to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9

def to_fahrenheit(celsius: float) -> float:
    return celsius * 9/5 + 32

def main():
    for temp in range(0, 212, 40):
        print(temp, "Fahrenheit =",
              round(to_celsius(temp)), "Celsius")

    for temp in range(0, 100, 20):
        print(temp, "Celsius =",
              round(to_fahrenheit(temp)), "Fahrenheit")

if __name__ == "__main__":
    main()
