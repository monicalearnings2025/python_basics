#find every occurrance of substring in the given string

a = 'abcabccabc'
sub = 'abc'

def find(a,sub):
    a_len = len(a)
    sub_len = len(sub)
    occurrence = 0
    index = []
    for i in range(a_len):
        if a[i:i+sub_len] == sub:
            occurrence += 1
            index.append(i)
    return occurrence, index

    
print(find(a,sub))
