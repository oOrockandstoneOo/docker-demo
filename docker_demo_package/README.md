# Demo Docker Base su Debian 13

## Contenuto
- demo-dockerfile/: esempio di Dockerfile + index.html
- demo-compose/: esempio di docker compose con web (Python) + Redis

## Istruzioni rapide

### Build immagine custom
```bash
cd demo-dockerfile
docker build -t demo-nginx:local .
docker run --rm -d -p 8081:80 demo-nginx:local
```

### Avvio stack Compose
```bash
cd demo-compose
docker compose up -d
curl http://localhost:8000
```

### Stop
```bash
docker compose down
```
