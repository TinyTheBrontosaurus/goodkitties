import copy
from dataclasses import dataclass
from .board import board_v2


class Board:

    def __init__(self):
        self._graph = board_v2()
        self._kitties = None
        self._dog = None
        self._mice = None
        self._turn_order = None


class TurnStage:
    stages = ["supply", "mice", "kitties", "dog"]
    #kitty_order = ["draw", "check cleanliness", "actions", "increase dirtiness", "discard"]
    kitty_stages = ["actions"]
    actions_per_turn = 4

    def __init__(self, kitty_count=4):
        self.stagei: int = -1
        self._kittyi: int = -1
        self.kitty_stagei: int = -1
        self.actions_left: int = -1
        self.kitty_count: int = kitty_count

    def reset(self):
        self.stagei = 0
        self._kittyi = -1
        self.kitty_stagei = -1
        self.actions_left = -1

    @property
    def stage(self):
        if 0 <= self.stagei < len(self.stages):
            return self.stages[self.stagei]
        else:
            return "N/A"

    @property
    def is_kitty_turn(self):
        return self.stage == "kitties"

    @property
    def kittyi(self):
        return self._kittyi

    @property
    def kitty_stage(self):
        if 0 <= self.kitty_stagei < len(self.kitty_stages):
            return self.kitty_stages[self.kitty_stagei]
        else:
            return "N/A"

    @property
    def kitty_actions_left(self):
        if not self.is_kitty_turn:
            return 0
        return self.actions_left

    def next(self):
        if self.stage == "N/A":
            return

        if not self.is_kitty_turn:
            # Go to next stage
            self.stagei += 1
            # Adjust if it's now a kitty's turn
            if self.is_kitty_turn:
                self._kittyi = 0
                self.kitty_stagei = 0
                self.actions_left = self.actions_per_turn
        else:
            # If it is a kitty's turn, check the actions
            if self.actions_left > 0:
                self.actions_left -= 1
            else:
                self.kitty_stagei += 1
                self.actions_left = self.actions_per_turn
                if self.kitty_stagei >= self.kitty_count:
                    # Kitties are done
                    self.stagei += 1
                    self.kitty_stagei = -1
                    self.actions_left = -1


class TurnController:
    def __init__(self):
        self.stage = TurnStage()

    def __iter__(self):
        self.stage.reset()
        return self

    def __next__(self):
        self.stage.next()
        if self.stage.stage == "N/A":
            raise StopIteration

        return copy.copy(self.stage)


@dataclass
class Entity:
    def __init__(self):
        self._location = None
        self._name = None