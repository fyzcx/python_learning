import random


class Sort:
    def __init__(self, n, nums_range):
        self.n = n  # 排序的数目
        self.arr = []
        # self.arr = [3, 87, 2, 93, 78, 56, 61, 38, 12, 40]
        self.nums_range = nums_range
        self.random_nums()

    def random_nums(self):
        for i in range(self.n):
            self.arr.append(random.randint(0, self.nums_range - 1))

    def partition(self, left, right):
        arr = self.arr
        k = left
        for i in range(left, right):
            if arr[i] < arr[right]:  # 如果小于分割值，就交换
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quick_sort(self, left, right):
        if left < right:
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)  # 递归快排左边一半
            self.quick_sort(pivot + 1, right)  # 递归快排右边一半

    def adjust_max_heap(self, parent_pos, arr_len):
        """
        把某一棵子树调整为大根堆
        :param parent_pos: 要调整的位置
        :param arr_len: 列表的长度
        :return:
        """
        arr = self.arr
        dad = parent_pos
        son = 2 * dad + 1
        while son < arr_len:  # 儿子存在
            if son + 1 < arr_len and arr[son] < arr[son + 1]:  # 如果有右儿子且右儿子大于左儿子，则son指向右儿子
                son += 1
            if arr[dad] < arr[son]:  # 如果父节点小于儿子，则交换
                arr[dad], arr[son] = arr[son], arr[dad]  # 交换父子
                dad = son  # 继续调整下一层
                son = 2 * dad + 1
            else:
                break

    def heap_sort(self):
        arr = self.arr
        # 把列表调整为大根堆，self.n//2-1是最后一个父亲结点的下标值
        for parent_pos in range(self.n // 2 - 1, -1, -1):
            self.adjust_max_heap(parent_pos, self.n)
        for end_pos in range(self.n - 1, 0, -1):
            arr[end_pos], arr[0] = arr[0], arr[end_pos]  # 交换堆顶和最后一个元素
            self.adjust_max_heap(0, end_pos)  # 调整剩余元素为大根堆


if __name__ == '__main__':
    s = Sort(10, 100)
    print(s.arr)
    # s.quick_sort(0, s.n - 1)
    s.heap_sort()
    print(s.arr)
