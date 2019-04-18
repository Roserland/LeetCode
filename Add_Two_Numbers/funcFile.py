class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def show(rsNode):
    result = ''
    currNode = rsNode
    while(currNode.next):
        result  = result + str(currNode.val)
        currNode = currNode.next
    result = result + str(currNode.val)
    print(result)
    return result

def generateNode(num):
    currNum = num
    rsNode = ListNode(num % 10)
    headNode = rsNode
    # print(rsNode.val)
    while((currNum // 10) != 0):
        # print(currNum)
        currNum = currNum // 10
        rsNode.next = ListNode((currNum % 10))
        rsNode = rsNode.next
        # print('rs:', rsNode.val)
    # rsNode.next = ListNode(currNum)
    return headNode


def reversStr(str_1):
    length = len(str_1)
    result = ''
    for i in range(1, length+1):
        # print(length - i)
        result = result + str_1[length - i]
        # print(result)
    return  result

# mmm = generateNode(281943)
# print(mmm.val)
# print(mmm.next.val)
# print(mmm.next.next.val)
# show(mmm)

