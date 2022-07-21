class Counter:
    """Basic counter implementation"""
    def __init__(self) -> None:
        self.count = 0

    def increase(self):
        """Increase counter"""
        self.count += 1

    def decrease(self):
        """Decrease counter."""
        self.count -= 1
