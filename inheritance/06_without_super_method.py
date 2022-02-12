class A():
    def bar(self, string):
        print("Hi, I'm bar, inherited from A"+string)


class B(A):
    def baz(self):
        self.bar(" - called by baz in B")


B().baz()