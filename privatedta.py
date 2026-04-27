class myclass:
    __privatevar=27
    def __privatemethod(self):
        print("im inside myclass")
    def hello(self):
        print("this is the private variable",myclass.__privatevar)
    def bye(self):
        myclass.__privatemethod(self)
fooo=myclass()
fooo.hello()
fooo.bye()