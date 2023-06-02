from dataclasses import dataclass
from importlib import resources
from importlib.abc import Traversable

from joint_bert import data


RESOURCES = resources.files(data)

@dataclass
class Labels:
    slot: Traversable
    intent: Traversable

    @classmethod
    def from_directory(cls, folder):
        return cls(folder / "slot_label.txt", folder / "intent_label.txt")


LABELS = {corpus: Labels.from_directory(RESOURCES / corpus) for corpus in ("atis", "snips")}
