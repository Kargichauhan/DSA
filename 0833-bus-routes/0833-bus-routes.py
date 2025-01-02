class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        '''
        bus stops -> bus stops sequence
        [1,2,7] -> 1,2,7,1,2,7
        [3,6,7] -> 3,6,7,3,6,7



        bus stop -> min buses to reach 
        1 - 0
        2- inf 
    
        '''
        if source == target:
            return 0

        adjList = {}
        for bus, route in enumerate(routes):
            for stop in route:
                if stop in adjList:
                    adjList[stop].add(bus)
                else:
                    adjList[stop] = {bus}

        if source not in adjList:
            return -1
        
        visitedStops = set()
        visitedBuses = set()
        queue = deque()

        visitedStops.add(source)
        queue.append(source)

        numStops = 0

        while queue:
            lenQ = len(queue)

            for _ in range(lenQ):
                currStop = queue.popleft()
                if currStop == target:
                    return numStops

                for bus in adjList[currStop]:
                    if bus not in visitedBuses:
                        for stop in routes[bus]:
                            if stop not in visitedStops:
                                visitedStops.add(stop)
                                queue.append(stop)

                        visitedBuses.add(bus)
                        
            numStops += 1

        return -1