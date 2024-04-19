FROM python:latest
WORKDIR /usr/app/src

COPY rps.py ./
COPY rps_library.py ./
COPY pages ./pages/

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir streamlit
RUN pip install --no-cache-dir st_pages
RUN pip install --no-cache-dir streamlit_extras
RUN pip install --no-cache-dir validators

EXPOSE 8501

CMD [ "python", "-m",  "streamlit", "run", "./rps.py" ]