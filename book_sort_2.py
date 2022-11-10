import sys
N = sys.stdin.readline().rstrip()
array=[]
for i in range(int(N)):
    array.append(int(sys.stdin.readline().rstrip()))

def count_sort(array):
    count_array = [0]*(max(array)+1)
    for i in array:
        count_array[i]+=1
        
    for i in range(len(count_array)):
        for j in range(count_array[i]):
            print(i,end=" ")
        
def insert_sort(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if array[j]<array[j-1]:
                array[j],array[j-1]=array[j-1],array[j]
            else:
                break
    return array

def quick_sort(array,start,end):
    if start>=end:
        return
    left=start+1
    right=end
    pivot = start
    while left<=right:
        while left <= end and array[left]<= array[pivot]:
            left+=1
        while right>start and array[right]>=array[pivot]:
            right-=1
        if left>right:
            array[right],array[pivot] = array[pivot],array[right]
        else:
            array[left],array[right] = array[right],array[left]
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)
    return array
    
def select_sort(array):
    for i in range(len(array)):
        min_index=i
        for j in range(i+1,len(array)):
            if array[min_index]>array[j]:
                min_index=j
        array[i],array[min_index]=array[min_index],array[i]
    return array
        
#count_sort(array)
#print()
#print(insert_sort(array))
#print(quick_sort(array,0,len(array)-1))
print(select_sort(array))