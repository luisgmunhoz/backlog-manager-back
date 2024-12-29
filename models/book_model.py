from sqlalchemy import Column, Integer, PrimaryKeyConstraint, String
from sqlalchemy.orm import relationship

from models.base_model import EntityMeta
from models.book_author_association import book_author_association


class Book(EntityMeta):
    __tablename__ = "books"

    id = Column(Integer)
    name = Column(String(40), nullable=False)
    authors = relationship(
        "Author",
        lazy="dynamic",
        secondary=book_author_association,
    )

    PrimaryKeyConstraint(id)

    def normalize(self) -> dict[str, str]:
        return {
            "id": str(self.id),
            "name": str(self.name),
        }
