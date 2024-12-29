from abc import abstractmethod
from typing import Generic, TypeVar

# Type definition for Model
M = TypeVar("M")

# Type definition for Unique Id
K = TypeVar("K")

#################################
# Abstract Class for Repository #
#################################


class RepositoryMeta(Generic[M, K]):
    # Create a new instance of the Model
    @abstractmethod
    def create(self, instance: M) -> M:
        pass

    # Delete an existing instance of the Model
    @abstractmethod
    def delete(self, repository_id: K) -> None:
        pass

    # Fetch an existing instance of the Model by it's unique Id
    @abstractmethod
    def get(self, repository_id: K) -> M:
        pass

    # lists all existing instance of the Model
    @abstractmethod
    def list_items(
        self, name: str | None, limit: int | None, start: int | None
    ) -> list[M]:
        pass

    # Updates an existing instance of the Model
    @abstractmethod
    def update(self, repository_id: K, instance: M) -> M:
        pass
