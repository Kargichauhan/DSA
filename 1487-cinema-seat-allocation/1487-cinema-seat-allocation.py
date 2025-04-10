class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        '''
        rows of seats -> 1 to n 

        labelled row -> 1 to 1o

        reservedseats[i] = 3,8 -> row 3 labelled 8 => booked

        find 4 person groups -> adjacent seat in one single row

        aisle not consider 

        Technique: masking -> uses bitwise operations -> binary 0 or 1 
        to how know if it is reseved or not reserved
        masking each row -> in binary or bitwise operation
        iterate each masked row, and verify
        '''

        # building the reserved seat masks:
        d = collections.defaultdict(int)

        for(r,c) in reservedSeats:  # d holding each rows reservation 
            d[r] |= 1 << (c-1)
            # 1<< c -> sets the (c-1)th bit to 1 meaning c seat is reserved 
            # |= ==> update the reserved bits for row r 



        ans = 2 * n # assuming tow groups per roe

        for r, binary in d.items():
            if binary | 513 == 513:
                continue
            elif binary | 543 == 543 or binary | 903 == 903 or binary | 993 == 993:
                ans -= 1
            else: ans -= 2

            '''

            If binary | 543 == 543, seats [2-5] are all free (at least 1 group possible).
            If binary | 903 == 903, seats [4-7] are all free (at least 1 group possible).
            If binary | 993 == 993, seats [6-9] are all free (at least 1 group possible).
            
            Seats 2-5  → 0000011110 (binary) = 30
            Seats 4-7  → 0001111000 (binary) = 120
            Seats 6-9  → 0111100000 (binary) = 480

            number	Binary Representation	Meaning (which bits must be empty)
                513	1000000001	Seats 2-9 are free (only seat 1 & 10 possibly reserved)
                543	1000011111	Seats 2-5 must be free
                903	1110000111	Seats 4-7 must be free
                993	1111100001	Seats 6-9 must be free

            '''


        return ans


        