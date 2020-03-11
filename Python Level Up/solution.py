import os
from Node import Node
from typing import List, Tuple


def get_ans_for_file(path: str) -> Tuple[int, List[Node]]:
    n = Node()
    n.from_file(path)
    l = n.shortest_path()
    return l[0], Node.pathToInts(l[1])
    # return (0, [])


directory = "tests/"


for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        l, path = get_ans_for_file(directory + filename)
        print(filename, "Suma:", l, "Ścieżka:", ";".join(list(map(str, path))))
