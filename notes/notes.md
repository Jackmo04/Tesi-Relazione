# Testing

Falco vince sul contesto semantico, Tetragon sulla velocità e enforcement. 
Es. per valutare se viene spawnata una shell, Falco può basarsi sulla presenza di una TTY, mentre Tetragon deve basarsi solo sulla syscall execve ed eventualmente filtrare dei falsi positivi.

# Punti da toccare
- Tuning delle regole, pochi FP ma senza creare punti ciechi (caso TracingPolicies)
- Utilizzo dei container ID per tracciamento test (in generale la logica)
- Il sottosistema eBPF del kernel è progettato per supprotare la concorrenza, perciò non interferiscono.
- Aggiungere una sezione di confronto metodologico:
    - Falco è costruito con una mentalità da Intrusion Detection System (IDS). Di base, non è un logger di eventi, ma un motore di regole.
	- Tetragon nasce nell'ecosistema Cilium come strumento di osservabilità profonda (Flight Recorder) oltre che di sicurezza.
- Nel compose, parlare dell'allowlist (per rendere Tetragon più simile a Falco)
- Parlare dei container usa-e-getta (isolamento di stato, correlazione test-container)
- Utilizzo di Prometheus per collezionare statistiche sui drop
- Mettere link a lista di test usati
- Elencare tecniche MITRE ATT&CK usate
