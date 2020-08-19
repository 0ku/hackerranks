n,p = map(int,input().split(" "))
countries = {}
allpeople = []
pairs = []
finished = []
for a in range(0,n):
    countries[a] = [a]
    allpeople.append(a)

for a in range(0,p):
    p1,p2 = map(int,input().split(" "))
    countries[p1].append(p2)
    countries[p2].append(p1)

for x in countries.keys():
    for a in countries[x]:
        for b in countries[a]:
            if b not in countries[x]:
                countries[x].append(b)

combinations = 0
for a in countries.keys():
    for currentPerson in allpeople:
        if currentPerson not in countries[a] and currentPerson not in finished:
            combinations+=1
            pairs.append([currentPerson,a])
    finished.append(a)
print(combinations)

