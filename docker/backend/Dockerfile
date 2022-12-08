FROM python:3.11.1-alpine

WORKDIR /app

COPY ./backend .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry
RUN poetry config virtualenvs.create false

EXPOSE 8000

RUN poetry install --no-root

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
