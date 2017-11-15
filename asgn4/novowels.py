def novowels (s):
    new_s = ""
    for c in s:
        if c != "a" and c != "e" and c != "i" and c != "o" and  c!= "u":
            new_s = new_s + c
    return new_s

print(novowels("hello there"))

i = 0
while i < 0:
    i = i + 1
    #do stuff

for i in range(10):
    for j in range(3):
        print(i,j)


def is_palindrome(s):
    for i in range(len(s)):
        if s[i] != s[-1-i]:
            return False
    return True


#novowels("hello there"
print(is_palindrome("madam"))
print(is_palindrome("hello"))
