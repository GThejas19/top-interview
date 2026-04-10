class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        
        while i < len(words):
            # Find how many words fit in the line
            line_len = len(words[i])
            j = i + 1
            
            while j < len(words) and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1
            
            num_words = j - i
            total_spaces = maxWidth - line_len
            
            # Last line OR single word → left justified
            if j == len(words) or num_words == 1:
                line = words[i]
                for k in range(i + 1, j):
                    line += " " + words[k]
                
                # Fill remaining spaces at the end
                line += " " * (maxWidth - len(line))
            
            else:
                spaces_between = total_spaces // (num_words - 1)
                extra_spaces = total_spaces % (num_words - 1)
                
                line = ""
                for k in range(i, j - 1):
                    line += words[k]
                    # Add spaces
                    spaces = spaces_between + (1 if k - i < extra_spaces else 0)
                    line += " " * spaces
                
                line += words[j - 1]  # last word
            
            res.append(line)
            i = j
        
        return res