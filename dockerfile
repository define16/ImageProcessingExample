FROM ubuntu:18.04
MAINTAINER OCRTEST
WORKDIR /app
ENV PYTHONPATH "/app/src"
ARG DEBIAN_FRONTEND=noninteractive
COPY . /app

RUN apt-get -y update
RUN apt-get -y install language-pack-ko
RUN apt-get -y install wget
# Python
RUN apt-get -y install python3.8
RUN apt-get -y install python3-pip
RUN python3.8 -m pip install --upgrade pip
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
# tesseract
RUN apt-get -y install tesseract-ocr=4.00~git2288-10f4998a-2
RUN apt-get -y install libtesseract-dev
ENV TESSDATA_PREFIX="/usr/share/tesseract-ocr/4.00/tessdata"
RUN wget https://github.com/tesseract-ocr/tessdata/raw/4.00/kor.traineddata -P /usr/share/tesseract-ocr/4.00/tessdata
# Opencv
RUN apt-get -y install ffmpeg libsm6 libxext6

# Python package
RUN pip3 --version
RUN pip3 install Image
RUN pip3 install -r requestments.txt

RUN python3 --version
CMD ["/bin/sh"]
# CMD ["python3", "tesseract/main.py"]
