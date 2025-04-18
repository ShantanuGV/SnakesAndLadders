#quicksort

def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0] #Taking the First element as the pivot
    left=[x for x in arr[1:] if x < pivot] #Elements smaller than pivot
    middle=[pivot] # Pivot element
    right=[x for x in arr[1:] if x >= pivot] #Elements greater than or equal to pivot
    return quicksort(left) + middle + quicksort(right)

def display_top_five(arr):
    sorted_arr = quicksort(arr)
    print(" Soretd Array : ", sorted_arr)
    top_five = sorted_arr[-5:] #Get the top 5 scores
    top_five.reverse()
    print("Top 5 Scores: ")
    for score in top_five:
        print(score)

print("\n Program for Quicksort")
student_percentages = input(" Enter student percentages : ")
student_percentages = list(map(float, student_percentages.split()))
display_top_five(student_percentages)