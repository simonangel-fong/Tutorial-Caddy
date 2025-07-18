# Tutorial Caddy

A repo to learn Caddy.

---

## Static Web

```conf
:80 {
    root * /usr/share/caddy
    file_server
}
```

```sh
docker compose -f compose.web.yaml up -d

curl localhost:8001
```

---

## Reverse Proxy

```conf
:80 {
    redir /app1 /app1/
    handle_path /app1/* {
        reverse_proxy app1:8000
    }

    redir /app2 /app2/
    handle_path /app2/* {
        reverse_proxy app2:8000
    }
}
```

```sh
docker compose -f compose.proxy.yaml up -d

curl -L localhost:8001/app1
# {"message":"Current app: app1"}
curl -L localhost:8001/app2/
# {"message":"Current app: app2"}
```

---

## Load Balancer

```conf
:80 {
     reverse_proxy app1:8000 app2:8000 {
           lb_policy round_robin
     }
}
```

```sh
docker compose -f compose.balancing.yaml up -d

curl -L localhost:8001
# {"message":"Current app: app1"}
# {"message":"Current app: app2"}
```