line= int(input())
i=0
w=[]
while i<line:
    word=input()
    w.append(word)
    i+=1
S=set(w)
print(len(S))


from collections import Counter

count= dict(Counter(w))


for k in count.keys():
    print(count[k],end=' ')

print()