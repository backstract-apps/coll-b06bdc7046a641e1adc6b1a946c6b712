from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_employees(db: Session):

    employees_all = db.query(models.Employees).all()
    employees_all = [new_data.to_dict() for new_data in employees_all] if employees_all else employees_all

    res = {
        'employees_all': employees_all,
    }
    return res

async def get_employees_id(db: Session, id: int):

    employees_one = db.query(models.Employees).filter(models.Employees.id == id).first() 
    employees_one = employees_one.to_dict() if employees_one else employees_one

    res = {
        'employees_one': employees_one,
    }
    return res

async def put_employees_id(db: Session, id: str, name: str, email: str, password_hash: str, role: str, shift_id: str, is_active: str, created_at: str):

    employees_edited_record = db.query(models.Employees).filter(models.Employees.id == id).first()
    for key, value in {'id': id, 'name': name, 'role': role, 'email': email, 'shift_id': shift_id, 'is_active': is_active, 'created_at': created_at, 'password_hash': password_hash}.items():
          setattr(employees_edited_record, key, value)
    db.commit()
    db.refresh(employees_edited_record)
    employees_edited_record = employees_edited_record.to_dict() 

    res = {
        'employees_edited_record': employees_edited_record,
    }
    return res

async def delete_employees_id(db: Session, id: int):

    employees_deleted = None
    record_to_delete = db.query(models.Employees).filter(models.Employees.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        employees_deleted = record_to_delete.to_dict() 

    res = {
        'employees_deleted': employees_deleted,
    }
    return res

async def get_attendance_records(db: Session):

    attendance_records_all = db.query(models.AttendanceRecords).all()
    attendance_records_all = [new_data.to_dict() for new_data in attendance_records_all] if attendance_records_all else attendance_records_all

    res = {
        'attendance_records_all': attendance_records_all,
    }
    return res

async def get_attendance_records_id(db: Session, id: int):

    attendance_records_one = db.query(models.AttendanceRecords).filter(models.AttendanceRecords.id == id).first() 
    attendance_records_one = attendance_records_one.to_dict() if attendance_records_one else attendance_records_one

    res = {
        'attendance_records_one': attendance_records_one,
    }
    return res

async def post_attendance_records(db: Session, raw_data: schemas.PostAttendanceRecords):
    id:str = raw_data.id
    employee_id:str = raw_data.employee_id
    check_in:datetime.datetime = raw_data.check_in
    check_out:datetime.datetime = raw_data.check_out
    work_hours:float = raw_data.work_hours
    date:datetime.date = raw_data.date
    late:bool = raw_data.late
    early_leave:bool = raw_data.early_leave


    record_to_be_added = {'id': id, 'date': date, 'late': late, 'check_in': check_in, 'check_out': check_out, 'work_hours': work_hours, 'early_leave': early_leave, 'employee_id': employee_id}
    new_attendance_records = models.AttendanceRecords(**record_to_be_added)
    db.add(new_attendance_records)
    db.commit()
    db.refresh(new_attendance_records)
    attendance_records_inserted_record = new_attendance_records.to_dict()

    res = {
        'attendance_records_inserted_record': attendance_records_inserted_record,
    }
    return res

async def put_attendance_records_id(db: Session, id: str, employee_id: str, check_in: str, check_out: str, work_hours: float, date: str, late: str, early_leave: str):

    attendance_records_edited_record = db.query(models.AttendanceRecords).filter(models.AttendanceRecords.id == id).first()
    for key, value in {'id': id, 'date': date, 'late': late, 'check_in': check_in, 'check_out': check_out, 'work_hours': work_hours, 'early_leave': early_leave, 'employee_id': employee_id}.items():
          setattr(attendance_records_edited_record, key, value)
    db.commit()
    db.refresh(attendance_records_edited_record)
    attendance_records_edited_record = attendance_records_edited_record.to_dict() 

    res = {
        'attendance_records_edited_record': attendance_records_edited_record,
    }
    return res

async def delete_attendance_records_id(db: Session, id: int):

    attendance_records_deleted = None
    record_to_delete = db.query(models.AttendanceRecords).filter(models.AttendanceRecords.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        attendance_records_deleted = record_to_delete.to_dict() 

    res = {
        'attendance_records_deleted': attendance_records_deleted,
    }
    return res

async def get_shifts(db: Session):

    shifts_all = db.query(models.Shifts).all()
    shifts_all = [new_data.to_dict() for new_data in shifts_all] if shifts_all else shifts_all

    res = {
        'shifts_all': shifts_all,
    }
    return res

async def get_shifts_id(db: Session, id: int):

    shifts_one = db.query(models.Shifts).filter(models.Shifts.id == id).first() 
    shifts_one = shifts_one.to_dict() if shifts_one else shifts_one

    res = {
        'shifts_one': shifts_one,
    }
    return res

async def post_shifts(db: Session, raw_data: schemas.PostShifts):
    id:str = raw_data.id
    name:str = raw_data.name
    start_time:datetime.time = raw_data.start_time
    end_time:datetime.time = raw_data.end_time


    record_to_be_added = {'id': id, 'name': name, 'end_time': end_time, 'start_time': start_time}
    new_shifts = models.Shifts(**record_to_be_added)
    db.add(new_shifts)
    db.commit()
    db.refresh(new_shifts)
    shifts_inserted_record = new_shifts.to_dict()

    res = {
        'shifts_inserted_record': shifts_inserted_record,
    }
    return res

async def put_shifts_id(db: Session, id: str, name: str, start_time: str, end_time: str):

    shifts_edited_record = db.query(models.Shifts).filter(models.Shifts.id == id).first()
    for key, value in {'id': id, 'name': name, 'end_time': end_time, 'start_time': start_time}.items():
          setattr(shifts_edited_record, key, value)
    db.commit()
    db.refresh(shifts_edited_record)
    shifts_edited_record = shifts_edited_record.to_dict() 

    res = {
        'shifts_edited_record': shifts_edited_record,
    }
    return res

async def delete_shifts_id(db: Session, id: int):

    shifts_deleted = None
    record_to_delete = db.query(models.Shifts).filter(models.Shifts.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        shifts_deleted = record_to_delete.to_dict() 

    res = {
        'shifts_deleted': shifts_deleted,
    }
    return res

async def get_leaves(db: Session):

    leaves_all = db.query(models.Leaves).all()
    leaves_all = [new_data.to_dict() for new_data in leaves_all] if leaves_all else leaves_all

    res = {
        'leaves_all': leaves_all,
    }
    return res

async def get_leaves_id(db: Session, id: int):

    leaves_one = db.query(models.Leaves).filter(models.Leaves.id == id).first() 
    leaves_one = leaves_one.to_dict() if leaves_one else leaves_one

    res = {
        'leaves_one': leaves_one,
    }
    return res

async def post_leaves(db: Session, raw_data: schemas.PostLeaves):
    id:str = raw_data.id
    employee_id:str = raw_data.employee_id
    date_from:datetime.date = raw_data.date_from
    date_to:datetime.date = raw_data.date_to
    status:str = raw_data.status
    reason:str = raw_data.reason


    record_to_be_added = {'id': id, 'reason': reason, 'status': status, 'date_to': date_to, 'date_from': date_from, 'employee_id': employee_id}
    new_leaves = models.Leaves(**record_to_be_added)
    db.add(new_leaves)
    db.commit()
    db.refresh(new_leaves)
    leaves_inserted_record = new_leaves.to_dict()

    res = {
        'leaves_inserted_record': leaves_inserted_record,
    }
    return res

async def put_leaves_id(db: Session, id: str, employee_id: str, date_from: str, date_to: str, status: str, reason: str):

    leaves_edited_record = db.query(models.Leaves).filter(models.Leaves.id == id).first()
    for key, value in {'id': id, 'reason': reason, 'status': status, 'date_to': date_to, 'date_from': date_from, 'employee_id': employee_id}.items():
          setattr(leaves_edited_record, key, value)
    db.commit()
    db.refresh(leaves_edited_record)
    leaves_edited_record = leaves_edited_record.to_dict() 

    res = {
        'leaves_edited_record': leaves_edited_record,
    }
    return res

async def delete_leaves_id(db: Session, id: int):

    leaves_deleted = None
    record_to_delete = db.query(models.Leaves).filter(models.Leaves.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        leaves_deleted = record_to_delete.to_dict() 

    res = {
        'leaves_deleted': leaves_deleted,
    }
    return res

async def post_employees(db: Session, raw_data: schemas.PostEmployees):
    id:str = raw_data.id
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password
    role:str = raw_data.role
    shift_id:str = raw_data.shift_id
    is_active:bool = raw_data.is_active
    created_at:datetime.datetime = raw_data.created_at


    record_to_be_added = {'id': id, 'name': name, 'role': role, 'email': email, 'password': password, 'shift_id': shift_id, 'is_active': is_active, 'created_at': created_at, 'password_hash': password_hash}
    new_employees = models.Employees(**record_to_be_added)
    db.add(new_employees)
    db.commit()
    db.refresh(new_employees)
    employees_inserted_record = new_employees.to_dict()



    bs_jwt_payload = {
        'exp': int((datetime.datetime.utcnow() + datetime.timedelta(seconds=1000)).timestamp()),
        'data': employees_inserted_record
    }

    jwt1 = jwt.encode(bs_jwt_payload, 'api_d2e40b5aa87e40bd8a65cd31a99e8ea8', algorithm='HS256')

    res = {
        'employees_inserted_record': employees_inserted_record,
        'jwt1': jwt1,
    }
    return res

async def post_login(db: Session, raw_data: schemas.PostLogin):
    email:str = raw_data.email
    password:str = raw_data.password


    login_email = db.query(models.Employees).filter(models.Employees.email == email).first() 
    login_email = login_email.to_dict() if login_email else login_email


    # student get records
    bs_jwt_payload = {
        'exp': int((datetime.datetime.utcnow() + datetime.timedelta(seconds=1000998)).timestamp()),
        'data': login_email
    }

    adjfhgukdhgkudh = jwt.encode(bs_jwt_payload, 'api_d2e40b5aa87e40bd8a65cd31a99e8ea8', algorithm='HS256')

    res = {
        'login': login_email,
        'jwt2': adjfhgukdhgkudh,
    }
    return res

