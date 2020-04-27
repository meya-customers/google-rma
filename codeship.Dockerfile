FROM alpine:3.10

ARG MEYA_AUTH_TOKEN
ARG GEMFURY_AUTH_TOKEN
ARG GOOGLE_AUTH_JSON
ARG GOOGLE_PROJECT_ID

WORKDIR /opt/app/

RUN apk update \
  && apk add g++ git python python3 yarn bzip2-dev coreutils gcc libc-dev \
     libffi-dev python3-dev py3-pygit2 linux-headers make \
     openssl-dev util-linux-dev xz-dev zlib-dev \
  && wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-243.0.0-linux-x86_64.tar.gz -O /opt/google-cloud-sdk-243.0.0-linux-x86_64.tar.gz \
  && tar -C /opt -zxf /opt/google-cloud-sdk-243.0.0-linux-x86_64.tar.gz \
  && rm /opt/google-cloud-sdk-243.0.0-linux-x86_64.tar.gz \
  && ln -s /opt/google-cloud-sdk/bin/gcloud /usr/local/bin/gcloud \
  && ln -s /opt/google-cloud-sdk/bin/gsutil /usr/local/bin/gsutil \
  && echo "${GOOGLE_AUTH_JSON}" > /keyconfig.json \
  && gcloud auth activate-service-account --key-file /keyconfig.json --project "${GOOGLE_PROJECT_ID}" \
  && echo "//npm.fury.io/meya-ai/:_authToken=${GEMFURY_AUTH_TOKEN}" >> ~/.npmrc \
  && git config --global user.email "codeship@meya.ai" \
  && git config --global user.name "codeship"

COPY requirements.txt .

RUN pip3 install --extra-index-url https://meya:$MEYA_AUTH_TOKEN@grid.meya.ai/registry/pypi -r requirements.txt

COPY package.json .
COPY yarn.lock .
COPY .yarnrc .
RUN yarn install

COPY . .
