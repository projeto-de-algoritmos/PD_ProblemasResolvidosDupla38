class Solution(object):
    def findAnagrams(self, s, p):
        matched = 0 
        char_freq = {}
        start = 0
        res = []
        
        for char in p:
            if char not in char_freq:
                char_freq[char] = 0
            char_freq[char] += 1
            
        for end in range(len(s)):
            right_char = s[end]
            if right_char in char_freq:
                char_freq[right_char] -= 1
                if char_freq[right_char] == 0:
                    matched += 1
                
            if matched == len(char_freq):
                res.append(start)
                
            if end >= len(p)-1:
                left_char = s[start]
                if left_char in char_freq:
                    if char_freq[left_char] == 0:
                        matched -= 1
                    char_freq[left_char] += 1
                start += 1
                
        return res