numInputs = raw_input("How many pairs are you giving?:")
counter=1
totals=[]
while (counter<=int(numInputs)):
    inputs = raw_input("Please give the pair of numbers?:")
    total=0
    for num in inputs.split():
        total += int(num)
    totals.append(total)
    counter+=1
print totals