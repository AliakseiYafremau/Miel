FROM node:18-slim

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm i

COPY . .
