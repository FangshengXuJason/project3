from typing import Tuple, List
from math import log
from datetime import datetime, timedelta
import time

RATE_LIFETIME = 1.5

class BellmanFord:
    def __init__(self, currencies):
        self.currencies = currencies
        self.size = len(currencies)

    def negate_logarithm_convertor(self, graph) -> List[List[float]]:
        """ log of each rate in graph and negate it"""
        result = [[]]
        for row in range(self.size):
            for col in range(self.size):
                if self.expired(graph[row][col][1]):
                    result[row][col] = float("Inf")
                else:
                    result[row][col] = graph[row][col][0]
        for row in result:
            print(row)
        return result


    def expired(self, publish_time: datetime):
        ts = datetime.utcnow()
        if ts - publish_time.total_seconds() >= RATE_LIFETIME:
            return True
        return False


    def arbitrage(self, currency_tuple: tuple, rates_matrix):
        """ Calculates arbitrage situations and prints out the details of this calculations"""

        trans_graph = self.negate_logarithm_convertor(rates_matrix)

        # Pick any source vertex -- we can run Bellman-Ford from any vertex and get the right result

        source = 0
        n = len(trans_graph)
        min_dist = [float('inf')] * n

        pre = [-1] * n

        min_dist[source] = source

        # 'Relax edges |V-1| times'
        for _ in range(n - 1):
            for source_curr in range(n):
                for dest_curr in range(n):
                    if min_dist[dest_curr] > min_dist[source_curr] + trans_graph[source_curr][dest_curr]:
                        min_dist[dest_curr] = min_dist[source_curr] + trans_graph[source_curr][dest_curr]
                        pre[dest_curr] = source_curr

        # if we can still relax edges, then we have a negative cycle
        for source_curr in range(n):
            for dest_curr in range(n):
                if min_dist[dest_curr] > min_dist[source_curr] + trans_graph[source_curr][dest_curr]:
                    print("\n"
                          "-log sum: ", min_dist[source_curr] + trans_graph[source_curr][dest_curr])
                    # negative cycle exists, and use the predecessor chain to print the cycle
                    print_cycle = [dest_curr, source_curr]
                    # Start from the source and go backwards until you see the source vertex again or any vertex that already exists in print_cycle array
                    while pre[source_curr] not in print_cycle:
                        print_cycle.append(pre[source_curr])
                        source_curr = pre[source_curr]
                    print_cycle.append(pre[source_curr])
                    print("Arbitrage Opportunity: ")
                    print(" --> ".join([self.currencies[p] for p in print_cycle[::-1]]))

# if __name__ == "__main__":
#     arbitrage(currencies, rates)

# Time Complexity: O(N^3)
# Space Complexity: O(N^2)