class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.build(0, 0, len(arr) - 1)
    
    def build(self, node, start, end):

        if start == end:
            self.tree[node] = self.arr[start]
            return
        
        mid = start + (end - start)//2
        left_child = 2*node + 1
        right_child = 2*node + 2
        self.build(left_child, start, mid)
        self.build(right_child, mid + 1, end)
        self.tree[node] = self.tree[left_child] + self.tree[right_child]


    def update(self, node, start, end, index, value):

        if start == end:
            self.arr[index] = value
            self.tree[node] = value
            return 
        
        mid = start + (end - start)//2
        left_child = 2*node + 1
        right_child = 2*node + 2

        if start <= index <= mid:
            self.update(left_child, start, mid, index, value)
        
        else:
            self.update(right_child, mid + 1, end, index, value)
        
        self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def query(self, node, start, end, left, right):

        if start > right or end < left:
            return 0
        
        elif left <= start and end <= right:
            return self.tree[node]
        
        mid = start + (end - start)//2
        left_child = 2*node + 1
        right_child = 2*node + 2
        left_sum = self.query(left_child, start, mid, left, right)
        right_sum = self.query(right_child, mid + 1, end, left, right)

        return left_sum + right_sum

class NumArray:

    def __init__(self, nums: List[int]):
        
        self.seg_tree = SegmentTree(nums)
        self.start = 0
        self.end = len(nums) - 1
        

    def update(self, index: int, val: int) -> None:
        self.seg_tree.update(0, self.start, self.end, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.seg_tree.query(0, self.start, self.end, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)