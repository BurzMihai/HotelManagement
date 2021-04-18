from sqlalchemy import Column, Integer, String, Float, Text
from View.utils import Base


class Review(Base):
    __tablename__ = 'reviews'
    review_id = Column(Integer, primary_key=True)
    client_first_name = Column(String, nullable=False)
    review_content = Column(Text, nullable=False)
    stars = Column(Float, nullable=False)

    def __repr__(self):
        return f'{self.review_id, self.review_content, self.client_first_name, self.stars}'
