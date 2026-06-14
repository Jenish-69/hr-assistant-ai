from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str


class LeaveRequest(BaseModel):
    employee_id: int
    leave_type: str
    from_date: str
    to_date: str
    reason: str


class RegularizationRequest(BaseModel):
    employee_id: int
    date: str
    entry_time: str
    exit_time: str
    reason: str
    description: str