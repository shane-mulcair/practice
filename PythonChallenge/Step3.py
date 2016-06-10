inputT=open("C:\Users\mulcas4\PycharmProjects\PythonChallenge\step3.txt")
txt=inputT.read()
output=""
for x in txt:
    if x == "{" or x =="}" or x == "(" or x == ")" :
        output+=""
    elif x =="#" or x == "@" or x == "&" or x =="^":
        output+=""
    elif x=="$" or x == "[" or x =="]" or x == "*":
        output+=""
    elif x == "_" or x == "+" or x == "%" or x == '!' or x == '\n':
        output+=""
    else:
        output+=x

print output
