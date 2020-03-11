from Container import Container
from typing import List


class Ship:
    containers: List[Container]
    ship_id: int
    name: str
    ship_class: str

    def __init__(self, cell: str):
        split_cell = cell.split(": ")
        names_part = split_cell[1]
        split_names_part = names_part.split(" (")

        self.ship_id = int(split_cell[0])
        self.name = split_names_part[0]
        self.ship_class = split_names_part[1][0:-1]
        self.containers = []

    def add_container(self, container: Container) -> None:
        self.containers.append(container)
