# Testing

Falco vince sul contesto semantico, Tetragon sulla velocità e enforcement. 
Es. per valutare se viene spawnata una shell, Falco può basarsi sulla presenza di una TTY, mentre Tetragon deve basarsi solo sulla syscall execve ed eventualmente filtrare dei falsi positivi.

# Punti da toccare
- Aggiungere una sezione di confronto metodologico:
    - Falco è costruito con una mentalità da Intrusion Detection System (IDS). Di base, non è un logger di eventi, ma un motore di regole.
	- Tetragon nasce nell'ecosistema Cilium come strumento di osservabilità profonda (Flight Recorder) oltre che di sicurezza.
- Elencare tecniche MITRE ATT&CK usate
