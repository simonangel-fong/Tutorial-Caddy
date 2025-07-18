# Tutorial Caddy

A repo to learn Caddy.

---

## Static Web

```sh
docker compose -f compose.web.yaml up -d

curl localhost:8001
```

---

## Reverse Proxy

```sh
docker compose -f compose.web.yaml up -d

curl -L localhost:8001/app1
# {"message":"Current app: app1"}
curl -L localhost:8001/app2/
# {"message":"Current app: app2"}
```
