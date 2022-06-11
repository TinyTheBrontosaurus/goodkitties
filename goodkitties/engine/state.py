from dataclasses import dataclass
from .board import board_v2


class Board:

    def __init__(self):
        self._graph = board_v2()
        self._kitties = None
        self._dog = None
        self._mice = None
        self._turn_order = None


@dataclass
class TurnStage:
    stagei: int = -1
    kitty_stagei: int = -1
    actions_left: int = -1
    kitty_count: int = -1


class TurnOrder:

    stages = ["supply", "mice", "kitties", "dog"]
    #kitty_order = ["draw", "check cleanliness", "actions", "increase dirtiness", "discard"]
    kitty_stages = ["actions"]
    actions_per_turn = 4

    def __init__(self):
        self.stagei = -1
        self.kitty_stagei = -1
        self.actions_left = -1
        self.kitty_count = 4

    def __iter__(self):
        self.stagei = 0
        self.kittyi = -1
        self.actions_left = -1
        return self

    def __next__(self):
        if self.stage == "N/A":
            raise StopIteration

        if not self.is_kitty_turn:
            self.stagei += 1
            if self.is_kitty_turn:
                self.kittyi = 0
                self.actions_left = self.actions_per_turn
        else:
            if self.actions_left > 0:
                self.actions_left -= 1
            else:
                self.kittyi += 1
                self.actions_left = self.actions_per_turn
                if self.kittyi >= self.kitty_count:
                    # Kitties are done
                    self.stagei += 1
                    self.kittyi = -1
                    self.actions_left = -1

        raise StopIteration

    @property
    def stage(self):
        if 0 <= self.stagei <= len(self.stages):
            return self.stages[self.stagei]
        else:
            return "N/A"

    @property
    def is_kitty_turn(self):
        return self.stage == "kitties"

    @property
    def kitty_stage(self):
        if 0 <= self.kitty_stagei <= len(self.kitty_stages):
            return self.kitty_stages[self.kitty_stagei]
        else:
            return "N/A"

    @property
    def kitty_actions_left(self):
        if not self.is_kitty_turn:
            return 0
        return self.actions_left


@dataclass
class Entity:
    def __init__(self):
        self._location = None
        self._name = None