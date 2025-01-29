class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:

            if stack and stack[-1] > 0 and asteroid < 0:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()

                if stack and stack[-1] > abs(asteroid):
                    continue

                elif stack and stack[-1] == abs(asteroid):
                    stack.pop()

                    continue

            stack.append(asteroid)
        return stack


    