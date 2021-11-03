FROM node:14.18

WORKDIR /app/frontend
COPY package*.json /app/frontend/

RUN npm install
RUN npm install -g @vue/cli

COPY . .
EXPOSE 8080

CMD ["npm", "run", "serve"]