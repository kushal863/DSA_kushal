
def search(arr,target, find_first_element:True):
        # check first occurence of target first
    ans  = -1
    start =0
    end = len(arr)-1

    if (target>arr[end]):
        return -1

    while (start<=end):
        mid = int((start+end)/2)

        if (target< arr[mid]):
            end = mid -1
        elif (target >arr[mid]):
            start = mid+1

        else:
            # Potential ans found
            ans = mid
            if find_first_element:
                end = mid-1
            else:
                start = mid+1
    return ans
    


def search_range(arr,target):
    ans =[-1,-1]

    ans[0] = search(arr,target,find_first_element=True)
    if (ans[0]!=-1):
        ans[1] = search(arr,target,find_first_element=False)


    return ans

arr = [3,4,6,7,7,7,8,9,10]
target = 11

print(search_range(arr,target))