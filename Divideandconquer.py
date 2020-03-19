def Bsearch(list, val):
    list_size = len(list)-1

    beg = 0
    end = list_size

    while beg <= end:
        midval = (beg+end)//2

        if list[midval] == val:
            return midval
        if val > list[midval]:
            beg = midval+1
        else:
            end = midval-1


   if beg > end:
     return None


list = [2, 5, 6, 9, 8, 7]
print(Bsearch(list, 8))
print(Bsearch(list, 25))
