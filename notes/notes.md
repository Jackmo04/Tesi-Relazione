# Note importanti
- Sez. 4.4 da rivedere: un po' troppo scza

# Punti da toccare
## Testing
- Elencare tecniche MITRE ATT&CK usate
- Falco vince sul contesto semantico, Tetragon sulla velocità e enforcement. Es. per valutare se viene spawnata una shell, Falco può basarsi sulla presenza di una TTY, mentre Tetragon deve basarsi solo sulla syscall execve ed eventualmente filtrare dei falsi positivi.

## Risultati
- I drop di falco non sono nulla di inaspettato. Falco produce un warning in caso di saturazione del ring-buffer, ma ciò non permette di agire in maniera mirata.
