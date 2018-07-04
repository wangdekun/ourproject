print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print(3 * 'un' + 'ium')
print('Py' 'thon')
prefix = 'Py'
print(('un' * 3) + 'ium')
print(prefix + 'ium')
text = ('Put several strings within parentheses '
'to have them joined together.')
print(text)
word = 'Python'
print(word[0],word[-1],word[0:2])
print(len('sssdskdasdjsabdjsbdjsadsd'))
print('%(language)s has %(number)03d quote types.' % {'language': "Python", "number": 2})
a=['a','b','c','d']
b=['c','d','e','f']
for x in a:
	if x in b:
		a.remove(x)
print (a)

'''x = int(input("Please enter an integer: "))
if x<0:
    x=0
    print('qwerty')
elif x==0:
    print('asdf')
elif x==1:
    print('zxcv')
else:
    print('MORE')
print(x)'''
for i in range(5):
    print(i)
print(range(10))
range(5,10)
