# SPAtaREST
## Scopul aplicației
Scaunul smart „SPAtaREST” revoluționează modul în care stai la birou, crearea lui având ca scop îmbunătățirea vieții și a sănătății fizice a utilizatorului prin oferirea unui confort sporit pentru a face posibilă o utilizare day to day cu un program de lucru scurt, mediu sau lung. Acest scaun oferă utilizatorului un adevărat spa la birou prin ajustarea caracteristicilor fizice ale scaunului în așa fel încât să ofere confort maxim utilizatorului și să mențină utilizatorul într-o poziție anatomic corectă.


## Obiectivele aplicației
* ajustarea temperaturii scaunului pentru a livra productivitate maximă atât vara cât și iarna
* software ușor de folosit pentru introducerea și vizualizarea datelor
* reglarea automată a înălțimii pentru a oferi confort maxim fiecărui utilizator
* opțiunea de a da lock automat atunci când utilizatorul se ridică de pe scaun pentru a-i ușura experiența utilizării computerului
* reminder când ai stat prea mult jos pentru că nici măcar SPAtaREST nu elimină necesitatea de a te ridica în picioare pentru a te întinde puțin
* măsurarea greutății utilizatorului și afișarea acesteia pentru a putea a-și putea vizualiza evoluția

Obiective pe care le vom dezvolta în viitor:
* scaun user friendly care te salută și îți ține băutura caldă pentru a simți cu adevărat că acest scaun este un companion bun încă de când te așezi pe el
* fingerprint sensor pentru o deblocare mai ușoară a computerului


## Grupul țintă
* Ca angajat care lucrează cu date confidențiale, mi-ar plăcea ca atunci când mă ridic de pe scaun, computerul la care lucrez să fie securizat automat
* Ca gamer, îmi doresc ca scaunul meu să îmi permită să stau ore în șir așezat fără să mă doară spatele și fără să fie nevoie să îl ajustez eu în permanentă.
* Ca student pe timpul pandemiei, îmi doresc să am un scaun care să poată fi utilizat de dimineață devreme până seară târziu, dar care să mă și mențină sănătos din punct de vedere al posturii.
* Ca medic, îmi doresc ca scaunul pe care stau toată ziua să aibă un suport lombar corect, să aibă înălțimea reglabilă în așa fel încât să pot să o ajustez în funcție de înălțimea mea, printr-un mecanism ușor de utilizat.
* Ca angajat într-o corporație, îmi doresc să am un scaun care să nu mă facă să transpir vara și să îngheț iarnă.
* Ca pensionar cu hernie de disc, îmi doresc un scaun care să îmi susțină bine coloana pentru a nu agrava boală, care să aibă încălzire pentru că de la o vârstă e nevoie și care să îmi amintească periodic să mă ridic și să mă plimb, pentru că mă pot pierde în integrame.
* Ca utilizator atehnic, îmi doresc un scaun cu care să pot interacționa ușor și intuitiv.
* Ca utilizator preocupat de sănătatea mea, îmi doresc un scaun care să mă mențină într-o poziție ergonomică și care să mă informeze constant de schimbările în greutate datorate sedentarismului.



## Colectarea cerințelor
* când utilizatorul se ridică de pe scaun să se dea PC-ul lock
* când se pune pe scaun să apară login
* scaunul să-și regleze automat înălțimea în funcție de înălțimea introdusă de utilizator
* biroul să-și regleze automat înălțimea în funcție de înălțimea introdusă de utilizator
* spătarul să se ajusteze automat în funcție de poziția utilizatorului (senzor de presiune)
* ajustare automată hand-rests
* să se lase pe spate automat
* desktop software (driver) pentru introducerea și vizualizarea datelor
* să-ți zică să te ridici când stai prea mult pe scaun
* preluarea temperaturii din cameră și încălzire scaunului
* măsurarea greutății utilizatorului
* afișarea greutății utilizatorului în driver
* să îți țină băutura caldă
* boxe integrate în scaun care să te salute
* crearea server-ului flask
* crearea si conectarea la baza de date
* realizarea specificației OpenAPI
* realizarea specificației AsyncAPI
* realizarea documentului de utilizare
* realizarea testelor corespunzătoare pentru aplicație
* crearea unui borker MQTT


## Interpretarea și prioritizarea cerințelor
### Cerințe funcționale : 
* când utilizatorul se ridică de pe scaun să se dea PC-ul lock 
* când se pune pe scaun să apară login
* spătarul să se ajusteze automat în funcție de postura utilizatorului (senzor de presiune)
* scaunul să-și regleze automat înălțimea în funcție de înălțimea introdusă de utilizator
* biroul să-și regleze automat înălțimea în funcție de înălțimea introdusă de utilizator
* ajustare automata hand-rests
* încălzire scaunului
* să se lase pe spate automat
* să îți țină băutura caldă
* boxe integrate în scaun care să te salute
* să-ți zică să te ridici când stai prea mult
* afișarea în driver a greutății

### Cerințe nonfunctionale:
* fingerprint sensor
* ajustare automată hand rests
* desktop software (driver) pentru introducerea și vizualizarea datelor
* preluarea temperaturii din cameră
* să se lase pe spate automat
* crearea server-ului flask
* realizarea specificației OpenAPI
* realizarea specificației AsyncAPI
* crearea si conectarea la baza de date
* preluarea greutății utilizatorului
* realizarea documentului de utilizare
* realizarea testelor corespunzătoare pentru aplicație
* crearea unui broker MQTT

 ### Cerințe care țin de sănătate, securitate, modificări fizice ale scaunului
* când utilizatorul se ridică de pe scaun să se dea PC-ul lock 
* când se pune pe scaun să apară login
* fingerprint sensor
* spătarul să se ajusteze automat în funcție de poziția utilizatorului (senzor de presiune)
* scaunul să-și regleze automat înălțimea în funcție de înălțimea introdusă de utilizator
* biroul să-și regleze automat înălțimea în funcție de înălțimea introdusă de utilizator
* ajustare automată hand rests
* afișarea greutății utilizatorului

### Cerințe care țin de software, quality of life, control din driver
* desktop software (driver) pentru date biometrice
* încălzire în scaun (în funcție de temperatura din cameră)
* să comunice prin mqtt cu un smart thermostat
* preluarea greutății utilizatorului
* să îți țină băutură caldă
* să se lase pe spate automat
* boxe integrate în scaun care să te salute
* să-ți zică să te mai ridici când stai prea mult


![Plotarea POKERSCRUM](https://github.com/andreitudose2000/ingineria-programarii/blob/main/docs/Poker.png)
