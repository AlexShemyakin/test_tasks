# Сортировка слиянием
# Данная сортировка отлично подходит под требования задачи,
# т.к. даже при худшем случае сложность сортировки будет nlog(n) 
def merge_sort(arr: list):
    """Sort of merge."""
    if len(arr) <= 1:
        return arr
    mid = int(len(arr) / 2)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left: list, right: list) -> list:
    """Merge left and right arrays."""
    result: list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

