from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        
        from collections import Counter
        word_map = Counter(words)
        result = []
        
        # Try all possible starting offsets
        for i in range(word_len):
            left = i
            curr_count = Counter()
            count = 0
            
            # Move window in steps of word_len
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]
                
                if word in word_map:
                    curr_count[word] += 1
                    count += 1
                    
                    # If more than expected, shrink window
                    while curr_count[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    # If valid window found
                    if count == word_count:
                        result.append(left)
                else:
                    # Reset window
                    curr_count.clear()
                    count = 0
                    left = right + word_len
        
        return result