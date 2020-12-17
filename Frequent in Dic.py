import operator
string = input("Please enter a String:")

freq ={}

for i in string:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1

sorted_d = dict( sorted(freq.items(), key=operator.itemgetter(1),reverse=True))
print(sorted_d)
