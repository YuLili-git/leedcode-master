#给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
#示例 1:
#输入: nums = [1,1,1,2,2,3], k = 2
#输出: [1,2]
#示例 2:
#输入: nums = [1], k = 1
#输出: [1]
##################### solution 1 #####################
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        sort_dic = sorted(dic.items(), key=lambda d: d[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sort_dic[i][0])
        return res

##################### solution 2 #####################
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1

        pri_que = []
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)

        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result
