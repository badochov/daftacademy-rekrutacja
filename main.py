from Ship import Ship
from Container import Container
from typing import List
from collections import defaultdict
from math import ceil


def read_data(file_path: str) -> List[Ship]:
    with open(file_path, "r") as data_file:
        data = data_file.read()
        [ships_line, *containers_lines] = data.split("\n")
        ships_data = ships_line.split(";")
        ships: List[Ship] = []
        for ship_cell in ships_data:
            if ship_cell != "":
                ship = Ship(ship_cell)
                ships.append(ship)


        for containers_line in containers_lines:
            container_data = containers_line.split(";")
            for i, container_data in enumerate(container_data):
                if container_data != "":
                    container = Container(container_data)
                    ships[i].add_container(container)

        return ships


def to_country(ships: List[Ship], country: str) -> int:
    counter = 0
    for ship in ships:
        for container in ship.containers:
            if container.destination_country == country:
                counter += 1

    return counter


def class_name_that_carried_the_most(ships: List[Ship]) -> str:
    count = defaultdict(int)
    container_count = defaultdict(int)

    for ship in ships:
        class_name = ship.ship_class
        container_count[class_name] += len(ship.containers)
        count[class_name] += 1

    average_containers = {}
    for ship_class in container_count:
        average_containers[ship_class] = container_count[ship_class] / count[class_name]

    return max(average_containers, key=average_containers.get)


def average_weight_of_cargo_class(ships: List[Ship], cargo_class: str) -> int:
    count = 0
    average_weight = 0

    for ship in ships:
        for container in ship.containers:
            if container.cargo == cargo_class:
                count += 1
                average_weight = average_weight + (container.weight - average_weight) / count

    return ceil(average_weight)


def company_that_sends_max_amount_of_containers_by_country(ships: List[Ship], country: str) -> str:
    count = defaultdict(int)

    for ship in ships:
        for container in ship.containers:
            if container.company_origin_country == country:
                company_name = container.company_name
                count[company_name] += 1

    return max(count, key=count.get)


def company_that_exports_most(ships: List[Ship], country: str) -> str:
    count = defaultdict(int)
    origin_country = country.upper()

    for ship in ships:
        for container in ship.containers:
            if container.company_origin_country == country and container.origin_country == origin_country:
                company_name = container.company_name
                count[company_name] += 1

    return max(count, key=count.get)


ships_list = read_data("dane.csv")

print("Zadanie 2")
print(to_country(ships_list, "JP"))

print("Zadanie 3")
print(class_name_that_carried_the_most(ships_list))

print("Zadanie 4")
print(average_weight_of_cargo_class(ships_list, "X1"))

print("Zadanie 5")
print(company_that_sends_max_amount_of_containers_by_country(ships_list, "pl"))

print("Zadanie 6")
print(company_that_exports_most(ships_list, "de"))
