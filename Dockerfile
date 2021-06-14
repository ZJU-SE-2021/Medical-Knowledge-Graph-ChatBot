FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

COPY . /app

ENV NEO4J "http://127.0.0.1:7474"

RUN pip install -r requirements.txt -i https://mirrors.bfsu.edu.cn/pypi/web/simple

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
