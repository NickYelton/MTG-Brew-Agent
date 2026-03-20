from models.base import Base
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Card(Base):
    __tablename__ = 'cards'

    id = Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    scryfall_id = Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    name = Mapped[str] = mapped_column(String, nullable=False)
    mana_cost = Mapped[str] = mapped_column(String)
    type_line = Mapped[str] = mapped_column(String)
    oracle_text = Mapped[str] = mapped_column(String)
    color_identity = Mapped[str] = mapped_column(String)
    last_synced = Mapped[DateTime] = mapped_column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Card(name='{self.name}', mana_cost='{self.mana_cost}', type_line='{self.type_line}')>"