class Container:
    origin_country: str
    destination_country: str
    container_number: str
    weight: int
    cargo: str
    company_name: str
    company_origin_country: str
    cost: int

    def __init__(self, row: str):
        [self.origin_country, self.destination_country, data] = row.split("-")
        [self.container_number, weight, details, cost] = data.split("/")
        self.weight = int(weight)
        self.cost = int(cost)
        [self.cargo, company] = details.split("@")
        [self.company_name, self.company_origin_country] = company.split(".")

    @property
    def company(self) -> str:
        return self.company_name + "." + self.company_origin_country
