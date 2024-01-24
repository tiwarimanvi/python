#binary search
def Bsearch(AR,ele):
    beg=0
    last=len(AR)-1
    while beg<=last:
        mid=(beg+last)//2
        if AR[mid]==ele:
            return mid
        elif ele>AR[mid]:
            beg=mid+1
        else:
            last=mid-1
    return -1
AR=eval(input("enter the list"))
ele=int(input("enter the ele to be searched:"))
n=Bserach(AR,ele)
if n==-1:
    print("ele not found")
else:
    print("ele found")
    
