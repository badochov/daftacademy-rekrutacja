from __future__ import annotations
from queue import Queue, PriorityQueue
import re
from File import File
from typing import Dict, List


class Node():
    left: Node = None
    right: Node = None
    value: int

    def __init__(self, num: int = 0):
        super().__init__()
        self.value = num

    def __eq__(self, value: Node) -> bool:
        return self is value

    def __hash__(self) -> int:
        return id(self)

    def __lt__(self, value: Node):
        return hash(self) < hash(value)

    def init_tree(self, height: int) -> None:
        if height < 1:
            raise Exception
        elif height == 1:
            return
        else:
            if self.left == None:
                self.left = Node()
                self.left.init_tree(height-1)

            self.right = Node()
            self.right.left = self.left.right
            self.right.init_tree(height-1)

    def from_file(self, path: str) -> Node:
        count = File.file_line_count(path)
        self.init_tree(count)
        q = Queue()
        q.put(self)
        nums_gen = File.num_generator(path)
        vis = {}
        while not q.empty():
            n = q.get()
            if vis.get(n, False):
                continue
            n.value = next(nums_gen)
            vis[n] = True

            if n.left is not None:
                q.put(n.left)
            if n.right is not None:
                q.put(n.right)

    def dijkstra(self) -> {}:
        ans = {}
        pq = PriorityQueue()
        pq.put((0, self, ()))
        while not pq.empty():
            (dist, n, path) = pq.get()
            if n in ans:
                if ans[n][0] <= dist:
                    continue
            dist += n.value
            path += n,
            ans[n] = (dist, path)
            if n.left is not None:
                pq.put((dist, n.left, path))
            if n.right is not None:
                pq.put((dist, n.right, path))
        return ans

    def shortest_path(self) -> int:
        dists = self.dijkstra()
        min_dist = (-1, ())
        q = Queue()
        q.put(self)
        vis = {}
        while not q.empty():
            n = q.get()
            if vis.get(n, False):
                continue
            vis[n] = True
            if n.left is not None:
                q.put(n.left)
            if n.right is not None:
                q.put(n.right)
            if n.right is None or n.left is None:
                if min_dist[0] == -1:
                    min_dist = dists[n]
                elif min_dist[0] > dists[n][0]:
                    min_dist = dists[n]
        return min_dist

    def print_tree(self):
        q = Queue()
        q.put(self)
        vis = {}
        while not q.empty():
            n = q.get()
            if vis.get(n, False):
                continue
            vis[n] = True
            print(n.value)
            if n.left is not None:
                q.put(n.left)
            if n.right is not None:
                q.put(n.right)

    @staticmethod
    def pathToInts(path: List[Node]):
        return list(map(lambda n: n.value, path))


if __name__ == "__main__":
    n = Node()
    n.from_file("./tests/example.txt")
    # n.print_tree()
    l = n.shortest_path()
    l = l[0], Node.pathToInts(l[1])
    print(l)
