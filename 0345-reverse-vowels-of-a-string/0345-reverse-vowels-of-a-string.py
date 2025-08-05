class Solution:
    def reverseVowels(self, s: str) -> str:

        s = list(s)

        # These are our fairy letters
        vowels = set("aeiouAEIOU")

        # Left finger and right finger
        left, right = 0, len(s) - 1

        # Keep going until fingers meet
        while left < right:
            # If left is not a vowel, move right
            if s[left] not in vowels:
                left += 1
            # If right is not a vowel, move left
            elif s[right] not in vowels:
                right -= 1
            else:
                # Both are vowels — let's swap!
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        # Join the letters back into a string and return
        return "".join(s)
