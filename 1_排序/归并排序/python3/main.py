def merge_sort(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    mid = len(nums) >> 1
    return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))


def merge(a: list, b: list) -> list:
    ans = list()
    ai = bi = 0
    while ai < len(a) and bi < len(b):
        if a[ai] <= b[bi]:
            ans.append(a[ai])
            ai += 1
        else:
            ans.append(b[bi])
            bi += 1

    if ai < len(a):
        ans.extend(a[ai:])

    if bi < len(b):
        ans.extend(b[bi:])

    return ans


if __name__ == '__main__':
    case = [2, 4, 2, 3, 10, 99, 4, 6, 2, 1, 5, 77, 2]
    print(merge_sort(case))
