class WordDistance:
    # to-do : check

    '''
    1. Shortest distance between 2 string from array
    
    2. dis = i, j --> abs(i-j)

    3. two pointer

    ["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]

output - [null, 3, 1]


    '''

    def __init__(self, wordsDict: List[str]):
        self.word_indices = defaultdict(list)

        # Store the index positions of each word in a dictionary
        for index, word in enumerate(wordsDict):
            self.word_indices[word].append(index)

        # Ensure all index lists are sorted for efficient binary search
        for indices in self.word_indices.values():
            indices.sort()

        
        

        

    def shortest(self, word1: str, word2: str) -> int:
        # Retrieve sorted index lists
        word1_list, word2_list = self.word_indices[word1], self.word_indices[word2]

        # Initialize minimum distance as infinity
        min_dist = math.inf

        # Iterate through occurrences of word1 and use binary search to find the closest word2 occurrence
        for word1_index in word1_list:
            # Use binary search to find the closest insertion point in word2_list
            pos = bisect.bisect_left(word2_list, word1_index)

            # Check the closest elements around the insertion position
            if pos > 0:
                min_dist = min(min_dist, abs(word2_list[pos - 1] - word1_index))
            if pos < len(word2_list):
                min_dist = min(min_dist, abs(word2_list[pos] - word1_index))

            # Early exit if the shortest possible distance (1) is found
            if min_dist == 1:
                return 1

        return min_dist

        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)