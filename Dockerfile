FROM python:3.10 as builder

WORKDIR /working

COPY / /working

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip3 install --upgrade pip

RUN pip3 install --upgrade -r /working/requirements.txt

RUN python -m build /working

RUN pip3 install /working/dist/pythonPractice-0.12-py3-none-any.whl

FROM python:3.10-slim-bullseye as main

COPY --from=builder /opt/venv /opt/venv

ENTRYPOINT ["sh"]






