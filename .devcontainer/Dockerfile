FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    tesseract-ocr libtesseract-dev \
    python3-pip python3-pil python3-pandas \
    poppler-utils

RUN pip3 install pytesseract pdf2image
