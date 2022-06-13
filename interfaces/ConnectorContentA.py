from abc import ABC, abstractmethod
class ConnectorContentA(ABC):
    @abstractmethod
    def connect(self) ->bool:
        pass

    @abstractmethod
    def run(self):
        pass