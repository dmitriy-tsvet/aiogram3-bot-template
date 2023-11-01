from abc import ABCMeta, abstractmethod


class BaseDatabase(metaclass=ABCMeta):
    @property
    def name(self) -> str:
        return self.__class__.__name__.lower()

    @property
    @abstractmethod
    def interface(self) -> str:
        pass

    @abstractmethod
    def __str__(self):
        pass


class FileDatabase(BaseDatabase):
    def __init__(self, path):
        self.path = path

    @property
    def interface(self):
        return None

    def __str__(self):
        return f"{self.name}:///{self.path}"


class TransactionDatabase(BaseDatabase):
    def __init__(self, database_name: str, username: str, password: str, hostname: str, port: int):
        self.database_name = database_name
        self.username = username
        self.password = password
        self.hostname = hostname
        self.port = port

    @property
    @abstractmethod
    def interface(self) -> str:
        pass

    def __str__(self):
        return f"{self.name}+{self.interface}://{self.username}:{self.password}@" \
               f"{self.hostname}:{self.port}/{self.database_name}"


class AsyncDatabase(BaseDatabase):
    def __init__(self, database_name: str, username: str, password: str, hostname: str, port: int):
        self.database_name = database_name
        self.username = username
        self.password = password
        self.hostname = hostname
        self.port = port

    @property
    def name(self):
        return self.__class__.__name__.lower()[5:]

    @property
    @abstractmethod
    def interface(self) -> str:
        pass

    def __str__(self):
        return f"{self.name}+{self.interface}://{self.username}:{self.password}@" \
               f"{self.hostname}:{self.port}/{self.database_name}"