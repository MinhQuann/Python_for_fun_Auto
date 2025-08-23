# src/api/schemas_ucrm.py
from datetime import datetime
from pydantic import BaseModel, ConfigDict, field_validator

class ContactRecord(BaseModel):
    model_config = ConfigDict(extra="allow")  # cho phép API trả thêm trường khác

    _id: str
    created_date: datetime
    created_by: str
    modify_time: datetime
    modify_by: str
    active: bool
    owner: str

    # Không rỗng cho các trường string chính
    @field_validator("_id", "created_by", "modify_by", "owner")
    @classmethod
    def not_blank(cls, v: str):
        if v is None or not str(v).strip():
            raise ValueError("must be a non-empty string")
        return v
