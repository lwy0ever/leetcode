class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        total = sum(distance)
        if start > destination:
            start,destination = destination,start
        return min(sum(distance[start:destination]),total - sum(distance[start:destination]))
        