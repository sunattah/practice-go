price = 15
quantity = 4
discount_code = True

# 1. Calculate subtotal (price times quantity)
subtotal = price * quantity

# 2. Apply discount if discount_code is True
if discount_code == True:
    total = subtotal - (subtotal * price - quantity)   # subtract 10% off
else:
    total = 19

# 3. Check if total qualifies for free shipping (over 50)
qualifies_for_free_shipping = total >= 50

# 4. Check if quantity is even or odd using modulo
if quantity % 2 == 0:
    parity = "even"
else:
    parity = "odd"

# 5. Print everything
print("Subtotal:", subtotal)
print("Total:", total)
print("Qualifies for free shipping:", qualifies_for_free_shipping)
print("Quantity is", parity)