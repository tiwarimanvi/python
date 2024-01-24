#linear search
def Lsearch(AR,ele):
    for i in range(0,len(AR)):
        if AR[i]==ele:
            return i
    return -1
AR=eval(input("enter the list"))
ele=int(input("enter the ele to be searched:"))
n=L
serach(AR,ele)
if n==-1:
    print("ele not found")
else:
    print("ele found")
