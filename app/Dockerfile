FROM python:alpine3.23

WORKDIR /app

RUN apk add --no-cache postgresql-dev gcc musl-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN addgroup -S python_group  \
&& adduser -SDH -G python_group python_user 

USER python_user

COPY --chown=python_user:python_group main.py config.py ./

EXPOSE 8000

HEALTHCHECK --interval=5s --timeout=10s --start-period=5s --retries=3 \
CMD ["wget", "-q", "--spider", "http://localhost:8000/healthy"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]