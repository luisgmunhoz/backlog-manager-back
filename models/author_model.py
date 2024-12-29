from sqlalchemy import Column, Integer, PrimaryKeyConstraint, String
from sqlalchemy.orm import relationship

from models.base_model import EntityMeta
from models.book_author_association import book_author_association


class Author(EntityMeta):
    __tablename__ = "authors"

    id = Column(Integer)
    name = Column(String(16), nullable=False)
    books = relationship(
        "Book",
        lazy="dynamic",
        secondary=book_author_association,
    )

    PrimaryKeyConstraint(id)

    def normalize(self) -> dict[str, str]:
        return {
            "id": str(self.id),
            "name": str(self.name),
        }
