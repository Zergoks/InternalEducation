FROM python:3.9.5-buster

#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
#    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
#RUN apt-get update && apt-get -y install google-chrome-stable

#RUN echo 'nameserver 8.8.8.8'>/etc/resolv.conf
#RUN ping pypi.org -n 10

RUN mkdir -p /user/src/app/
WORKDIR /usr/src/app/

COPY requirements.txt ./

#RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD ["pytest", "-m test"]
CMD ["ls"]

