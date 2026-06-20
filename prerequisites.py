'''
count the frequency of the characters
ex:
input: aabc
output
a:3
b:1
c:1

'''
'''
s=input()
freq={}
for i in range(len(s)):
    ch=s[i]
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)

'''
s=input()
freq={}
max_freq=1
for i in range(len(s)):
    ch=s[i]
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for key in freq:
    if freq[key]>max_freq:
        max_freq=freq[key]
        max_char = key
print(max_freq,key)