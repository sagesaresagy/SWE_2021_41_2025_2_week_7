from typing import List #그냥 파이썬에 내장된 자료구조라서 이렇게 한 거

def twoSum(nums: List[int], target: int) -> List[int]: #정수 리스트를 반환한다는 뜻
    #여기에 입력
    for i in range(len(nums)-1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            