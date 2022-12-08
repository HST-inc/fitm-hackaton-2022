FROM node:18.12.1-alpine3.16

WORKDIR /app

COPY ./frontend .

RUN yarn install --frozen-lockfile --non-interactive

CMD ["yarn", "dev", "--host", "0.0.0.0"]
