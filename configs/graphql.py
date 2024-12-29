# GraphQL Dependency Context
from typing import Any

from services import Service


async def get_graphql_context() -> dict[str, Service[Any, int]]:
    return {}
