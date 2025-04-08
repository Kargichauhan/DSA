class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        '''
        stack 
        res [size of array] -> to store exculsive time 
        track [prev_time] -> last time a fn was executing?
        parse -> log into function_id, type, (start/end) and timestamp

        if it is start: 
            if fn -> stack not empty 

            res[stack[-1]] += timestamp - prev_time

            update => prev_time = timestamp


        '''

        #initialize a result array to store exclusive time

        res = [0] * n

        # stack to simulate fn call stack 
        stack = []

        #keep track of last recorded timestamp
        prev_time = 0 


        #process each log entry
        for log in logs:
            #split log into fn ID + event type and timestamp
            func_id, typ,time = log.split(":")
            func_id = int(func_id)
            time = int(time)


            if typ == "start":
                if stack:
                    res[stack[-1]] += time - prev_time

                stack.append(func_id)
                prev_time = time


            else:
                res[stack.pop()] += time - prev_time + 1

                prev_time = time + 1

        return res
        
        

        