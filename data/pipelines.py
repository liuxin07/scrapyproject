from sqlalchemy.orm import sessionmaker
from data.models import Repository, engine
class DataPipeline(object):
    def process_item(self, item, spider):
        self.session.add(Repository(**item))
        return item

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()
