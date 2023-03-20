# ############################################################################
# 段怡冰
######
from models.errorInfo import ErrorInfoModel
from exts import db

class ErrorInfoOperation():
    # errorinfo表添加记录
    def _errorAdd(self, error_id, open_id, garbage_id, error_content, create_time):
        error_info = ErrorInfoModel(error_id=error_id, open_id=open_id, garbage_id=garbage_id,
                                   error_content=error_content, create_time=create_time)
        db.session.add(error_info)
        db.session.commit()
        return "ok"

    # errorinfo表记录个数
    def _errorNum(self):
        error_num = ErrorInfoModel.query.count()
        return error_num