FROM python:3.7-alpine 
WORKDIR /app 

# Set the correct timezone
RUN apk add tzdata 
RUN ln -sf /usr/share/zoneinfo/Europe/Zurich /etc/localtime

# python environement
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app 
# VOLUME [ "./score.csv" ]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"] 
