from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Employees(Base):
    __tablename__ = 'employees'
    id = Column(String, primary_key=True)
    name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    password = Column(String, primary_key=False)
    role = Column(String, primary_key=False)
    shift_id = Column(String, primary_key=False)
    is_active = Column(Boolean, primary_key=False)
    created_at = Column(Time, primary_key=False)


class Salaries(Base):
    __tablename__ = 'salaries'
    id = Column(Integer, primary_key=True)
    employee_id = Column(String, primary_key=False)
    month = Column(Date, primary_key=False)
    total_work_days = Column(Float, primary_key=False)
    amount_paid = Column(Float, primary_key=False)


class AttendanceRecords(Base):
    __tablename__ = 'attendance_records'
    id = Column(String, primary_key=True)
    employee_id = Column(String, primary_key=False)
    check_in = Column(Time, primary_key=False)
    check_out = Column(Time, primary_key=False)
    work_hours = Column(Float, primary_key=False)
    date = Column(Date, primary_key=False)
    late = Column(Boolean, primary_key=False)
    early_leave = Column(Boolean, primary_key=False)


class Shifts(Base):
    __tablename__ = 'shifts'
    id = Column(String, primary_key=True)
    name = Column(String, primary_key=False)
    start_time = Column(Time, primary_key=False)
    end_time = Column(Time, primary_key=False)


class Leaves(Base):
    __tablename__ = 'leaves'
    id = Column(String, primary_key=True)
    employee_id = Column(String, primary_key=False)
    date_from = Column(Date, primary_key=False)
    date_to = Column(Date, primary_key=False)
    status = Column(String, primary_key=False)
    reason = Column(String, primary_key=False)


