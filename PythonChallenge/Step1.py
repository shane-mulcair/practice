# Adding two to each letter
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q" \
       " ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
output = ""
for x in text:
    if x == " ":
        output += " "
    elif x == "y":
        output += "a"
    elif x == "z":
        output += "b"
    elif ord(x)<65 or ord(x)>122:
        output +=chr(ord(x))
    else:
        output += chr(ord(x) + 2)
print output
