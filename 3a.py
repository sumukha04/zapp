s=input("Enter a sentence")
w, d, u, l=0, 0, 0, 0
l_w=s.split()
w=len(l_w)
for c in s:
    if c.isdigit():
        d=d+1
        if c.isupper():
            u=u+1
            if c.islower():
                l=l+1
                print("numer of words", w)
                print("number of digits", d)
                print("number of uppercase", u)
                print('number of lowercase', l)