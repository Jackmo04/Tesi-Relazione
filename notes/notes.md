# Testing

Falco vince sul contesto semantico, Tetragon sulla velocità e enforcement. 
Es. per valutare se viene spawnata una shell, Falco può basarsi sulla presenza di una TTY, mentre Tetragon deve basarsi solo sulla syscall execve ed eventualmente filtrare dei falsi positivi.