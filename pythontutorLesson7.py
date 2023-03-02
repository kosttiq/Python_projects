#EVEN INDICES
a = input().split()
for i in range (0, len(a), 2):
    print(a[i])

#EVEN ELEMENTS
l = input()
a = [int(l) for l in l.split()]
for i in a:
    if int(i)%2 == 0:
        print(i)
        
# > THAN PREVIOUS
a = [int(b) for b in input().split()]
for b in range(1, len(a)):
    if a[b] > a[b-1]:
        print(a[b])

#SAME SIGN
l = input()
a = [int(l) for l in l.split()]
for l in range(1, len(a)):
    if a[l-1] * a[l]>0:
        print(a[l-1], a[l])
        #break (??)

#MAX INDEX
a=[int(i) for i in input().split()]
for i in range(len(a)):
    if a[i]==max(a):
        print(max(a),i)
        break
    
#
