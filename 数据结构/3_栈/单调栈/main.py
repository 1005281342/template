_ = input()
nums = [int(x) for x in input().split(" ")]

stk = list()
ans = [-1] * len(nums)
for i, num in enumerate(nums):
    if not stk:
        stk.append(num)
        continue
    while stk and stk[-1] >= num:
        stk.pop()
    if stk:
        ans[i] = stk[-1]
    stk.append(num)

print(ans)
