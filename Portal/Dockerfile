FROM harbor.ad.glshk.com/baseimgproxy/node:18.12.1-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm", "run", "start"]