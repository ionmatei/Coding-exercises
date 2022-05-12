class Solution:
    def isAlienSorted(self, words, order):
        # index the letter order
        letters = {order[i]: i for i in range(len(order))}
        for i in range(len(words)-1): #iterate through all consecutive words
            word1, word2 = words[i], words[i+1]
            j = 0
            while j < min(len(word1), len(word2)) and word1[j] == word2[j]:
                j += 1
            if j == len(word2) and j < len(word1): # word2 is a prefix of word1. thus must return False
                return False

            if j < min(len(word1), len(word2)) and letters[word1[j]] > letters[word2[j]]: # found a bad order
                return False
        return True


if __name__ == '__main__':
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    # words = ["word", "world", "row"]
    # order = "worldabcefghijkmnpqstuvxyz"
    # words = ["apple", "app"]
    # order = "abcdefghijklmnopqrstuvwxyz"
    words = ["hello", "hello"]
    order = "abcdefghijklmnopqrstuvwxyz"
    sol = Solution()
    print(sol.isAlienSorted(words, order))







