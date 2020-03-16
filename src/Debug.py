class FalseChannel:
    async def send(self, message):
        print(message)

class FalseMessage:
    def __init__(self):
        self.channel = FalseChannel()
