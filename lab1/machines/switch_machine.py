from enum import Enum


class Event(Enum):
    A, B, C, D, Any = range(5)


class State(Enum):
    q0, q1, q2, q3, q4, q5, Err = range(7)


class SwitchMachine:
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

    def handle_event(self, event):
        if event == Event.Any:
            self.currentState = State.Err
        elif self.currentState == State.q0:
            if event == Event.A:
                self.currentState = State.q1
            else:
                self.currentState = State.Err
        elif self.currentState == State.q1:
            if event == Event.A:
                self.currentState = State.q2
            elif event == Event.B:
                self.currentState = State.q1
            else:
                self.currentState = State.Err
        elif self.currentState == State.q2:
            if event == Event.C:
                self.currentState = State.q3
            else:
                self.currentState = State.Err
        elif self.currentState == State.q3:
            if event == Event.A:
                self.currentState = State.q4
            else:
                self.currentState = State.Err
        elif self.currentState == State.q4:
            if event == Event.A:
                self.currentState = State.q5
            elif event == Event.D:
                self.currentState = State.q4
            else:
                self.currentState = State.Err
        return self.currentState == State.Err