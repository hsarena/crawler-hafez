from sqlalchemy.orm import sessionmaker
from hafez.models import HafezDB, db_connect, create_table
from datetime import datetime

class HafezPipeline(object):

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        hafezdb = HafezDB()
        now = datetime.now()
        formated_date = now.strftime('%Y-%m-%d %H:%M:%S')
        hafezdb.title = item['title']
        hafezdb.voice = item['voice']
        hafezdb.faal = item['faal']
        hafezdb.meaning = item['meaning']
        hafezdb.created_date = formated_date


        try:
            session.add(hafezdb)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return item