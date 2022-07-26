from counter import Counter
from utils import Func

INCREASE = "i"
DECREASE = "d"
QUIT = "q"


class ActionsTracker:
    """Action tracking implementation."""
    def __init__(self) -> None:
        self.actions = []
        self.actionsResult = []

    def printAll(self,actions,result):
        """Print all actions and their result."""
        aux = 0
        print("pribando results", self.actionsResult)
        for action in actions:
            print("compruebo ")
            aux += 1
            print(f"Action: {action} result: {self.actionsResult}")

    def track(self, action, result):
        """Track action and result."""
        print("estoy en track", action, result)
        self.actions.append(action)
        print('imprimo action', self.actions)
        self.actionsResult.append(result)
        print("imprimo actions result", self.actionsResult)


class CounterWithTrackerProgram:
    """A counter program with action tracking builtin ."""
    counter = Counter()
    running = True
    actions = {
        INCREASE: Func("action", {"action": "increase"}),
        DECREASE: Func("action", {"action": "decrease"}),
        QUIT: Func("quit")
    }

    @classmethod
    def action(cls, action: str):
        """Process action."""
        getattr(cls.counter, action)()
        print("entra en action tracker", cls.actionsTracker.track(action.upper(), cls.counter.count) )
        cls.actionsTracker.track(action.upper(), cls.counter)
        print(f"Counter is now {cls.counter.count}")

    @classmethod
    def quit(cls):
        """Process quit."""
        cls.running = False

    @classmethod
    def _cls_action_from_user_input(cls) -> Func:
        cls_action = None
        while not cls_action:
            i = input("Input \"i\" for \"increase\", \"d\" for \"decrease\" and \"q\" for \"quit\": ")
            try:
                cls_action = cls.actions[i]
            except:
                print("enter proper value")

        return cls_action

    @classmethod
    def print_summary(cls):
        """Print summary."""
        print("---- Counter -----:")
        print(f"Value: {cls.counter.count}")
        print("---- Summary of actions -----:")
        print("en print sumary ", cls.counter.count)
        cls.actionsTracker.printAll(cls.actions,)

    @classmethod
    def run(cls):
        """Run the program."""
        while CounterWithTrackerProgram.running:
            cls.actionsTracker = ActionsTracker()
            cls_action = CounterWithTrackerProgram._cls_action_from_user_input()
            action = getattr(cls, cls_action.method)
            action(**cls_action.payload)

        if cls.actions:
            cls.print_summary()



if __name__ == '__main__':
    CounterWithTrackerProgram.run()