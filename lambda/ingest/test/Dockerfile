FROM python:3.10

WORKDIR /app
RUN pip install --no-cache-dir requests

COPY test_lambda.py .

# python -m unittest test_post_request.py
CMD [ "python3", "-m", "unittest", "test_lambda.py" ]