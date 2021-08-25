from datetime import datetime, timezone
from libs.database.database import Database
from sqlalchemy import Column, Integer, DateTime



class MasterModel(Database.base):
    __abstract__ = True

    id = Column(Integer, autoincrement=True, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
