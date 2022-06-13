from interfaces.ConnectorContentA import ConnectorContentA
class Connector:
    name = None
    id = None
    description = None
    brand = None
    content: ConnectorContentA = None

    def __init__(self, id, name, description, brand, content=None):
        self.id = id
        self.name = name
        self.description = description
        self.brand = brand
        self.content = content

    def __eq__(self, other):
        if (self.id == other.id and
                self.name == other.name and
                self.description == other.description and
                self.brand == other.brand and
                self.content == other.content):
            return True
        return False