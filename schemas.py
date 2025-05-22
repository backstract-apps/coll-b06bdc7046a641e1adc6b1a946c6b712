from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Employees(BaseModel):
    id: str
    name: str
    email: str
    password: str
    role: str
    shift_id: str
    is_active: bool
    created_at: datetime.time


class ReadEmployees(BaseModel):
    id: str
    name: str
    email: str
    password: str
    role: str
    shift_id: str
    is_active: bool
    created_at: datetime.time
    class Config:
        from_attributes = True


class Salaries(BaseModel):
    id: int
    employee_id: str
    month: datetime.date
    total_work_days: float
    amount_paid: float


class ReadSalaries(BaseModel):
    id: int
    employee_id: str
    month: datetime.date
    total_work_days: float
    amount_paid: float
    class Config:
        from_attributes = True


class AttendanceRecords(BaseModel):
    id: str
    employee_id: str
    check_in: datetime.time
    check_out: datetime.time
    work_hours: float
    date: datetime.date
    late: bool
    early_leave: bool


class ReadAttendanceRecords(BaseModel):
    id: str
    employee_id: str
    check_in: datetime.time
    check_out: datetime.time
    work_hours: float
    date: datetime.date
    late: bool
    early_leave: bool
    class Config:
        from_attributes = True


class Shifts(BaseModel):
    id: str
    name: str
    start_time: datetime.time
    end_time: datetime.time


class ReadShifts(BaseModel):
    id: str
    name: str
    start_time: datetime.time
    end_time: datetime.time
    class Config:
        from_attributes = True


class Leaves(BaseModel):
    id: str
    employee_id: str
    date_from: datetime.date
    date_to: datetime.date
    status: str
    reason: str


class ReadLeaves(BaseModel):
    id: str
    employee_id: str
    date_from: datetime.date
    date_to: datetime.date
    status: str
    reason: str
    class Config:
        from_attributes = True




class PostAttendanceRecords(BaseModel):
    id: str
    employee_id: str
    check_in: Any
    check_out: Any
    work_hours: Any
    date: Any
    late: bool
    early_leave: bool

    class Config:
        from_attributes = True



class PostShifts(BaseModel):
    id: str
    name: str
    start_time: Any
    end_time: Any

    class Config:
        from_attributes = True



class PostLeaves(BaseModel):
    id: str
    employee_id: str
    date_from: Any
    date_to: Any
    status: str
    reason: str

    class Config:
        from_attributes = True



class PostEmployees(BaseModel):
    id: str
    name: str
    email: str
    password: str
    role: str
    shift_id: str
    is_active: bool
    created_at: Any

    class Config:
        from_attributes = True



class PostLogin(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True

