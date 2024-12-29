from abc import abstractmethod
from typing import Generic, TypeVar

# Type definition for Model
M = TypeVar("M")

# Type definition for Unique Id
K = TypeVar("K")

#################################
# Abstract Class for Service #
#################################


class Service(Generic[M, K]):
    # Create a new instance of the Model
    @abstractmethod
    def create(self, instance: M) -> M:
        pass

    # Delete an existing instance of the Model
    @abstractmethod
    def delete(self, svc_id: K) -> None:
        pass

    # Fetch an existing instance of the Model by it's unique Id
    @abstractmethod
    def get(self, svc_id: K) -> M:
        pass

    # lists all existing instance of the Model
    @abstractmethod
    def list_items(
        self,
        name: str | None,
        page_size: int,
        start_index: int,
    ) -> list[M]:
        pass

    # Updates an existing instance of the Model
    @abstractmethod
    def update(self, svc_id: K, instance: M) -> M:
        pass
