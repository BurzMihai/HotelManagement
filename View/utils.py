from sqlalchemy import create_engine, text

engine = create_engine('mysql+pymysql://root:@127.0.0.1:3305/hotel', echo=False)


if __name__ == '__main__':
    with engine.connect() as conn:
        query = conn.execute(text('SELECT * FROM clients'))
        for item in query:
            print(item)
