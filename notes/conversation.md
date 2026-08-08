## 30/06
### Io:
    Come le avevo già accennato, mi piacerebbe sviluppare un progetto nell'ambito dei sistemi operativi e della virtualizzazione, con un focus sulla cybersecurity in ambienti web.

    Avevo perciò pensato a un'idea di tesi incentrata sull'uso di eBPF (Extended Berkeley Packet Filter) per l'hardening e il monitoraggio dei container.

    L'obiettivo del progetto sarebbe la realizzazione di un Proof of Concept (sfruttando il framework BCC e Python (o Go) per lo user space) in grado di intercettare a livello kernel le chiamate di sistema critiche (come execve) provenienti da un container Docker isolato che ospita un'applicazione web vulnerabile. Il sistema dovrebbe identificare in tempo reale tentativi di anomalie o attacchi di tipo Remote Code Execution.

### Ghini:
    Mi piace molto come argomento, però magari controlla che non esistano già programmi che fanno esattamente quello che vuoi fare tu.

## 30/07
### Io:
    Ho fatto un po' di ricerche e ho trovato che in effetti esistono alcuni programmi open-source (ad esempio Cilium Tetragon e Falco) che fanno più o meno quello che volevo fare io.

### Ghini:
    Gli strumenti che hai individuato Cilium/Tetragon e Falco mi sembra siano diventati moolto moolto avanzati e robusti, e che stiano diventando quasi uno standard di gestione della sicurezza in sistemi cloud e kubernetes.

    Per me vale la pena di capire bene che cosa sono, in quali contesti si possono applicare:

    a) applicazioni docker/podman
    b) docker swarm
    c) kubernetes
    d) generiche cloud

    che cosa fanno di preciso, cosa riescono a controllare e cosa gli scappa, in che modo (e con che facilità) si possono integrare in una applicazione dei 4 contesti a,b,c,d, magari facendo qualche prova comparativa.

    Cioè dopo una robusta fase descrittiva di quel che sono e che fanno questi sistemi, si potrebbe fare:

    1) una sperimentazione per capire cosa riescono a intercettare e cosa no, quali falsi allarmi generano, cosa gli scappa, come riescono ad avvisare l'utente e come riescono ad esempio a far partire qualche azione di blocco dell'attacco o di riduzione del danno.

    Oppure 2) si potrebbe considerare più un aspetto di architettura del software per capire se si può aggiungere questi sistemi ad un'applicazione esistente e quanto è complicato, o se occorre impostare le applicazioni in un modo adatto per poter usare questi sistemi, se è possibile integrare la visualizzazione dei report e degli allarmi in una unica dashboard come Grafana/Prometheus.

    Insomma, confesso che mi hai fatto venir voglia di approfondire questi argomenti, se a te l'idea piace io ti farei proseguire lo studio e valutazione sia di efficacia sia di applicabilità architetturale di questi sistemi.

    Dimenticavo una premessa al discorso precedente: visto il grado di maturità di questi sistemi Cilium/Tetragon e Falco mi sembra difficile riuscire a realizzare qualcosa di meglio partendo da zero, quindi credo sia meglio occuparsi di studiare, approfondire e testare l'esistente.

## 04/08
### Io:
    Attualmente ho creato un cluster Kubernetis in una VM e ho installato Falco. Ho poi creato un pod in cui gira un web server vulnerabile e sto cercando di analizzare che cosa Falco riesce a identificare e che cosa gli scappa, falsi allarmi che genera, facilità di configurazione, come avvisa l'utente, ecc. 

    Dopodiché pensavo di provare a integrare i due sistemi negli altri contesti che mi aveva proposto (applicazioni docker/podman, docker swarm e generiche cloud) e vedere se è possibile, con che difficoltà e con che efficacia.
    Insomma, una completa analisi comparativa fra i due sistemi.

    Volevo però capire meglio nello specifico che cosa intende per "integrarli in un'applicazione"; cioè in che tipo di applicazione vorrebbe integrarli. Inoltre, ho visto che sia per Falco che per Tetragon esistono già delle integrazioni con Grafana/Prometheus per la dashboard.
    
### Ghini:
    Sì, mi interessava capire se era già possibile integrare questi sistemi nella dashboard Grafana/Prometheus e se era possibile far partire qualche azione automatica in caso che si evidenziasse un attacco o un malfunzionamento (forse si può fare sta cosa direttamente in grafana?)