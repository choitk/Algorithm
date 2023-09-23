class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = j = 0
        
        while i < len(word1) and j < len(word2):
            result.append(word1[i])  # word1의 문자를 결과 리스트에 추가합니다.
            result.append(word2[j])  # word2의 문자를 결과 리스트에 추가합니다.
            i += 1
            j += 1
        
        # 남은 문자가 있는 경우 word1의 남은 문자를 결과 리스트에 추가합니다.
        while i < len(word1):
            result.append(word1[i])
            i += 1
        
        # 남은 문자가 있는 경우 word2의 남은 문자를 결과 리스트에 추가합니다.
        while j < len(word2):
            result.append(word2[j])
            j += 1
        
        return ''.join(result)

# Example usage:
solution = Solution()
word1 = "abc"
word2 = "pqr"
merged = solution.mergeAlternately(word1, word2)
print(merged)  # 출력: "apbqcr"
