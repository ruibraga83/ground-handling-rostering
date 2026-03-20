FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY dist ./dist
EXPOSE 3002
CMD ["node", "dist/index.js"]