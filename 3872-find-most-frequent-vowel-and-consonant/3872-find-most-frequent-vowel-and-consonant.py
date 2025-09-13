class Solution:
    def maxFreqSum(self, s: str) -> int:

        vowels = "aeiou"
        
        
        vowel_counts = collections.Counter(c for c in s if c in vowels)
        consonant_counts = collections.Counter(c for c in s if c not in vowels)
        
        
        max_vowel_freq = max(vowel_counts.values()) if vowel_counts else 0
        max_consonant_freq = max(consonant_counts.values()) if consonant_counts else 0
        
        return max_vowel_freq + max_consonant_freq  