from pathlib import Path
from typing import Any
from collections.abc import Iterator

from scramble_history.twistytimer import parse_file

from bleanser.core.modules.extract import ExtractObjectsNormaliser


class Normaliser(ExtractObjectsNormaliser):
    def extract_objects(self, path: Path) -> Iterator[Any]:
        for solve in parse_file(path):
            yield int(solve.when.timestamp())


if __name__ == "__main__":
    Normaliser.main()
