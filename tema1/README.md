# Paunoiu Darius Alexandru - 342CD - Tema 1 TSSC

Rezolva aceste task-uri cu mine in 10 pasi simplii

## Task 1

1. Telnet la adresa de am primit-o sa vedem ce e pe acolo
2. Primim un string **dubios** pe care facem Base64 decode
3. Vedem ca obtinem un json cu elementele pt `Diffie Hellman`
4. Trecem totul intr-un script de python cu socket tcp
5. Repetam pasii de mai sus in python si raspundem un `B` calculat cu formula `g
   ^ b % p`, `b` ales aleator
6. Primim alt string dubios pe care-l decodam cu base64, obtinem json cu un
   mesaj si o sare
7. DECODAM IAR 64 VALORILE DE LA MSG Si SALT ??? (WHY DE CE 2 ORI M AM SUIT PE
   PERETI O ZI INTREAGA PT ASTA)
8. Luam cheia cu `get_aes_key` folosing `sarea` si `shared_num` egal cu cheia
   `Diffie Hellman` adica $A^b$ % p
9. Decodam msg
10. Obtinem **flag-ul**

## Task 2

1. Facem `ssh` cu cheia privata primita la adresa extrasa din cheia publica
2. Ne uitam ca **fraierii** si nu vedem decat suntem un parlit si exista un
   admin
3. Incercam sa intram in adminel, dar nu avem Jack The Ripper sau access pe
   /etc/shadow deci **renuntam** la acest plan
4. Folosim `find` sa gasim **flag-ul** la `/usr/share/vim/talent/xyzflag` si mai
   multe **hint-uri** (doar 1...... la
   `/usr/src/linux/headers/angry_torvalds/.hints.txt` cu urmatorul continut)

   ```txt
   Here's more hints:

   - Gandalf giving you problems? try the magic words `ltrace`...
   - `find` is your friend (helped you find this);
   - 16iyemkx 19aypjr 23vxlg 17krwjarnb 12kwhv 18XIBP 22zevmefpiw!
   ```

5. Cautam 2-3-5-12-24 ore alte cuvinte **cheie**, gen hunt, hack, friend etc...
   Dar macar ne dam seama ca string-ul dubios din hint e codificare cu cezar cu
   shiftare de 26 - numar din fata...Il rezolvam manual... Si obtinem **you can
   trick suid binaries with path variables**
6. Gasim o comanda smechera care ne arata ce fisiere au `suid` setat (`find /
   -type f -perm /4000 2>/dev/null`)
7. Gasim un executabil `/var/lib/initscripts/hi/indestructibil.x` ... Cu
   siguranta ma *gandeam* la numele astea....
8. Vedem cu `strings` cam care e faza cu el, are un string dubios si il rulam cu
   acel string
9. Folosim `ltrace`, vedem ca face un apel de executabil `file`
10. Ne scriem propriul `file` care face `cat` pe **flag**, il adaugam in `$PATH`
    si obtinem **flag-ul**

## Task 3

1. Rulam `casino` - ul sa vedem cu ce se mananca dar pierdem toti banii....
2. Ne suim pe pereti ca nu avem codul sursa, trebuie sa instalam `ghidra` si ne
   simtim ca la iocla
3. Ne uitam pe decompilare, vedem ca citirea de numere se face la infinit si o
   *abuzam*
4. Nu prea stim sa calculam cati octeti sunt pana la eip, deci facem un `for` de
   la 30 la 100 si obtinem 56, trecem in pwndbg in python
5. Vedem ca nu merge deloc, si realizam ca citirea se face de un `int` si nu de
   `hex`
6. Luam adresa din `hexa` `0x8049256` a lui `win` si o facem in `decimal` `134517334`
7. Vedem ca intram in `win`, dar nu avem parametrul setat bine ca nu stim cat e
   *lucky number* (e random la fiecare rulare)
8. Dupa 30 de minute de dispare, realizam ca dupa *nume de joc* in globale vine
   imediat *lucky number*, iar citirea de *nume* nu e limita
9. Introducem un *nume* de 36 de caractere ca sa nu mai existe niciun `\0`
10. Facem niste hack-uri sa extragem *lucky number* dintr-un string cu multe
    B-uri (ca sa nu fie A-uri), nu uitam ca e in little endian, convertim cum
    trebuie, ii dam send, si obtinem *flag-ul*

## Extra notes

Script-urile de rezolvare a temei folosite sunt flagz0rx.py pentru task-ul 1
si exploit.py [local/remote] pentru task-ul 3, task-ul 2 fiind rezolvat manual.
Script-ul exploit.py are mesaje ajutatoare de folosire.

## Va multumesc pentru urmarirea acestui tutorial, lasa-ti un like si un comm
