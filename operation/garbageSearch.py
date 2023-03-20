from models.garbage import GarbageModel
from models.search import SearchModel
from sqlalchemy import func
from exts import db

class GarbageSearchOperation():
    def __init__(self):
        self.__fields__ = ['garbage_id', 'garbage_class', 'garbage_name']

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

    # #######################################################################
    # 段怡冰
    # garbage表查询垃圾分类
    def _searchExact(self, content):
        search_result = GarbageModel.query.filter_by(garbage_name=content).first()
        return search_result

    def _searchVague(self, content):
        search_result = GarbageModel.query.filter(GarbageModel.garbage_name.like('%' + content + '%')).all()
        return search_result

    # search表添加记录
    def _searchAdd(self, task_id, open_id, garbage_id, search_type, create_time):
        search_add = SearchModel(task_id=task_id, open_id=open_id, garbage_id=garbage_id,
                                 search_type=search_type, create_time=create_time)
        db.session.add(search_add)
        db.session.commit()
        return "ok"

    # search表记录个数
    def _searchNum(self):
        search_number = SearchModel.query.count()
        return search_number