word = input()

# Enter your code here. Read input from STDIN. Print output to STDOUT
result = {}
for n in range(len(word)):
    number = 0
    for i in range (len(word)):
        if word[n] == word[i]:
            number += 1
    if word[n] !=" ":
        result[word[n]] = number
print(result)