FROM public.ecr.aws/lambda/python:3.12

WORKDIR ${LAMBDA_TASK_ROOT}

COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install --no-cache-dir -r requirements.txt

ENV KAGGLE_KEY=$KAGGLE_KEY
ENV KAGGLE_USERNAME=$KAGGLE_USERNAME

COPY app.py ${LAMBDA_TASK_ROOT}
COPY test_curl.py ${LAMBDA_TASK_ROOT}

CMD [ "app.handler" ]
