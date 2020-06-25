l = ["washington", "test", "key", "random"]


## Approach 1
long_str_len = len(max(l,key=len))
temp_l = []

for i in range(len(l)):
    if len(l[i]) != long_str_len:
        diff = long_str_len - len(l[i])
        var = '*' * diff
        var = var + l[i]
        temp_l.append('|'.join(var))
    else:
        temp_l.append('|'.join(l[i]))
for row in temp_l:
    print(row)


## Approach 2
myArray = l
mx = len(max(myArray, key= len ))
mn = len(min(myArray,key = len))
temp_list = []
for i in myArray:
    if len(i)<=mx and len(i)>mn:
        temp_list.append(i)
    elif len(i)== mn:
        temp_list.append(i)
        break
for row in temp_list:
    print("|".join("{:*>{mx}}".format(row,mx=mx)))


## One Liner Approach

long_str_len = len(max(l,key=len))
matrix = ['|'.join(('*' * (long_str_len - len(l[i]))) + l[i]) for i in range(len(l))]
for row in matrix:
    print(row)
