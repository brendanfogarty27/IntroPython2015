# print ("let's see if this works")
# a = ('+' + '-'*4) * 2 + '+'
# b = ('|' + " "*4) * 2 + '|'
# print ((a + ('\n' + b)*4) + '\n' + (a + ('\n' + b)*4) + '\n' +a)

def mkgrid(k):
    a = ('+' + '-'*(4+k)) * 2 + '+'
    b = ('|' + " "*(4+k)) * 2 + '|'
    return (a + ('\n' + b)*k) + '\n' + (a + ('\n' + b)*k) + '\n' +a

print(mkgrid(3))

print(mkgrid(5))
