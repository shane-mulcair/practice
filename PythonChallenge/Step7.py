import re
import zipfile
z=zipfile.ZipFile("C:\Users\mulcas4\Downloads\channel.zip")
with open("C:\Users\mulcas4\PycharmProjects\PythonChallenge\step7\90052.txt") as f:
    content=f.readline()
output=re.sub(r'\D',"",content)
while output != 0:
    with open("C:\Users\mulcas4\PycharmProjects\PythonChallenge\step7\\"+output+".txt") as f:
        content = f.readline()
    output = re.sub(r'\D', "", content)
    print ''.join([z.getinfo(output+".txt").comment])
