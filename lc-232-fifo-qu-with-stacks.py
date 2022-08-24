class MyQueue:

    def __init__(self):
        self.qu = []

    def push(self, x: int) -> None:
        self.qu.append(x)

    def pop(self) -> int:
        pop = self.qu[0]
        self.qu = self.qu[1:]
        return pop

    def peek(self) -> int:
        return self.qu[0]

    def empty(self) -> bool:
        return False if self.qu else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

#damn that was Freelo af