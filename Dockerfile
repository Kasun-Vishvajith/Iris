# ── Base image ──────────────────────────────────────────────────────────────
FROM python:3.11-slim

# ── Environment ─────────────────────────────────────────────────────────────
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# ── Working directory ────────────────────────────────────────────────────────
WORKDIR /app

# ── Install dependencies (cached layer) ─────────────────────────────────────
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── Copy source ──────────────────────────────────────────────────────────────
COPY model/ ./model/
COPY app/   ./app/

# ── Create model output directory ────────────────────────────────────────────
RUN mkdir -p /app/model

# ── Train the model at build time ────────────────────────────────────────────
RUN python model/train.py

# ── Expose port ──────────────────────────────────────────────────────────────
EXPOSE 8000

# ── Start FastAPI server ──────────────────────────────────────────────────────
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
