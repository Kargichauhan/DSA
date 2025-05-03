class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        time_to_left = [float('inf')] * n
        time_to_right = [float('inf')] * n
        result = ['.'] * n

        # Pass 1: simulate force from Right ('R')
        time = float('inf')
        for i in range(n):
            if dominoes[i] == 'R':
                time = 0
            elif dominoes[i] == 'L':
                time = float('inf')
            else:
                if time != float('inf'):
                    time += 1
            time_to_right[i] = time

        # Pass 2: simulate force from Left ('L')
        time = float('inf')
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                time = 0
            elif dominoes[i] == 'R':
                time = float('inf')
            else:
                if time != float('inf'):
                    time += 1
            time_to_left[i] = time

        # Decide final state for each domino
        for i in range(n):
            if time_to_left[i] < time_to_right[i]:
                result[i] = 'L'
            elif time_to_right[i] < time_to_left[i]:
                result[i] = 'R'
            else:
                result[i] = dominoes[i] if time_to_left[i] == float('inf') and time_to_right[i] == float('inf') else '.'

        return ''.join(result)