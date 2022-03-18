nums = [1, 2, 3, 6, 5, 4]
while True:
	counter = 0
	for x in range(len(nums) - 1):
		c = nums
		a = nums[x]
		b = nums[x + 1]

		if b > a:
			counter += 1
			nums[x],nums[x + 1] = nums[x + 1],nums[x]
			print(nums)

	if counter == 0:
		break
print(nums)
