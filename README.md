# SPAtaREST
## Scopul aplicației
Scaunul smart SPAtaREST revoluționează modul în care stai la birou, crearea lui având ca scop îmbunătățirea vieții și a sănătății fizice a utilizatorului, precum și oferirea unui confort sporit pentru a face posibilă o utilizare day to day cu un program de lucru scurt, mediu sau lung. Acest scaun are ca scop să ofere utilizatorului un adevărat spa la birou prin ajustarea caracteristicilor fizice ale scaunului în așa fel încât să ofere confort maxim utilizatorului și să mențină utilizatorul într-o poziție anatomic corectă.

## Obiectivele aplicației
* reglarea automată a spătarului, a înălțimii, a mânerelor pentru a oferi confort maxim fiecărui utilizator, indiferent de înălțime, greutate sau alte particularități corporale

* ajustarea temperaturii scaunului pentru a livra productivitate maximă atât vara cât și iarnă, indiferent de temperatura de afară sau din încăpere

* log off și log in cu senzor de amprentă pentru a oferi utilizatorului un boost de încredere și de siguranță

* reminder când ai stat prea mult jos pentru că nici măcar SPAtaREST nu elimină necesitatea de a te ridica în picioare pentru a te întinde puțin

* scaun user friendly care te salută și îți ține băutura caldă pentru a simți cu adevărat că acest scaun este un companion bun încă de când te așezi pe el

* software ușor de folosit care fluidizează procesele fizice ale scaunului

## Grupul țintă
* Ca angajat care lucrează cu date confidențiale, mi-ar plăcea ca atunci când mă ridic de pe scaun, computerul la care lucrez să fie securizat automat, fără să fie nevoie să securizez eu manual fișierele. 

* Ca gamer, îmi doresc ca scaunul meu să îmi permită să stau ore în șir așezat fără să mă doară spatele și fără să fie nevoie să îl ajustez eu în permanentă. 

* Ca student pe timpul pandemiei, îmi doresc să am un scaun care să poată fi utilizat de dimineață devreme până seară târziu, dar care să mă și mențină sănătos din punct de vedere al posturii. 

* Ca medic, îmi doresc ca scaunul pe care stau toată ziua să aibă un suport lombar corect, să aibă mânerele reglabile în așa fel încât să pot să le ajustez în funcție de înălțimea mea și a biroului și să aibă un mecanism fizic de reglare ușor de utilizat, fără 10 tipuri diferite de șuruburi și 12 piulițe, ca să pot să îl reglez în cabinet. 

* Ca angajat într-o corporație, îmi doresc să am un scaun care să nu mă facă să transpir vara și să îngheț iarnă.

* Ca pensionar cu hernie de disc, îmi doresc un scaun care să îmi susțînă bine coloana pentru a nu agrava boală, care să aibă încălzire pentru că de la o vârstă e nevoie și care să îmi amintească periodic să mă ridic și să mă plimb, pentru că mă pot pierde în integrame. Dacă poate și să îmi țină ceaiul cald, e ideal. 


## Colectarea cerințelor

1. când utilizatorul se ridică de pe scaun să se dea pc-ul lock/când se pune pe scaun să apară login

2. fingerprint sensor (integrare cu windows hello?)

3. spătarul să se ajusteze automat în funcție de postura utilizatorului (senzor de presiune)

4. scaunul să regleze automat înălțimea în funcție de date biometrice introduse de utilizator

    input: înălțime utilizator, înălțime nivel birou (tastatură și mouse), înălțime nivel monitor

5. ajustare automată hand rests

6. desktop software (driver) pentru date biometrice

7. încălzire în scaun (în funcție de temperatura din camera)

    note: să comunice prin mqtt cu un smart thermostat

8. să îți țină băutura caldă

9. să se lase pe spate automat

10. boxe integrate în scaun care să te salute

11. să-ți zică să te mai ridici când stai prea mult

## Interpretarea și prioritizarea cerințelor

### Cerințe funcționale : 

-când utilizatorul se ridică de pe scaun să se dea pc-ul lock/când se pune pe scaun să apară login

-spătarul să se ajusteze automat în funcție de postura utilizatorului (senzor de presiune)

-scaunul să regleze automat înălțimea în funcție de date biometrice introduse de utilizator

-încălzire în scaun (în funcție de temperatura din cameră)

-să îți țină băutura caldă

-boxe integrate în scaun care să te salute

-să-ți zică să te mai ridici când stai prea mult

### Cerințe nonfunctionale:

-fingerprint sensor (integrare cu windows hello?)

-ajustare automată hand rests

-desktop software (driver) pentru date biometrice

-să se lase pe spate automat

 ### Cerințe care țin de sănătate, securitate, modificări fizice ale scaunului

* când utilizatorul se ridică de pe scaun să  dea pc-ul lock/când se pune pe scaun să apară login

* fingerprint sensor (integrare cu windows hello?)

* spătarul să se ajusteze automat în funcție de poziția utilizatorului (senzor de presiune)

* scaunul să regleze automat înălțimea în funcție de date biometrice introduse de utilizator

* input: înălțime utilizator, înălțime nivel birou (tastatură și mouse), înălțime nivel monitor

* ajustare automată hand rests

### Cerințe care țin de software, quality of life, control din driver

* desktop software (driver) pentru date biometrice

* încălzire în scaun (în funcție de temperatura din cameră)

* să comunice prin mqtt cu un smart thermostat

* să îți țină băutură caldă

* să se lase pe spate automat

* boxe integrate în scaun care să te salute

* să-ți zică să te mai ridici când stai prea mult
