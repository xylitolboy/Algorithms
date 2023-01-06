class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev:
                return[prev[diff], i]
            prev[n] = i 
        return
#Brute Force를 쓰면 모든 값을 다 찾기 때문에 시간이 O(n**2 시간이 듬.)
#그래서 해시 맵을 쓰는 거임. i가 값, n이 index 
#리스트 각각의 value를 접근하는데, target value와의 차이를 구함. 
#이 차이의 값을 M이라고 하면, M과 같은 value를 list에서 찾으면 되는 거임. 
#왜냐하면 