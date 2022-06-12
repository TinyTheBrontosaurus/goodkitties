import copy
from dataclasses import dataclass
from typing import Dict, Iterable, Iterator, Optional
from .board import board_v2


class Board:

    def __init__(self):
        self._graph = board_v2()
        self._kitties = None
        self._dog = None
        self._mice = None
        self._turn_order = None


class NestedPhase:
    def __init__(self, phases: Dict[str, Optional[Iterable]]):
        self._phases = phases
        self._key = ""
        self._child = None
        self._iter = None

    def __iter__(self):
        self._iter = self._phases.items().__iter__()
        return self

    def __next__(self):
        """
        Go to the next value. This phase does not go to the next phase until its child is done
        :return: the value of this and each nested iterator in a list
        """
        val = None
        repeat = True
        while repeat:
            repeat = False
            if self._child is None:
                self._key, self._child = self._iter.__next__()

                if self._child is not None:
                    self._child = self._child.__iter__()
            if self._child is not None:
                try:
                    val = self._child.__next__()
                except StopIteration:
                    self._child = None
                    repeat = True

        retval = [self._key]
        if val is not None:
            retval += val

        return retval


class Repeater:
    def __init__(self, parent: Iterable, child: Iterable):
        self._parent = parent
        self._child = child
        self._parent_iter: Iterator = None
        self._child_iter: Iterator = None

        self._parent_val = None

    def __iter__(self):
        self._parent_iter = self._parent.__iter__()
        self._parent_val = self._parent_iter.__next__()
        self._child_iter = self._child.__iter__()
        return self

    def __next__(self):
        repeat = True
        child_val = []
        while repeat:
            repeat = False
            try:
                child_val = self._child_iter.__next__()
            except StopIteration:
                # This would throw to end the iteration
                self._parent_val = self._parent_iter.__next__()
                self._child_iter = self._child.__iter__()
                repeat = True

        return self._parent_val + child_val


class Counter:
    def __init__(self, count):
        self._count = count

    def __iter__(self):
        return [[x] for x in range(1, self._count + 1)].__iter__()


def default_turn_phase(kitty_count=4):
    actions_per_turn = 4

    return NestedPhase({
        "re-supply": None,
        "mice": None,
        "kitties": Repeater([[x] for x in iter(range(1, kitty_count + 1))], NestedPhase({
            "draw": None,
            "check cleanliness": None,
            "actions": Counter(actions_per_turn),  # actions_per_turn),
            "increase dirtiness": None,
            "discard": None,
        })),
        "dog": None
    })


class TurnStage:

    def __init__(self, kitty_count=4):
        self.stages = default_turn_phase(kitty_count)
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
            if self.actions_left > 1:
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
        self._first = True

    def __iter__(self):
        self._first = True
        return self

    def __next__(self):
        if self._first:
            self._first = False
            self.stage.reset()
        else:
            if self.stage.stage == "N/A":
                raise StopIteration

            self.stage.next()

        return copy.copy(self.stage)


@dataclass
class Entity:
    def __init__(self):
        self._location = None
        self._name = None