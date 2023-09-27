#
# @lc app=leetcode id=880 lang=python3
#
# [880] Decoded String at Index
#


# @lc code=start
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # curr: encoded string
        # currSize: the size of encoded
        # we either parse a word or a number 2-9
        # 1. when we parse a word, update curr and currSize, k should be minus by len(word)
        # 2. when we parse a number x between 2-9, update curr and currSize,
        # k should be minus by currSize*(x-1)
        # when k is about to be less than zero, we know we are about to find the letter we want
        # return word[k-1]
        # we do this check in both case
        # if it's in "word" case, return word[count-1]
        # else, recursively call the function
        # s: curr+str(x-1), k: count

        # preprocess to array of word and num
        arr = []
        tmp = ""
        for char in s:
            if char.isnumeric():
                if tmp != "":
                    arr.append(tmp)
                tmp = ""
                arr.append(int(char))
            else:
                tmp += char
        if tmp != "":
            arr.append(tmp)

        # base case
        if k == 1:
            return s[0]
        if len(arr) == 1:
            return arr[0][k - 1]

        curr = ""
        currSize = 0
        count = k
        for wordOrNum in arr:
            if type(wordOrNum) is int:
                num = wordOrNum
                if count - (currSize * (num - 1)) <= 0:
                    return self.decodeAtIndex(curr + str(num - 1), count)
                count -= currSize * (num - 1)
                curr += str(num)
                currSize *= num
            else:
                word = wordOrNum
                curr += word
                currSize += len(word)
                if count - len(word) <= 0:
                    return word[count - 1]
                count -= len(word)


# @lc code=end
