f = open("C:\Users\mulcas4\PycharmProjects\CodeAbbey\inputs\\body_mass_index.txt")
inputs = []
for line in f:
    weight, height = line.split()
    bmi = (float(weight) / (float(height) * float(height)))
    if float(bmi) < 18.5:
        inputs.append("under")
    elif 18.5 <= float(bmi) < 25:
        inputs.append("normal")
    elif 25 <= float(bmi) < 30:
        inputs.append("over")
    else:
        inputs.append("obese")
print " ".join(str(x) for x in inputs)
