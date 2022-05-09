import heapq

class MedianFinder:
    def __init__(self):
        self.left_heap = [] # instantiate left heap
        self.right_heap = [] # instantiate right heap
        heapq.heapify(self.left_heap)
        heapq.heapify(self.right_heap)

    def addNum(self, num):
        if len(self.left_heap) == 0 and len(self.right_heap) == 0:
            heapq.heappush(self.right_heap, num)
        else:
            if num < self.right_heap[0]:
                heapq.heappush(self.left_heap, -num)
            else:
                heapq.heappush(self.right_heap, num)
            # check for imbalance
            if len(self.left_heap) > len(self.right_heap) + 1:
                num = - heapq.heappop(self.left_heap)
                heapq.heappush(self.right_heap, num)
            if len(self.right_heap) > len(self.left_heap) + 1:
                num = heapq.heappop(self.right_heap)
                heapq.heappush(self.left_heap, -num)

    def findMedian(self):
        if len(self.left_heap) == 0 and len(self.right_heap) == 1:
            return self.right_heap[0]
        if len(self.left_heap) == 1 and len(self.right_heap) == 0:
            return -self.left_heap[0]
        if len(self.left_heap) == len(self.right_heap):
            return 0.5*(-self.left_heap[0] + self.right_heap[0])
        elif len(self.left_heap) > len(self.right_heap):
            return -self.left_heap[0]
        else:
            return self.right_heap[0]

    def insertSortedArray(self, nums, num):
        if len(nums) == 1:
            if nums[0] < num:
                nums += [num]
            else:
                nums = [num] + nums
            return nums
        if nums[-1] < num:
            nums += [num]
            return nums
        n = int(len(nums)/2)
        if nums[n-1] > num:
            nums = self.insertSortedArray(nums[:n], num) + nums[n:]
        else:
            nums = nums[:n] + self.insertSortedArray(nums[n:], num)
        return nums


if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(4)
    print(mf.findMedian())
    mf.addNum(2)
    print(mf.findMedian())
    mf.addNum(5)
    print(mf.findMedian())
    mf.addNum(3)
    print(mf.findMedian())
    mf.addNum(4.5)
    print(mf.findMedian())
