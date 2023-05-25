'''
有n个硬币排成一排，每次要你从最左边或者最右侧拿出一个硬币。总共拿k次，写一个算法，使能拿到的硬币的和最大。
1 <= k <= n <= 100000
硬币的价值不大于10000

sample1:
输入： list = [5,4,3,2,1], k = 2,
输出：9
解释：从左边开始连取两个硬币即可。
sample2:
输入： list = [5,4,3,2,1,6], k = 3 
输出：15.
解释：从左边开始连取两个硬币,右边取一个即可。
'''

def pick_from_sides(a, k):
    list_sum = []
    tmp = 0
    for ele in a[0:]:
        tmp += ele
        list_sum.append(tmp)
    sum = list_sum[k - 1]
    for i in range(1, k):
        sum = max(list_sum[k - 1 - i] + list_sum[-1] - list_sum[-i-1], sum)
    return sum




if __name__ == '__main__':
    a = [1, 2, 100, 5, 5, 5, 7, 8, 9]
    k = 3
    sum = pick_from_sides(a, k)
    print(sum)



