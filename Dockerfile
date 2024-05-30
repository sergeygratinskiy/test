FROM python:3
WORKDIR /test
COPY view_test.py /test/view_test.py
CMD ["python", "/test/view_test.py"]
