# Given a string, find the length of the longest substring without repeating characters.

# first, find all the substring without repeating characters
# then, get the maxium length of them

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        if s_len < 2:         # empty str or just one character
            return s_len      #

        first = 0
        second = 0              # two pointers

        result = []             # to store the length
        while((first < s_len) & (second < s_len)):
            if s[second:second+1] not in s[first:second]:
                # s[second] not in the s[first:second]
                if second == s_len - 1:
                    # second pointer has been the last char position in the string
                    result.append(second - first + 1)
                    break
                second += 1

            else:
                print(second - first)
                result.append(second - first)
                first += 1
                if second == s_len-1:
                    return max(result)

                # 检测连续字符序列，并且重定位
                while(s[second] == s[second+1]):
                    second += 1
                    first = second
                    if second == s_len-1:
                        #末尾部分全是重复
                        print("max", max(result))
                        return max(result)
        return  max(result)


test_str = 'firstfindeallthestringoffthemainstringgingtext'
test_str = 'auqwertyyy'
# test_str = 'bbbbbbbbbbbbbbbbbbb'
# test_str = 'uu'
str_length = len(test_str)
# print(len(test_str))
# print(test_str[4])


# one solution from web
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=""
        count=0
        for i in s:
            res+=i
            if i in res[0:-1]:
                res=res[res[0:-1].rfind(i)+1::]
            if count<=len(res):
                count=len(res)
        return count





S = Solution()
rs = S.lengthOfLongestSubstring(test_str)
print(rs)

# print(len('   '))