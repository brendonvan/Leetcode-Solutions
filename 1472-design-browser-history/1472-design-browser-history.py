class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.__step = 1

    def visit(self, url: str) -> None:
        while len(self.history) > self.__step:
            self.history.pop()
            
        self.history.append(url)
        self.__step = len(self.history)

    def back(self, steps: int) -> str:
        if self.__step - steps > 0:
            self.__step = self.__step - steps
        else:
            self.__step = 1

        return self.history[self.__step - 1]

    def forward(self, steps: int) -> str:
        if self.__step + steps < len(self.history):
            self.__step = self.__step + steps
        else:
            self.__step = len(self.history)
        
        return self.history[self.__step - 1]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)