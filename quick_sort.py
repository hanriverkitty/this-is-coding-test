
q_array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(q_array, start, end):
    if start >= end:
        return
    pivot = start
    left=start+1
    right = end
    while left <=right:
        while left<=end and q_array[left]<=q_array[pivot]:
            left+=1
        while right>start and q_array[right]>=q_array[pivot]:
            right-=1
        if right<left:
            q_array[right],q_array[pivot]=q_array[pivot],q_array[right]
        else:
            q_array[left],q_array[right]=q_array[right],q_array[left]
    quick_sort(q_array,start,right-1)
    quick_sort(q_array,right+1,end)
    
quick_sort(q_array,0,len(q_array)-1)
print(q_array)