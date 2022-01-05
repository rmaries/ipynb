class OptimalGolf(object):
    def minStrokes(self, D, clubLo, clubHi):
        max_distance = max(clubHi)
        #print(max_distance)
        min_distance = min(clubLo)
        #print(min_distance)
        excess_distance = D % max_distance
        if excess_distance == 0:
            return (D/max_distance)
        elif D < min_distance:
            return 2
        else:
            return (D//max_distance)+1

#print(OptimalGolf.minStrokes(D = 7, clubLo = (2,), clubHi = (2,)))
#print(OptimalGolf.minStrokes(D = 47, clubLo = (5, 4, 2), clubHi = (5, 7, 10)))