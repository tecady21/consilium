import dataclasses
import json


@dataclasses.dataclass
class Persona:
    name: str
    personality: str

    @staticmethod
    def load(path):
        with open(path, "r") as file:
            args = json.load(file)
            return Persona(**args)

    def save(self, path):
        with open(path, "w") as file:
            json.dump(dataclasses.asdict(self), file)
