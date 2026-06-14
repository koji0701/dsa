class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        rv = set()
        counts = defaultdict(int) 
        bar = len(nums) // 3

        for num in nums: 
            counts[num] += 1
            if counts[num] > bar: 
                rv.add(num) 
        
        return list(rv)
