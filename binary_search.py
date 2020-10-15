def b_search(tbl: list, in_num: int):
    n = len(tbl)
    left = 0
    right = n - 1
    mid = (left + right) // 2
    while tbl[mid] != in_num and left < right:
        if tbl[mid] > in_num:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2

    if tbl[mid] == in_num:
        return mid
    # return "Not Found"
    return n * 1000