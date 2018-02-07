# 직접 해보기 1
likes = ''
likes += 'Cinema, '
likes += 'Youtube, '
likes += 'Apple'
print(likes)
print(likes[0:6])
print(likes[8:-7])
print(likes[-5:])

# 직접 해보기 2
nums = []
i = 0
while i < 10:
  nums.append(i + 1)
  i += 1
print(nums[:1])
print(nums[-1:])
print(nums[0:3])
print(nums[0:2] + nums[-2:])
nums.reverse()
print(nums)
del nums[::2]
print(nums)
