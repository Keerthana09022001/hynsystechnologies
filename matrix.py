import re


first_multiple_input = input().rstrip().split()

x = int(first_multiple_input[0])

y = int(first_multiple_input[1])

matrix = []

for _ in range(x):
    matrix_item = input()
    matrix.append(matrix_item)
elements = []
result=''
for t in range(y):
    for w in matrix:
        elements.append(w[t])
result = "".join(elements)
pattern=r'\b[^a-zA-Z0-9]+\b'
print(re.sub(pattern,r' ',result))
