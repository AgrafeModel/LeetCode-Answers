class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float("inf")
        nums.sort()
        for i in range(len(nums)):
            left,right = i+1,len(nums)-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if(abs(target - s)<abs(target - res)):
                    res = s

                if(s < target):
                    left +=1
                elif(s>target):
                    right-=1
                else:
                    return target   
        return res
