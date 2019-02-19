# prompting string input by user
word = str(input('enter any word: '))

# list declaration
vowels = ['a', 'e', 'i', 'o', 'u']

# count initialization
vowelCount = 0

for str in word:
    for i in vowels:
        if str == i:
            vowelCount +=1

print("vowels[%s] " %(vowelCount))