ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG PIP_VERSION

# Content
RUN pip install sherlock-project==$PIP_VERSION

ENTRYPOINT ["sherlock"]