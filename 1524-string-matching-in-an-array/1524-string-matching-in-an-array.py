class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        match_words = []

        for current_word_index in range(len(words)):
            for other_word_index in range(len(words)):
                if current_word_index == other_word_index:
                    continue

                if words[current_word_index] in words[other_word_index]:
                    match_words.append(words[current_word_index])
                    break

        return match_words
        
        