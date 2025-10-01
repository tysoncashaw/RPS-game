FROM python:3.11-slim as base
WORKDIR /usr/app/src
RUN groupadd -r rps && useradd -r -g rps rps    
USER rps
EXPOSE 8501

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY rps.py rps_library.py ./
COPY pages ./pages/

# Run Streamlit app
CMD ["streamlit", "run", "rps.py", "--server.port=8501", "--server.address=0.0.0.0"]