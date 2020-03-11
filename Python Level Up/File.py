from typing import Generator


class File():
    @staticmethod
    def file_line_count(path: str) -> int:
        count = 0
        with open(path, "r") as F:
            for line in F:
                if line.strip():
                    count += 1
        return count

    @staticmethod
    def num_generator(path: str) -> Generator[int, None, None]:
        with open(path, "r") as F:
            for line in F:
                trimmed = line.strip()
                for num in trimmed.split():
                    yield int(num)
