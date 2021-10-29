#给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#返回滑动窗口中的最大值。
#示例 1：
#输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
#输出：[3,3,5,5,6,7]
#解释：
#滑动窗口的位置                最大值
#---------------               -----
#[1  3  -1] -3  5  3  6  7       3
# 1 [3  -1  -3] 5  3  6  7       3
# 1  3 [-1  -3  5] 3  6  7       5
# 1  3  -1 [-3  5  3] 6  7       5
# 1  3  -1  -3 [5  3  6] 7       6
# 1  3  -1  -3  5 [3  6  7]      7
#示例 2：
#输入：nums = [1], k = 1
#输出：[1]
#示例 3：
#输入：nums = [1,-1], k = 1
#输出：[1,-1]
#示例 4：
#输入：nums = [9,11], k = 2
#输出：[11]
#示例 5：
#输入：nums = [4,-2], k = 2
#输出：[4]
class MyQueue:
    def __init__(self):
        self.queue = []

    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.pop(0)

    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        result = []
        for i in range(k):
            que.push(nums[i])
        result.append(que.front())
        for i in range(k, len(nums)):
            que.pop(nums[i - k])
            que.push(nums[i])
            result.append(que.front())
        return result
