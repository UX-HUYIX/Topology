from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(String)

class ParsedState(Base):
    __tablename__ = 'parsed_states'
    id = Column(Integer, primary_key=True, index=True)
    state_data = Column(String)
    session_id = Column(Integer, ForeignKey('sessions.id'))

class Pattern(Base):
    __tablename__ = 'patterns'
    id = Column(Integer, primary_key=True, index=True)
    pattern_data = Column(String)

class ExpertCorrection(Base):
    __tablename__ = 'expert_corrections'
    id = Column(Integer, primary_key=True, index=True)
    correction_data = Column(String)


class SessionModel(BaseModel):
    user_id: int
    created_at: str

class ParsedStateModel(BaseModel):
    state_data: str
    session_id: int

class PatternModel(BaseModel):
    pattern_data: str

class ExpertCorrectionModel(BaseModel):
    correction_data: str
