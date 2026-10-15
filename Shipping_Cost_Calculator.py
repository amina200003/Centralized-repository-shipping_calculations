# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost in USD: {shipping_cost} USD")

## new update by amina200003
print (f"Shpping cost in KWD: {shipping_cost * 0.3111} KWD")
