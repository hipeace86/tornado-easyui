# -*- coding: utf-8 -*-
__author__ = 'Hipeace86'
from sqlalchemy import Column, Integer, String, DateTime
from lib.Route import BaseModel, RightModel
from Right.Entity.Kit import Kit


class LogPassword(RightModel, BaseModel):
    """
    密码修改日志
    """
    __tablename__ = 'trt_log_password'

    Id = Column('fi_id', Integer, primary_key=True)
    UserId = Column('fi_user_id', Integer)
    OldPassword = Column('fs_old_password', String(100))
    CreateId = Column('fi_create_id', Integer)
    CreateTime = Column('ft_create_time', DateTime)
    UpdateId = Column('fi_update_id', Integer)
    UpdateTime = Column('ft_update_time', DateTime)

    def toDict(self):
        return {
            'Id': self.Id,
            'UserId': self.UserId,
            'OldPassword': self.OldPassword,
            'CreateId': Kit.getUserNameById(self.CreateId),
            'CreateTime': self.CreateTime.strftime('%Y-%m-%d %H:%M:%S') if self.CreateTime else '',
            'UpdateId': Kit.getUserNameById(self.UpdateId),
            'UpdateTime': self.UpdateTime.strftime('%Y-%m-%d %H:%M:%S') if self.UpdateTime else '',
            'UserName': Kit.getUserNameById(self.UserId),
        }
#=========================================================================
# 开发人员添加的其它所有代码请加到下面，以便生成的模板修改后重新生成的替换
#=========================================================================
