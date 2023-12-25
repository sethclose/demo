print("Hello, Test Function")

"""
This is a comment block.
"""

x = lambda a : a + 10
print(x(5))

f = open("textfile.txt")
print(f.read())

g = open("/home/sethclose/Python-3.12.0/Python/testfunction.py", "r")
#for line in g:
#    print(line)

print(g.read(100))