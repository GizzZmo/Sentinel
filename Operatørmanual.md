# Project Sentinel - Operatørmanual
# Versjon 3.0

### 1. Systemoversikt og Filosofi
Formål: Project Sentinel er et avansert beslutningsstøttesystem designet for å gi sikkerhetspersonell en proaktiv evne til å identifisere og mitigere potensielle trusler i sanntid. Systemets kjernefilosofi er ikke å erstatte menneskelig dømmekraft, men å forsterke den. Ved å analysere komplekse dataflyter fra video, lyd og andre sensorer, gir Sentinel operatøren en dypere situasjonsforståelse, slik at de kan ta mer informerte og effektive beslutninger.

Direktiv 7A - Menneskelig Myndiggjøring: All bruk av Project Sentinel skal underlegges Direktiv 7A. Dette innebærer at:

AI er en rådgiver, ikke en beslutningstaker: Systemet gir prediksjoner, analyser og anbefalinger. Den endelige beslutningen om å handle, og hvordan man skal handle, ligger alltid hos den autoriserte menneskelige operatøren.

Fokus på De-eskalering: Systemets primære mål er å identifisere de tidlige tegnene på uro for å muliggjøre proaktive, de-eskalerende tiltak, og dermed forhindre at voldelige situasjoner oppstår.

Integritet og Transparens: All data og alle systemhandlinger skal loggføres for å sikre full sporbarhet og ansvarlighet.

### 2. Protokollforklaringer
Project Sentinel er bygget på en rekke spesialiserte AI-protokoller som jobber sammen for å bygge et helhetlig situasjonsbilde.

2.1 Protokollbeskrivelser
GABRIEL (Integritetsvakt): Verifiserer integriteten og kvaliteten på innkommende data. Sikrer at ansiktsgjenkjenning opererer innenfor definerte kvalitetsparametere.

RAFAEL (Bevegelsesanalyse): Overvåker og analyserer bevegelsesmønstre. Identifiserer uvanlig flukt- eller forfølgelsesatferd, og synkroniserte bevegelser i grupper.

URIEL (Miljøanalyse): Oppdager avvik i det fysiske miljøet. Dette inkluderer deteksjon av potensielt farlige objekter (f.eks. forlatte gjenstander) og plutselige, høye lyder (f.eks. skrik, smell).

AZRAEL (Emosjonsanalyse): Utfører dybdeanalyse av emosjonell tilstand basert på ansiktsuttrykk og (simulert) kroppsspråk. Identifiserer dominerende følelser som sinne, frykt og glede.

SERAPHIM (Signalanalyse): Simulerer triangulering av mobilenheter for å identifisere og spore gruppedannelse og klynger av mennesker, selv uten direkte visuell kontakt.

SANDALPHONE (Sosial Dynamikk): Evaluerer interaksjonen mellom individer og grupper. Analyserer sosial samhørighet, emosjonell smitte og dannelsen av "ingrupper" og "utgrupper".

METATRON (Prediktiv Syntese): Systemets kjerne-AI. Samler data fra alle andre protokoller og bruker Gemini API til å generere en helhetlig risikovurdering og prediktive analyser om sannsynlige fremtidige hendelser.

2.2 Kritikalitetsnivå og Risikobidrag
METATRONs samlede trusselvurdering er en vektet sum av input fra de andre protokollene. Hver protokoll bidrar med en risikoscore basert på alvorlighetsgraden av dens funn. Dette gir en transparent modell for hvordan systemet kommer frem til sine konklusjoner.

URIEL (Miljøavvik):

Deteksjon av forlatt objekt: +3 poeng

Høy lyd (skrik/smell): +2 poeng

AZRAEL (Emosjonsanalyse):

Høy konsentrasjon av "sinne" i gruppe: +2 poeng

Høy konsentrasjon av "frykt" (panikk-indikator): +3 poeng

SANDALPHONE (Sosial Dynamikk):

Rask dannelse av stor, kohesiv gruppe: +2 poeng

Høy negativ energi/smitte mellom grupper: +5 poeng

RAFAEL (Bevegelsesanalyse):

Synkronisert, aggressiv bevegelse mot et mål: +4 poeng

Plutselig, kaotisk bevegelse (flukt): +3 poeng

METATRON summerer og vekter disse poengene for å generere en endelig trusselscore og en anbefaling, som presenteres for operatøren.

### 3. Adferdskodeks og Etiske Retningslinjer
Operatører av Project Sentinel bærer et betydelig ansvar. Følgende retningslinjer er absolutte.

3.1 Kjerneverdier
Bekreft før Handling: En AI-generert alarm er et utgangspunkt for etterforskning, ikke en ordre. Verifiser alltid systemets analyse med direkte observasjon eller annen etterretning før du iverksetter tiltak.

Motstå Automatiseringsbias: Vær bevisst på den psykologiske tendensen til å stole blindt på et automatisert system. Still alltid kritiske spørsmål til systemets konklusjoner.

Respekter Personvern: Systemet skal kun brukes til legitime sikkerhetsformål innenfor rammen av gjeldende lover og forskrifter. Overvåking skal være målrettet og tidsbegrenset.

Rapporter Avvik: Enhver opplevd feil, bias eller uetisk resultat fra systemet skal umiddelbart rapporteres for analyse og systemforbedring.

Beskytt Data: All data generert av systemet er sensitiv. Behandle den med høyeste grad av konfidensialitet og sikkerhet.

3.2 Tilgangsnivåer og Roller
Systemet opererer med et strengt, rollebasert tilgangskontrollsystem for å sikre ansvarlighet og datasikkerhet.

Nivå 1: Observatør (Observer)

Tilgang: Kun lesetilgang til dashboard og sanntidsdata.

Rettigheter: Kan monitorere situasjonen, se alarmer og følge med på operatørhandlinger. Kan ikke iverksette responstiltak, endre systemparametere eller navngi individer.

Formål: Situasjonsforståelse for støttepersonell eller ledere.

Nivå 2: Feltoperatør (Field Operator)

Tilgang: Full tilgang til alle sanntidsanalyse- og responsverktøy.

Rettigheter: Kan justere trusselresponsskala, navngi individer, og aktivere forhåndsdefinerte responshandlinger. Alle handlinger loggføres i Audit-Loggen og krever en kort begrunnelse.

Formål: Den primære brukeren av systemet under en operasjon.

Nivå 3: Administrator (System Administrator)

Tilgang: Full systemtilgang, inkludert konfigurasjon.

Rettigheter: Kan definere og justere regler for protokollene, administrere brukerroller, og sette standardparametere for gjenkjenningstoleranse og trusselresponsskalaer.

Formål: Systemvedlikehold, konfigurasjon og brukeradministrasjon.

3.3 Nødprotokoll: DEUS Override
I ekstraordinære situasjoner der en umiddelbar, overhengende trussel mot liv krever handling som går utenfor standard AI-restriksjoner, kan en autorisert operatør (Nivå 2 eller høyere) aktivere "DEUS Override".

Aktivering: Krever dobbel bekreftelse og en skriftlig begrunnelse for aktivering.

Effekt: Deaktiverer midlertidig AI-anbefalingssløyfen og gir operatøren direkte kontroll over systemets responsverktøy.

Logging: Aktivering av DEUS Override utløser en høyprioritets-hendelse i Audit-Loggen, som krever en etterfølgende gjennomgang og godkjenning av en systemadministrator.

Formål: Sikrer at menneskelig dømmekraft kan overstyre systemet i ekstreme tilfeller, samtidig som det opprettholder en streng ramme for ansvarlighet.

Vedlegg A: Datapipeline og Scenarier
A.1 Visualisering av Datapipeline
Dette er en tekstlig fremstilling ment som grunnlag for en infografikk.

Sensor-input (Kameraer/Mikrofoner): Rå video- og lydstrømmer sendes til systemet.

GABRIEL (Integritet): Data verifiseres for kvalitet og synkronisering.

Parallell Analyse:

URIEL (Miljø): Video analyseres for objekter og avvik.

RAFAEL (Bevegelse): Posisjonsdata analyseres for bevegelsesmønstre.

AZRAEL (Emosjon): Ansikts- og stemmeanalyse for emosjonell tilstand.

SERAPHIM (Signal): Simulerer enhets-klynger.

SANDALPHONE (Sosial Syntese): Data fra RAFAEL, AZRAEL og SERAPHIM kombineres for å bygge en sosial interaksjonsgraf.

METATRON (Prediktiv Analyse): Mottar all prosessert data fra URIEL og SANDALPHONE. Sender en syntese til Gemini API for en helhetlig risikovurdering og anbefaling.

Operatørdashboard: Viser den endelige analysen og anbefalingen til operatøren.

A.2 Scenario-eksempler for Trening
Scenario 3.4.1: Plutselig gruppedannelse nær kritisk infrastruktur

Kl. 12:01:05: SERAPHIM detekterer en rask økning av enheter i Sone C.

Kl. 12:01:45: SANDALPHONE identifiserer to distinkte, men geografisk nære grupper (Gruppe A, Gruppe B). Intern energi er nøytral.

Kl. 12:02:30: AZRAEL rapporterer en kraftig økning i "sinne" og "forakt" i Gruppe A, korrelert med at Gruppe B beveger seg nærmere.

Kl. 12:02:55: METATRON predikerer: Høy sannsynlighet (93%) for verbal konflikt innen 2 minutter. Risiko for eskalering til fysisk konfrontasjon. Anbefaling: Etabler visuell tilstedeværelse mellom gruppene. Hev systemets trusselrespons til GUL.

Operatørhandling: Operatøren logger "Anbefaling fulgt", setter responsskalaen til GUL, og dirigerer en patrulje til Sone C med instruks om å skape en synlig, nøytral barriere.

Scenario 5.1.2: Koordinert, unormal bevegelse

Kl. 22:50:10: RAFAEL flagger en anomali: Tre individer (Person 12, 15, 21) beveger seg i en synkronisert, uvanlig rask formasjon gjennom et normalt rolig område.

Kl. 22:50:40: AZRAEL rapporterer at alle tre individene viser lav emosjonell respons ("nøytral" med høy konfidens), noe som er atypisk for den observerte hastigheten. Dette indikerer potensiell målrettet, planlagt handling.

Kl. 22:51:05: METATRON predikerer: Koordinert bevegelse med lav emosjonell signatur indikerer høy grad av intensjon. Potensial for innbrudd eller hærverk mot mål i bevegelsesretningen. Anbefaling: Følg individene på live monitor og varsle patrulje i Sone A om mulig innkommende aktivitet.

Operatørhandling: Operatøren dedikerer et panel til å følge de tre individene og gir en forhåndsvarsel til relevant patrulje.
