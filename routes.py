from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/employees/')
async def get_employees(db: Session = Depends(get_db)):
    try:
        return await service.get_employees(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/employees/id')
async def get_employees_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_employees_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/employees/id/')
async def put_employees_id(id: str, name: str, email: str, password_hash: str, role: str, shift_id: str, is_active: str, created_at: str, db: Session = Depends(get_db)):
    try:
        return await service.put_employees_id(db, id, name, email, password_hash, role, shift_id, is_active, created_at)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/employees/id')
async def delete_employees_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_employees_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/attendance_records/')
async def get_attendance_records(db: Session = Depends(get_db)):
    try:
        return await service.get_attendance_records(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/attendance_records/id')
async def get_attendance_records_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_attendance_records_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/attendance_records/')
async def post_attendance_records(raw_data: schemas.PostAttendanceRecords, db: Session = Depends(get_db)):
    try:
        return await service.post_attendance_records(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/attendance_records/id/')
async def put_attendance_records_id(id: str, employee_id: str, check_in: str, check_out: str, work_hours: float, date: str, late: str, early_leave: str, db: Session = Depends(get_db)):
    try:
        return await service.put_attendance_records_id(db, id, employee_id, check_in, check_out, work_hours, date, late, early_leave)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/attendance_records/id')
async def delete_attendance_records_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_attendance_records_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/shifts/')
async def get_shifts(db: Session = Depends(get_db)):
    try:
        return await service.get_shifts(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/shifts/id')
async def get_shifts_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_shifts_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/shifts/')
async def post_shifts(raw_data: schemas.PostShifts, db: Session = Depends(get_db)):
    try:
        return await service.post_shifts(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/shifts/id/')
async def put_shifts_id(id: str, name: str, start_time: str, end_time: str, db: Session = Depends(get_db)):
    try:
        return await service.put_shifts_id(db, id, name, start_time, end_time)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/shifts/id')
async def delete_shifts_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_shifts_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/leaves/')
async def get_leaves(db: Session = Depends(get_db)):
    try:
        return await service.get_leaves(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/leaves/id')
async def get_leaves_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_leaves_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/leaves/')
async def post_leaves(raw_data: schemas.PostLeaves, db: Session = Depends(get_db)):
    try:
        return await service.post_leaves(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/leaves/id/')
async def put_leaves_id(id: str, employee_id: str, date_from: str, date_to: str, status: str, reason: str, db: Session = Depends(get_db)):
    try:
        return await service.put_leaves_id(db, id, employee_id, date_from, date_to, status, reason)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/leaves/id')
async def delete_leaves_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_leaves_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/employees/')
async def post_employees(raw_data: schemas.PostEmployees, db: Session = Depends(get_db)):
    try:
        return await service.post_employees(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/login')
async def post_login(raw_data: schemas.PostLogin, db: Session = Depends(get_db)):
    try:
        return await service.post_login(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

