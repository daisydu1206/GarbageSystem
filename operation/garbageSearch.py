from models.garbage import GarbageModel
from models.search import SearchModel
from sqlalchemy import func
from exts import db

class GarbageSearchOperation():
    def _garbageNum(self):
        garbage_num = GarbageModel.query.count()
        return garbage_num
    def _searchNumToday(self, day):
        search_num_today = SearchModel.query.filter(SearchModel.create_time >= day).count()
        return search_num_today

    def _topWordsToay(self, mode, day):
        temp = SearchModel.query.with_entities(SearchModel.garbage_id, func.count("*").label('count')).filter(SearchModel.create_time >= day, SearchModel.search_type == mode).group_by(SearchModel.garbage_id).subquery()
        top_garbages = db.session.query(GarbageModel.garbage_name).outerjoin(temp, GarbageModel.garbage_id == temp.c.garbage_id).order_by(temp.c.count.desc()).limit(10).all()
        return top_garbages

