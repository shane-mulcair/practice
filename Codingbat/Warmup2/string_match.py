def string_match(a, b):
    counter = 0
    for x in range(len(a) - 1):
       substr = a[x:x+2]
       if b[x:x + 2] == substr:
          counter += 1
    return counter


print string_match('xxcaazz', 'xxbaaz')
print "hello"[-2:]
print "hello"[:-2]
print "hello"[:2]
