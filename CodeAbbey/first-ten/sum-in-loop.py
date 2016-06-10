numInputs = raw_input("How many numbers are you giving?:")
inputs = raw_input("Please give the list of numbers?:")
total = 0
for num in inputs.split():
    total += int(num)
print total
