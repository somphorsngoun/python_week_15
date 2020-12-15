studentsDic1 = eval(input())
studentsDic2 = eval(input())

# Enter your code here. Read input from STDIN. Print output to STDOUT
result = {}
for n in studentsDic1:
    X = False
    for i in studentsDic2:
        if n == i:
            result[n] = studentsDic1[n] + studentsDic2[i]
            X = True
    if X == False:
        result[n] = studentsDic1[n]
Y = result
for r in studentsDic2:
    for a in Y:
        if r != a:
            result[r] = studentsDic2
print(result)