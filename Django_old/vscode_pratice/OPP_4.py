class Person():

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def hello(self):
        print("hello!")

    def report(self):
        print(f"I am {self.first_name} {self.last_name}")

class Agent(Person):

    def __init__(self,first_name,last_name,code_name):
        Person.__init__(self,first_name,last_name)
        self.code_name = code_name

    def report(self):
        print(f"I am {self.code_name}!")

    def reveal(self,passcode):

        if passcode == 123:
            print("I am a secret agent!")
        else:
            self.report()

x = Agent("John","smith","mr.X")

x.reveal(1243)