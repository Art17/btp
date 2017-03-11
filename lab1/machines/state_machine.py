from machines.machine import Machine, State
from abc import ABCMeta, abstractmethod
from machines.machine import Event


class FsmState:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def a(self, context):
        pass

    @abstractmethod
    def b(self, context):
        pass

    @abstractmethod
    def c(self, context):
        pass

    @abstractmethod
    def d(self, context):
        pass


class Q0(FsmState):
    def __init__(self):
        super().__init__()

    def name(self):
        return 'q0'

    def a(self, context):
        context.set_state(Q1())

    def b(self, context):
        context.set_state(Err())

    def c(self, context):
        context.set_state(Err())

    def d(self, context):
        context.set_state(Err())


class Q1(FsmState):
    def __init__(self):
        super().__init__()

    def name(self):
        return 'q1'

    def a(self, context):
        context.set_state(Q2())

    def b(self, context):
        context.set_state(Q1())

    def c(self, context):
        context.set_state(Err())

    def d(self, context):
        context.set_state(Err())


class Q2(FsmState):
    def __init__(self):
        super().__init__()

    def name(self):
        return 'q2'

    def a(self, context):
        context.set_state(Err())

    def b(self, context):
        context.set_state(Err())

    def c(self, context):
        context.set_state(Q3())

    def d(self, context):
        context.set_state(Err())


class Q3(FsmState):
    def __init__(self):
        super().__init__()

    def name(self):
        return 'q3'

    def a(self, context):
        context.set_state(Q4())

    def b(self, context):
        context.set_state(Err())

    def c(self, context):
        context.set_state(Err())

    def d(self, context):
        context.set_state(Err())


class Q4(FsmState):
    def __init__(self):
        super().__init__()

    def name(self):
        return 'q4'

    def a(self, context):
        context.set_state(Q5())

    def b(self, context):
        context.set_state(Err())

    def c(self, context):
        context.set_state(Err())

    def d(self, context):
        context.set_state(Q4())


class Q5(FsmState):
    def __init__(self):
        super().__init__()

    def name(self):
        return 'q5'

    def a(self, context):
        pass

    def b(self, context):
        pass

    def c(self, context):
        pass

    def d(self, context):
        pass


class Err(FsmState):
    def __init__(self):
        super().__init__()

    def name(self):
        return 'err'

    def a(self, context):
        pass

    def b(self, context):
        pass

    def c(self, context):
        pass

    def d(self, context):
        pass


class StateMachine(Machine):
    def __init__(self):
        super().__init__()

        self.localFsmState = Q0()

    def set_state(self, state):
        self.localFsmState = state
        self.update_parent_state()

    def reset(self):
        super().reset()
        self.localFsmState = Q0()

    def a(self):
        self.localFsmState.a(self)

    def b(self):
        self.localFsmState.b(self)

    def c(self):
        self.localFsmState.c(self)

    def d(self):
        self.localFsmState.d(self)

    def update_parent_state(self):
        if self.localFsmState.name() == 'q0':
            self.currentState = State.q0
        elif self.localFsmState.name() == 'q1':
            self.currentState = State.q1
        elif self.localFsmState.name() == 'q2':
            self.currentState = State.q2
        elif self.localFsmState.name() == 'q3':
            self.currentState = State.q3
        elif self.localFsmState.name() == 'q4':
            self.currentState = State.q4
        elif self.localFsmState.name() == 'q5':
            self.currentState = State.q5
        elif self.localFsmState.name() == 'err':
            self.currentState = State.Err

    def update_local_state(self):
        if self.currentState == State.q0:
            self.localFsmState = Q0()
        elif self.currentState == State.q1:
            self.localFsmState = Q1()
        elif self.currentState == State.q2:
            self.localFsmState = Q2()
        elif self.currentState == State.q3:
            self.localFsmState = Q3()
        elif self.currentState == State.q4:
            self.localFsmState = Q4()
        elif self.currentState == State.q5:
            self.localFsmState = Q5()
        elif self.currentState == State.Err:
            self.localFsmState = Err()

    def handle_event(self, e):
        self.update_local_state()
        if e == Event.A:
            self.a()
        elif e == Event.B:
            self.b()
        elif e == Event.C:
            self.c()
        elif e == Event.D:
            self.d()
        else:
            self.localFsmState = Err()
        self.update_parent_state()

        return self.currentState == State.Err
