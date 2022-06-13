from KList import KList

class Application:
    id          = None
    name        = None
    description = None

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.connectorList = KList()

    def checkConnectors(self) ->bool:
        node = self.connectorList.head
        while(node):
            if(node.data.content.connect() == False):
                return False
            node = node.after
        return True

    def runConnectors(self):
        node = self.connectorList.head
        while(node):
            node.data.content.run()
            node = node.after
        return True
