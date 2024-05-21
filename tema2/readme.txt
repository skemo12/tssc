Paunoiu Darius Alexandru 342C4
Tema 2 TSSC


1. Ne logam la primul server folosind ./connect.sh. Facem un scan la adresa
folosind nmap -sP 192.168.160.* si vedem ca adresa 192.168.160.213 e
disponibila, verificam si ce port-uri sunt disponibile cu nmap -p-
192.168.160.213, descoperim ca 80, ne uitam pe ./webconnect.sh, vedem ca nu
conteaza decat finalul adresii, rulam ./webconnect.sh 1.1.1.213 80 si intram pe
localhost:8080 in browser. Cica ar trebui sa fie un flag da nu-l vedem.
Deschidem consola nu e acolo, deschidem codul html dam ctrl+f si-l gasim pe
SpeishFlag{0ejTi8B1rszukRrWCilZa0i3K2Yyf6ip}.

2. Verificam traficul local pe your-jail cu tcpdump -i eth0, si observam niste
trafic intre x.x.x.213 si your-jail, un arp (nimic interesant), dar si un pachet
trimis catre your-jail:8385. Folosim comanda nc -l 8385 sa vedem ce se intampla
si primim dupa mai mult timp, un post request, din care extragem username ul
guard si parola cc8654cb8b. Ne logam ca si guard si avem flag-ul in fata ochilor
SpeishFlag{MmGJMxEzvyOC2aB1tpVgq5ye7S6VIgJQ}.

3. Incercam sa-l hackuim pe deckan cu un script html care e fix formularul de
schimbare a parolei. Ne prindem cum sa facem scriptul datorita hinturilor din
html. Script-ul e inclus in arhiva, cu numele changePass.html. In consola gasim
flag-ul SpeishFlag{p8KXaXAGa5boHz6lWa4S1CfS8THOsF7F} si parola reala a decanului
61e0024fc2.

4. Mi-a mancat sufletul acest task, deoarece aparent daca ii schimbi si id-ul
rekt0r-ului, nu mai merge site-ul cand te loghezi ca rekt0r cum trebuie.
Comenzile initial folosite fiind:

update, accounts, id=77, profile_img=profile/vader.jpg, username` is not null OR
`username=rekt0r update, accounts,
password=83592796bc17705662dc9a750c8b6d0a4fd93396, id=77

Unde 83592796bc17705662dc9a750c8b6d0a4fd93396 este hash-ul sha1 al cuvantului
"parola".

Dupa care, am adaugat si o comanda sa ii schimb id-ul inapoi: update, accounts,
id=1, profile_img=profile/vader.jpg, username` is not null OR `username=rekt0r

DUPA asta, am obtinut flag-ul SpeishFlag{nA0eBcpak4lHW6CBkScqVEEtNVQMXKZc} si
parola rektor-ului 152360752a

5. Pentru task-ul 5, mai intai am zis sa incerc sa scanez fisierele de pe server
cu nikto (./nikto.pl -h localhost:8080), si am vazut exista un fisier .git. Am
vazut ca nu am putut sa-l descarc cu totul direct, dar in schimb, am putut
descarca fisierele HEAD, index, config folosindu-ma de browser
(localhost:8080/.git/HEAD, etc), si am facut un nou git repo cu ele, dupa care,
dupa un git status am vazut ca exista un fisier .git_flag, pe care l-am
descarcat cu aceasi metoda fara rusine. In el era flag-ul
SpeishFlag{qlj2vEudZlWde5dyDsaNHnBkRiSbf0TX}

6. Pentru 6, am inteles ca trebuie sa sterg folder-ul /var/www dupa ce deschid
portile. Problema era incarcarea script-ului pentru ca form-ul de upload nu
parea sa permita un script.sh, asa ca am incercat sa-l maschez ca fiind jpg, dar
nu a mers, nu a mers nici png si nici bmp, dar for some reason a mers cu gif. Am
incarcat script-ul script.sh mascat ca gif. Dupa care trebuia rulat, si am
vazuzt la fix'em ca rularea unui script se face cu un post request la
/admin/runScript, si nu m-am gandit sa editez calea la script-ul de fix'em sa
fie calea de la bash (scriptu incarcat nu are drepturi de execute) + script, ci
in schimb am facut un script de python, care se logheaza ca rekt0r si ruleaza
acel script :)). De plictiseala, am decis sa automatizez tot task-ul 6 in python.
Calea de la bash + script este ../../../../../bin/sh /var/www/userupload/posts/script.sh.
Flag-ul este SpeishFlag{lqabn1xA7LMprR3FVv8PfFq0Z863qrY0}.