import pytest
from datetime import datetime
from app.models.base import Base
from app.db.session import SessionLocal, engine
from tests.conftest import db_session
from app.models import card

class TestCardModel:
    @pytest.fixture(autouse=True)
    def setup(self, db_session):
        self.db = db_session

    def test_create_card(self):
        # Create a new card instance
        new_card = card.Card(
            scryfall_id=12345,
            name="Test Card",
            mana_cost="1G",
            type_line="Creature - Elf",
            oracle_text="This is a test card.",
            color_identity="G",
            last_synced=datetime(2024, 6, 1)
        )
        
        # Add and commit the new card to the database
        self.db.add(new_card)
        self.db.commit()
        
        # Query the card back from the database
        retrieved_card = self.db.query(card.Card).filter_by(name="Test Card").first()
        
        # Assert that the retrieved card matches the created card
        assert retrieved_card is not None
        assert retrieved_card.name == "Test Card"
        assert retrieved_card.scryfall_id == 12345
        assert retrieved_card.mana_cost == "1G"
        assert retrieved_card.type_line == "Creature - Elf"
        assert retrieved_card.oracle_text == "This is a test card."
        assert retrieved_card.color_identity == "G"
        assert retrieved_card.last_synced == datetime(2024, 6, 1)