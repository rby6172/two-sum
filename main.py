from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
	dic={}
	for i in range(len(nums)):
		num=nums[i]
		a=target-num
		if a in dic:
			return [dic[a], i]
		dic[num]=i

