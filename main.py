nums = [1, 7, 2, 3, 6, 5, 4, 9, 2]
counter = True
while counter:
	counter = False
	for x in range(len(nums) - 1):
		c = nums
		a = nums[x]
		b = nums[x + 1]

		if b > a:
			counter = True
			nums[x],nums[x + 1] = nums[x + 1],nums[x]
			print(nums)

print(nums)
