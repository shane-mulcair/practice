import re
with open("C:\Users\mulcas4\PycharmProjects\PythonChallenge\step4.txt") as f:
    content=f.readlines()

for x in range(len(content)):
    matchObj = re.search("[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]", content[x], 0)
    if matchObj:
        print matchObj.group()[4]