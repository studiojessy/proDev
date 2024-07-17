from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 수정: 실제 데이터베이스 URL로 변경하세요.
SQLALCHEMY_DATABASE_URL = "postgresql://user:abcd1234@postgres:5432/jessyapp"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()