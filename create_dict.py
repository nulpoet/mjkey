import json

list_f = []
for a in  open("alldump.txt").readlines():
    if a!="\n":
        list_f.append(a)


features = []
for a in list_f:
    features.append(a[0:len(a)-1])

dictf = {}
for a in features:
    hashf = json.loads(a)
    dictf[hashf['path']] = hashf

for a in dictf.keys():
    print a,dictf[a]


