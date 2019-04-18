# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from funcFile import *

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

    # first: the length of the two num is not equal
    # then:  how to get the num, and how to get the result
    # third:
    # the last linknode value can't be zero, except 0 itself
    # 1. l1.next == None, l2.next == None
    # 2. l1.next == None, l2.next != None
    # Try the most rude solution? Reading the num all and then add it
    # 一起取点，先算完早停

        # def calcuSingleNum(l1, l2):
        #     sum1 = l1.val + l2.val
        #     if sum1 < 10:
        #         return ListNode(sum1)
        #     else:
        #         t = sum1 % 10  # 十位数
        #         s = sum1 - t  # 个位数
        #         rtNode = ListNode(t)
        #         rsNode = ListNode(s)
        #         rsNode.next = rtNode
        #     return rsNode

        sum0 = l1.val + l2.val                          # 得到第一个数相加
        jinwei_i = sum0 // 10                           # 得到第一个可能的进位，为0，或者大于0
        single_0 = sum0 % 10                            # 可以构建头节点
        rsNode = ListNode(single_0)
        headNode = rsNode                               # 保存头节点，不可更改

        curr1 = l1
        curr2 = l2
        # 处理二者相同长度的部分
        while((curr1.next != None) & (curr2.next != None)):                     # 两个数都不止一位
            curr1 = curr1.next
            curr2 = curr2.next
            sum_i = curr1.val + curr2.val + jinwei_i        # 两个个位 + 进位
            jinwei_i = sum_i // 10                          # 得到新的进位
            single_i = sum_i % 10                           # 得到结果的某个个位

            rsNode.next = ListNode(single_i)                # 构建新的节点，并连接
            rsNode = rsNode.next                            # 指向新的节点

        # 二者不同长度
        while((curr1.next == None) ^ (curr2.next == None)):  # 两个开始中有一个数只有一位，没有后一位
            if (curr2.next == None):
                curr1 = curr1.next
                sum_i = curr1.val + jinwei_i
                jinwei_i = sum_i // 10
                single_i = sum_i % 10

                rsNode.next = ListNode(single_i)
                rsNode = rsNode.next

                # 早停拼接
                rsNode.next = curr1.next

                # 此时还有进位数据
                while((jinwei_i == 1) & (rsNode.next != None)):                            # 进位只存在1，0两种情况
                    rsNode = rsNode.next
                    sum_i = rsNode.val + jinwei_i
                    jinwei_i = sum_i // 10
                    single_i = sum_i % 10
                    rsNode.val = single_i

                if ((jinwei_i == 1) & (rsNode.next == None)):
                    rsNode.next = ListNode(jinwei_i)

                return headNode

            elif (curr1.next == None):
                # 如果是第一个数字开始只剩一位， 将rsNode拼接到curr2上
                curr2 = curr2.next
                sum_i = curr2.val + jinwei_i
                jinwei_i = sum_i // 10
                single_i = sum_i % 10

                rsNode.next = ListNode(single_i)
                rsNode = rsNode.next

                # 早停拼接
                rsNode.next = curr2.next

                # 此时还有进位数据
                while ((jinwei_i == 1) & (rsNode.next != None)):  # 进位只存在1，0两种情况
                    rsNode = rsNode.next
                    sum_i = rsNode.val + jinwei_i
                    jinwei_i = sum_i // 10
                    single_i = sum_i % 10
                    rsNode.val = single_i

                if ((jinwei_i == 1) & (rsNode.next == None)):
                    rsNode.next = ListNode(jinwei_i)

                return headNode         # 二者不同


        # 最终处理，如果二者相同长度
        if((curr1.next == None) & (curr2.next == None)):
            # 此时进位只有两种情况， 0， 1
            if (jinwei_i == 1):
                rsNode.next = ListNode(1)
                return headNode
            else:
                return headNode








sltn = Solution()

num1 = 12345
num2 = 54321

test_L1 = generateNode(num1)
test_L2 = generateNode(num2)
result = sltn.addTwoNumbers(test_L1, test_L2)

result_str = show(result)
print(reversStr(result_str))
print(num1 + num2)



