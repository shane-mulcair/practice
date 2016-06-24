def count_code(str):
    count = 0
    for s in range(len(str)):
        if len(str) >= 4 and s + 3 < len(str):
            if str[s] == "c" and str[s + 1] == "o" and str[s + 3] == "e":
                count += 1
                s += 3
    return count


print count_code("code")
print count_code("aaacodebbb")
print count_code("AAcodeBBcoleCCccoreDD")
