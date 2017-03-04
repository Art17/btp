from machines.machine import Machine, State, Event


class TableMachine(Machine):

    table = [ [State.q1, State.q2, State.Err, State.q4, State.q5],
              [State.Err, State.q1, State.Err, State.Err, State.Err],
              [State.Err, State.Err, State.q3, State.Err, State.Err],
              [State.Err, State.Err, State.Err, State.Err, State.q4]]

    def __init__(self):
        super().__init__()

    def handle_event(self, event):
        try:
            self.currentState = self.table[event.value][self.currentState.value]
        except:
            self.currentState = State.Err
        return self.currentState == State.Err

