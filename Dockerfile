FROM ubuntu:20.04 as base

ENV HOME /root
ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

RUN apt-get update -y
RUN apt-get install -y cron
RUN apt-get install -y python3-pip
    
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt
   
COPY download_cron_job /etc/cron.d/download_cron_job

RUN chmod 0644 /etc/cron.d/download_cron_job

RUN crontab /etc/cron.d/download_cron_job

RUN touch /var/log/cron.log

CMD ["python3", "api.py"]
    

    

