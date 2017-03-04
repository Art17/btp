from enum import Enum
from abc import ABCMeta, abstractmethod


class Event(Enum):
    A, B, C, D, Any = range(5)


class State(Enum):
    q0, q1, q2, q3, q4, q5, Err = range(7)


class Machine:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.currentState = State.q0

    def reset(self):
        self.currentState = State.q0

    def recognize_event(self, ch):
        if ch == '^':
            yield Event.A
        if ch.isupper():
            yield Event.B
        if ch == '*':
            yield Event.C
        if ch != 'A' and ch != 'Z' and ch != '^' and not ch.isdigit():
            yield Event.D
        yield Event.Any

    def check_string(self, string):
        for ch in string:
            for e in self.recognize_event(ch):
                state = self.currentState
                if self.handle_event(e) and e != Event.Any:
                    self.currentState = state
                else:
                    break
        return self.currentState == State.q5

    @abstractmethod
    def handle_event(self, e):
        pass
