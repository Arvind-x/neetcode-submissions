class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        k = [(position[i], speed[i]) for i in range(len(position))]
        k = sorted(k, key=lambda time: time[0])

        times = [(target - k[i][0])/k[i][1] for i in range(len(position))]
        fleets = 0
        while times:
            top = times.pop(-1)
            while times and times[-1] <= top:
                times.pop(-1)
            fleets += 1
        return fleets

        
