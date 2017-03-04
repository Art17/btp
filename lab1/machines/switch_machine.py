from machines.machine import Machine, State, Event


class SwitchMachine(Machine):
    def __init__(self):
        super().__init__()

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