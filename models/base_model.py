from sqlalchemy.ext.declarative import declarative_base

from configs.database import engine

# Base Entity Model Schema
EntityMeta = declarative_base()


def init() -> None:
    EntityMeta.metadata.create_all(bind=engine)
