FROM python:3.9

WORKDIR /app

# 먼저 requirements.txt만 복사하여 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 그 다음 나머지 애플리케이션 코드 복사
COPY . .

# 환경 변수 설정 (예시)
# ENV DATABASE_URL=postgresql://user:password@postgres:5432/dbname

# 애플리케이션 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]