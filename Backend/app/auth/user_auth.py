from fastapi import FastAPI, Depends, HTTPException, status
from app.database.models import User
from app.database.db import get_db
from sqlalchemy.orm import Session
import logging

