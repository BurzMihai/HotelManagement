from sqlalchemy.orm import sessionmaker
from Domain.review import Review
from View.utils import engine


class ReviewModel:
    def __init__(self):
        self.__engine = engine
        self.__my_session = sessionmaker(bind=engine)()

    def create_review(self, review_id, client_first_name, review_content, stars):
        self.__my_session.add(
            Review(
                review_id=review_id,
                client_first_name=client_first_name,
                review_content=review_content,
                stars=stars
            )
        )
        self.__my_session.commit()

    def read_review(self):
        self.__my_session.query(Review).all()

    def update_review(self, review_id, client_first_name, review_content, stars):
        my_review = self.__my_session.query(Review).filter_by(review_id=review_id).first()
        if my_review:
            self.__my_session.query(
                Review
            ).filter_by(
                review_id
            ).update({
                'client_first_name': f'{client_first_name or my_review.client_first_name}',
                'review_content': f'{review_content or my_review.review_content}',
                'stars': f'{stars or my_review.stars}'

            })
        self.__my_session.commit()

    def delete_review(self, review_id):
        self.__my_session.query(Review).filter_by(review_id=review_id).delete()
        self.__my_session.commit()

    def find_by_id(self, review_id):
        my_review = self.__my_session.query(Review).filter_by(review_id=review_id).first()
        return my_review
