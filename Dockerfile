FROM python:3.10

ARG UID
ARG GID

RUN groupadd --gid $GID nonroot && \
    useradd --uid $UID --gid $GID --shell /bin/bash --create-home nonroot

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir --progress-bar off -r requirements.txt

COPY . .
RUN pip install .

RUN chown -R $GID:$UID /usr/src/app
USER nonroot

CMD [ "mygit", "-h" ]