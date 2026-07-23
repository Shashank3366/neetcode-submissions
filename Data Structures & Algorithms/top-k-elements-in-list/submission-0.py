from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr=Counter(nums)
        return [num for num,freq in arr.most_common(k)]
        