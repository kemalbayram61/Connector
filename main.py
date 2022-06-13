from interfaces.HTTPMethods         import HTTPMethods
from objects.Application            import Application
from objects.HTTPRequestConnector   import HTTPRequestConnector
from objects.Connector              import Connector
from objects.KNode                  import KNode
from objects.MongoConnector         import MongoConnector

if __name__ == '__main__':
    application           = Application("1","Application1", "Application1")
    #uRule
    #uruleMongo            = MongoConnector("mongodb+srv:","Database", "Collection")
    #uruleMongoCon         = Connector("1", "uruleConnector", "uruleConnector", "db")
    #uruleMongoCon.content = uruleMongo
    #uruleNode             = KNode(uruleMongoCon)
    #application.connectorList.append(uruleNode)
    #get
    getConnectorContent  = HTTPRequestConnector("https://w3schools.com", HTTPMethods.GET)
    getConnector         = Connector("2", "findevConnector", "findevConnector", "db")
    getConnector.content = getConnectorContent
    getNode              = KNode(getConnector)
    application.connectorList.append(getNode)
    #post
    postData             = {"name": "kemal", "code": 61}
    postConnectorContent  = HTTPRequestConnector("https://w3schools.com", HTTPMethods.POST, postData)
    postConnector         = Connector("2", "findevConnector", "findevConnector", "db")
    postConnector.content = postConnectorContent
    postNode              = KNode(postConnector)
    application.connectorList.append(postNode)
    application.checkConnectors()
    application.runConnectors()
