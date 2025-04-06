# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    
    def cleanRoom(self, robot):
        # Directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(x, y, d):
            robot.clean()
            visited.add((x, y))

            for i in range(4):
                new_d = (d + i) % 4
                dx, dy = directions[new_d]
                new_x = x + dx
                new_y = y + dy

                if (new_x, new_y) not in visited:
                    if robot.move():
                        backtrack(new_x, new_y, new_d)
                        go_back()
                robot.turnRight()

        backtrack(0, 0, 0)






        #going clockwise 

        directions = [(-1,0), (0,1),(1,0),(0,-1)]

        visited = set()

        backtrack(0,0,0)





        