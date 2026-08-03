celsius = 28

# 1. Convert to fahrenheit
fahrenheit = celsius * 9/5 + 32

# 2. Check if fahrenheit is greater than 90
is_hot = fahrenheit > 90

# 3. Check if celsius is exactly equal to 28
is_28 = celsius == 28

# 4. Check if celsius is divisible by 4 (remainder is 0)
divisible_by_4 = celsius % 4 == 0

# 5. Print everything
print("Fahrenheit:", fahrenheit)
print("Is hot:", is_hot)
print("Is 28:", is_28)
print("Divisible by 4:", divisible_by_4)