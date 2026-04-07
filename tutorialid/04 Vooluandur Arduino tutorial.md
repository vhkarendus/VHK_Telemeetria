# WCS1700 Hall Current Sensor kasutamine Arduinoga

## Sisukord
1. [Mis on vooluandur?](#1-mis-on-vooluandur)
2. [WCS1700 Hall anduri põhimõtted](#2-wcs1700-hall-anduri-põhimõtted)
3. [WCS1700 ühendamine](#3-wcs1700-ühendamine)
4. [Voolutugevuse lugemine](#4-voolutugevuse-lugemine)
5. [Kalibreerimine](#5-kalibreerimine)
6. [Testimine DC mootoriga](#6-testimine-dc-mootoriga)

---

## 1. Mis on vooluandur?

### Definitsioon

**Vooluandur** (current sensor) on seade, mis mõõdab elektrivoolu tugevust (amprid) ja annab väljundiks pinge, mis on proportsionaalne mõõdetava vooluga.

**Erinevad anduritüübid:**
- **Non-invasive** andurid - kaabel läbib anduri ilma vooluringi katkestamata (nt WCS1700, CT)
- **Invasive** andurid - vool läbib anduri enda pinde, vajab vooluringi katkestamist (nt ACS712, shunt)

### Vooluandurite tüübid

#### 1. Hall-efekti andurid (Hall Current Sensors) ⭐

**Põhimõte:** Kasutavad Hall-efekti - magnetväli (mille tekitab vool juhtmes) mõjutab anduris olevat pooljuhti

**Kaks peamist tüüpi:**

**A) Läbiviimisel põhinevad (Through-hole) - WCS1700, WCS1800**
- Kaabel/juhe läheb **augu läbi**
- Non-invasive - vooluringi ei pea katkestama
- Lihtne paigaldamine
- Vahemik: 0-70A, 0-100A

**B) Integreeritud juhtmega (Integrated conductor) - ACS712, ACS758**
- Vool läbib anduri **enda pinde** (IP+/IP-)
- Kompaktsem
- Vajab vooluring katkestamist
- Vahemik: 5A-200A

**Plussid:**
- ✅ Mõõdab AC ja DC voolu
- ✅ Galvaaniline eraldus (isolatsioon)
- ✅ Lineaarne väljund
- ✅ Odav ja lihtne kasutada

**Miinused:**
- ❌ Väiksem täpsus (~1-2%)
- ❌ Temperatuuri drift

#### 2. Voolutransformaatorid (Current Transformers - CT)

**Põhimõte:** Elektromagnetiline induktsioon - primaarvool tekitab sekundaarvoolu

**Näited:**
- YHDC SCT-013 (100A AC)
- Split-core CT-d

**Plussid:**
- ✅ Väga täpne AC mõõtmiseks
- ✅ Kõrge vooluvahemik
- ✅ Kaabel läheb augu läbi

**Miinused:**
- ❌ **Ainult AC vool** (ei tööta DC'ga!)
- ❌ Vajab lisaelektroonika
- ❌ Suurem ja kallim

#### 3. Shunt takistid (Shunt Resistors)

**Põhimõte:** Oomi seadus - mõõdame pingelangust väikese takisti otstel

**Näited:**
- 0.1Ω shunt takisti
- INA219 (shunt + IC)

**Plussid:**
- ✅ Väga täpne
- ✅ Odav

**Miinused:**
- ❌ **Pole galvaanilist eraldust** (ohtlik!)
- ❌ Võimsuskadu (shunt kuumeneb)
- ❌ Vajab diferentsiaalvõimendi

### Võrdlustabel

| Omadus | WCS1700 | ACS712 | CT | Shunt |
|--------|---------|--------|-----|-------|
| **DC vool** | ✅ Jah | ✅ Jah | ❌ Ei | ✅ Jah |
| **AC vool** | ✅ Jah | ✅ Jah | ✅ Jah | ✅ Jah |
| **Paigaldamine** | Kaabel läbib augu | IP+/IP- pinid | Kaabel läbib augu | Jadasse |
| **Isolatsioon** | 4000V | 2.1kV | ✅ Jah | ❌ Ei |
| **Täpsus** | ~1-2% | ~1.5% | ~0.5% | ~0.1% |
| **Vahemik** | 0-70A | 5-30A | 1-1000A+ | 0.1-100A |
| **Hind** | € (~€5) | € (~€3) | €€ | € |

---

## 2. WCS1700 Hall anduri põhimõtted

### Mis on Hall-efekt?

**Hall-efekt** on füüsikaline nähtus, kus magnetväli mõjutab elektrivoolu suunda pooljuhtmaterjalis.

**WCS1700 puhul:**
1. **Toitekaabel** (mida me tahame mõõta) läbib kaablit/juhet
   - Näiteks: aku → mootor kaabel
   - Või: toiteallikas → kogu süsteem kaabel
2. See kaabel tekitab **magnetvälja** ümber enda
3. Kaabel läheb **9mm augu läbi** WCS1700's
4. Magnetväli mõjutab Hall-elementi anduri sees
5. Tekib **väljundpinge** proportsionaalne vooluga

**Oluline:** Me ei ühenda WCS1700 mitte kuidagi elektriliselt toitekaabliga - kaabel lihtsalt läbib augu füüsiliselt!

**Valem:**

$$V_{out} = V_{ref} + Sensitivity × I$$

### WCS1700 spetsifikatsioon

**Peamised parameetrid:**
- **Tootja:** Winson Semiconductor
- **Tööpinge:** 3-12V (5V soovitatud)
- **Mõõtevahemik:** 0-70A (ühesuunaline)
- **Tundlikkus:** ~36mV/A (0.036V/A)
- **Null-voolu väljund (V_ref):** VCC/2 (2.5V kui VCC=5V)
- **Augu läbimõõt:** 9.0mm
- **Täpsus:** ±1%
- **Ribalaius:** 23kHz
- **Isolatsioon:** 4000V RMS
- **Töötemperatuur:** -20°C kuni +85°C
- **Voolutarve:** ~3mA

**Väljundpinge valem (5V toitel):**

$$V_{out} = 2.5V + 0.036V/A × I$$

**Näited:**
- $I = 0A$ → $V_{out} = 2.5V$
- $I = +10A$ → $V_{out} = 2.5V + 0.36V = 2.86V$
- $I = +35A$ → $V_{out} = 2.5V + 1.26V = 3.76V$
- $I = +70A$ → $V_{out} = 2.5V + 2.52V = 5.02V$ (maksimum!)

**OLULINE:** WCS1700-l on mitmeid versioone:
- **WCS1700** - 0-70A ühesuunaline
- Mõned versioonid võivad mõõta ka negatiivset voolu (±35A)
- Kontrolli alati andmelehte!

### Pinni konfiguratsioon

WCS1700 moodulil on **4 pind**:

```
    ┌──────────────┐
    │   WCS1700    │
    │              │
    │   [  O  ]    │ ← 9mm auk (kaabel siia läbi!)
    │              │
    ├──────────────┤
 1. │ VCC          │ ← Toitepinge (5V)
 2. │ GND          │ ← Maandus
 3. │ Aout         │ ← Analoogne väljund (→ Arduino A0)
 4. │ Dout         │ ← Digitaalne väljund (comparator)
    └──────────────┘
```

**Pinnide funktsioonid:**
- **VCC** - Toitepinge (soovitatud 5V)
- **GND** - Maandus
- **Aout** - Analoogne väljundpinge (proportsionaalne vooluga)
- **Dout** - Digitaalne väljund (ülekoormuse võrdleja, vajadusel)

![WCS1700 pildid](images\04-vooluandur\04-vooluandur.png)

---

## 3. WCS1700 ühendamine

### Testimiseks Põhiskeem


![WCS1700 ühenduse skeem](images\04-vooluandur\04-vooluandur_skeem_Arduino.png)

Kuidas vooluahel peaks välja nägema:

![WCS1700 ühenduse skeem](images\04-vooluandur\04-ahel_kokku.jpg)

### Kaabli läbiviimine

**Kriitilised punktid:**

1. **MILLINE kaabel läbib auku?**
   - See on **toitekaabel**, mille voolu me tahame mõõta
   - Näiteks testimisel: patarei → mootor kaabel
   - Päris autol: aku → terve süsteem kaabel
   - **Mitte** WCS1700 enda toitekaabel (VCC/GND)!

2. **Kaabel peab läbima 9mm augu** WCS1700 valges plokis
   - Maksimaalne juhtme läbimõõt: ~7-8mm
   - Võib läbida paljad juhtmed või isoleeritud kaabli
   - **Ainult üks juhe** augu kaudu (+ VÕI -, mitte mõlemad korraga!)

3. **Voolu suund määrab polaarsuse**
   - Vool ühes suunas → pinge tõuseb
   - Vool vastupidises suunas → pinge langeb (kui toetab ±)

4. **Mitmekordne läbiviimine suurendab tundlikkust**
   - 1x läbi → 36mV/A
   - 2x läbi (loop) → 72mV/A
   - N korda läbi → N × 36mV/A

**Praktiline ühendamine:**

**Komponendid:**
- Arduino (Uno, Nano, Mega)
- WCS1700 vooluandur mooduli
- DC mootor või muu koormus (testimiseks)
- Toiteallikas (6-12V)
- Juhtmed

**Sammud:**

1. **Arduino toide WCS1700'le:**
   - Arduino GND → WCS1700 GND
   - Arduino 5V → WCS1700 VCC

2. **Signaal:**
   - WCS1700 Aout → Arduino A0
   - WCS1700 Dout → (valikuline, ei kasuta selles tutorialis)

3. **Vooluahel:**
   - Koormuse - → Toiteallikas -
   - Toiteallikas + → **Kaabel**
   - **Kaabel läbi WCS1700 augu**
   - Kaabel → Koormuse (mootori) +

4. **Kontrolli:**
   - ✅ Kaabel läbib valget auku
   - ✅ Aout on ühendatud A0'ga
   - ✅ VCC on 5V (Arduino'lt)
   - ✅ Ühine GND

**OLULINE:** 
- ❌ **Ära ühenda** mootori vooluringi Arduino GND'ga otse!
- ❌ **Ära ühenda** toiteallika + koos Aruinoga!
- ✅ Kasuta ainult **ühist GND**. Toiteallika GND ja Arduino GND peavad olema oma vähelt ühendatud.
- ✅ Mootori vooluahel on **galvaaniliselt eraldatud** (4000V isolatsioon)

---

## 4. Voolutugevuse lugemine

### ADC meenutus

Arduino ADC teisendab **analoogse** pinge **digitaalseks** väärtuseks:
- **Lahutus:** 10-bit → $2^{10} = 1024$ sammu (0-1023)
- **Vahemik:** 0V kuni 5V
- **Täpsus:** $\frac{5V}{1024} ≈ 4.88mV$ per samm


Järgmise samuga saad hakkata testima vooluandur.

### Kood 1: Toor ADC väärtused

```cpp
const int CURRENT_PIN = A0;

void setup() {
  Serial.begin(9600);
  Serial.println("WCS1700 - ADC lugemine");
  Serial.println("ADC väärtus");
}

void loop() {
  int adc = analogRead(CURRENT_PIN);
  Serial.println(adc);
  delay(100);
}
```

**Mida peaksid nägema:**
- **Koormus väljas:** ~512 (2.5V - null-punkt)
- **Koormus sees:** >512 (sõltub voolu suunast)
- **Mootor töötab:** väärtus tõuseb

### Kood 2: Pinge arvutamine
```cpp
const int CURRENT_PIN = A0;
const float VCC = 5.0;  // Arduino toitepinge

void setup() {
  Serial.begin(9600);
  Serial.println("WCS1700 - Pinge mõõtmine");
}

void loop() {
  int adc = analogRead(CURRENT_PIN);
  
  // Teisenda ADC → Volt
  float voltage = adc * (VCC / 1023.0);
  
  // Serial Plotter formaat
  Serial.print("ADC:");
  Serial.print(adc);
  Serial.print("\tPinge(V):");
  Serial.println(voltage, 3);  // 3 kohta pärast koma
  
  delay(100);
}
```

**Mida peaksid nägema:**

**Serial Monitor'is:**
```
ADC:512   Pinge(V):2.500
ADC:515   Pinge(V):2.515
ADC:510   Pinge(V):2.495
```

**Serial Plotter'is:**
- Kaks joonist: "ADC" (512 ümber) ja "Pinge(V)" (2.5V ümber)
- Kui koormus on väljas → stabiilne joon ~2.5V juures
- Kui lülitad koormuse sisse → pinge tõuseb
- Kui koormus töötab → joon kõrgem kui 2.5V


### Kood 3: Voolutugevuse arvutamine
Selle koodiga saad hästi visualiseerida Serial plotter-iga kuidas vool muutub mootori nuppu vajutades:
```cpp
const int CURRENT_PIN = A0;
const float VCC = 5.0;              // Arduino toitepinge  
const float SENSITIVITY = 0.036;    // 36mV/A = 0.036V/A
const float V_REF = 2.5;            // Null-voolu pinge (VCC/2)

void setup() {
  Serial.begin(9600);
  Serial.println("WCS1700 - Voolu mõõtmine");
}

void loop() {
  // Loe ADC
  int adc = analogRead(CURRENT_PIN);
  
  // Teisenda ADC → Volt
  float voltage = adc * (VCC / 1023.0);
  
  // Arvuta vool
  // I = (V_out - V_ref) / Sensitivity
  float current = (voltage - V_REF) / SENSITIVITY;
  
  // Serial Plotter formaat
  Serial.print("Vool(A):");
  Serial.print(current, 2);  // 2 kohta pärast koma
  Serial.print("\tPinge(V):");
  Serial.println(voltage, 3);
  
  delay(100);
}
```

**Valem selgitus:**

$$I = \frac{V_{out} - V_{ref}}{Sensitivity}$$

$$I = \frac{V_{out} - 2.5V}{0.036V/A}$$

**Näide:**
- $V_{out} = 2.86V$
- $I = \frac{2.86 - 2.5}{0.036} = \frac{0.36}{0.036} = 10A$ ✅

**Mida peaksid nägema:**

**Serial Plotter'is:**
- Kaks joonist: "Vool(A)" ja "Pinge(V)"
- **Koormus väljas (mootor seisab):**
  - Vool(A): ~0.0A (võib olla väike nihe ±0.2A)
  - Pinge(V): ~2.5V
- **Koormus töötab (mootor pöörleb):**
  - Vool(A): >0A (nt 1-3A sõltuvalt mootori koormusest)
  - Pinge(V): >2.5V (nt 2.86V kui vool on 10A)
- **Käivitamisel:**
  - Lühike piik (2-3x suurem vool)
  - Siis stabiliseerub

---

## 5. Kalibreerimine

### Miks on vaja kalibreerida?

WCS1700-l võivad olla:
1. **Null-punkti nihe** - $V_{ref}$ ei ole täpselt VCC/2
2. **Tundlikkuse viga** - tegelik tundlikkus erineb 36mV/A'st
3. **Temperatuuri drift** - muutub temperatuuriga
4. **Arduino ADC viga** - VCC ei ole täpselt 5.00V

### Meetod 1: Null-punkti kalibreerimine

**Eesmärk:** Leia täpne $V_{ref}$ väärtus

**Sammud:**
1. Ühenda WCS1700 Arduino'ga
2. **OLULINE:** **Eemalda kaabel august** või lülita koormus välja (vool = 0A)
3. Käivita kalibreerimise kood
4. Mõõda keskmist pinget
5. Kasuta seda $V_{ref}$ väärtust koodis

```cpp
// Null-punkti kalibreerimine
const int CURRENT_PIN = A0;
const float VCC = 5.0;

void calibrateZero() {
  Serial.println("Null-punkti kalibreerimine...");
  Serial.println("EEMALDA kaabel WCS1700 august!");
  delay(3000);
  
  float sum = 0;
  int samples = 100;
  
  for (int i = 0; i < samples; i++) {
    int adc = analogRead(CURRENT_PIN);
    float voltage = adc * (VCC / 1023.0);
    sum += voltage;
    delay(10);
  }
  
  float calibratedVRef = sum / samples;
  
  Serial.print("Kalibreeritud V_ref = ");
  Serial.print(calibratedVRef, 4);
  Serial.println(" V");
  Serial.println("");
  Serial.println("Kasuta seda väärtust koodis:");
  Serial.print("const float V_REF = ");
  Serial.print(calibratedVRef, 4);
  Serial.println(";");
}

void setup() {
  Serial.begin(9600);
  calibrateZero();
}

void loop() {
  // Tühi - kalibreerimine käib ainult setup()'is
}
```

### Meetod 2: Tundlikkuse kalibreerimine
Kui teise meetodiga kalibreeritud, siis seda pole vaja teha.

**Vajad:** Multimeeter (voolumõõtmise režiimis)

**Sammud:**
1. Ühenda multimeeter **jadas** koormusega
2. Loe multimeetriga tegelik vool
3. Loe Arduino näit
4. Arvuta tegelik tundlikkus

$$Sensitivity = \frac{V_{out} - V_{ref}}{I_{tegelik}}$$

**Näide:**
- Multimeeter: $I = 10.0A$
- Arduino: $V_{out} = 2.86V$
- $V_{ref} = 2.50V$ (kalibreeritud)
- $Sensitivity = \frac{2.86 - 2.50}{10.0} = \frac{0.36}{10.0} = 0.036V/A$ ✅

Kui tulemus erineb 0.036'st, kasuta uut väärtust!

---


### Täiustatud kood: Libisev keskmine

```cpp
const int CURRENT_PIN = A0;
const float VCC = 5.0;
const float SENSITIVITY = 0.036;    // WCS1700: 36mV/A
const float V_REF = 2.5;

// Silumise parameetrid
const int SAMPLE_COUNT = 10;
float samples[SAMPLE_COUNT];
int sampleIndex = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("Vool(A),Vool_silu(A)");
  
  // Täida massiiv algväärtusega
  for (int i = 0; i < SAMPLE_COUNT; i++) {
    samples[i] = 0;
  }
}

float readCurrent() {
  int adc = analogRead(CURRENT_PIN);
  float voltage = adc * (VCC / 1023.0);
  return (voltage - V_REF) / SENSITIVITY;
}

float getSmoothedCurrent(float newCurrent) {
  samples[sampleIndex] = newCurrent;
  sampleIndex = (sampleIndex + 1) % SAMPLE_COUNT;
  
  float sum = 0;
  for (int i = 0; i < SAMPLE_COUNT; i++) {
    sum += samples[i];
  }
  return sum / SAMPLE_COUNT;
}

void loop() {
  float current = readCurrent();
  float smoothed = getSmoothedCurrent(current);
  
  // CSV formaat Serial Plotter'ile
  Serial.print(current, 2);
  Serial.print(",");
  Serial.println(smoothed, 2);
  
  delay(50);
}
```

---
## 6. Testimine DC mootoriga

### Testimise komplekt

**Komponendid:**
- Arduino Uno/Nano
- WCS1700 vooluandur moodul
- DC mootor (6-12V, 0.5-2A)
- Toiteallikas (9V aku või 12V adapter, vähemalt 2A)
- LED + 220Ω takisti (ülekoormuse näidik)
- Multimeeter (võrdluseks, valikuline)
- Breadboard ja juhtmed

### Test 1: Lihtne voolu monitooring

**Kood:**
```cpp
const int CURRENT_PIN = A0;
const float VCC = 5.0;
const float SENSITIVITY = 0.036;  // 36mV/A
const float V_REF = 2.50;         // Kasuta kalibreeritud väärtust!

void setup() {
  Serial.begin(9600);
  Serial.println("WCS1700 - DC Mootori voolu test");
  Serial.println("Aeg(s),Vool(A)");
}

void loop() {
  int adc = analogRead(CURRENT_PIN);
  float voltage = adc * (VCC / 1023.0);
  float current = (voltage - V_REF) / SENSITIVITY;
  
  Serial.print(millis() / 1000.0, 1);
  Serial.print(",");
  Serial.println(current, 3);
  
  delay(100);
}
```

**Testimine nupuga (soovitatav!):**

Selleks, et näha kuidas vool muutub reaalajas, on kasulik lisada nupp mootori ja toiteallika vahele:

```
Toiteallikas + → [NUPP] → Kaabel (läbi WCS1700) → Mootor + → Mootor - → GND
```

**Kuidas testida:**
1. Laadi kood Arduino'sse
2. Ava Serial Plotter (Tools → Serial Plotter)
3. Vaata graafikut:
   - Nupp lahti → Vool = 0A
   - Vajuta nuppu → Vool hüppab üles (käivituspiik!)
   - Hoia nuppu all → Vool stabiliseerub (töövool)
   - Vabasta nupp → Vool langeb nulli

**Mida peaksid nägema Serial Plotter'is:**
- **Nupp lahti:** Sirge joon 0A juures
- **Nupu vajutamine:** Järsk tõus (piik 2-3A)
- **Mootor töötab:** Stabiilne joon 1-1.5A juures
- **Nupu vabastamine:** Järsk langus nulli

Sellega saad õpilane selgelt näha voolu muutusi!

**Mida jälgida:**
1. **Käivitusvoolupiik** - mootor võtab käivitumisel 2-3x rohkem voolu
2. **Töövool** - stabiilne vool pöörlemise ajal
3. **Kui blokeerid mootori** - vool tõuseb järsult (ohtlik!)

### Test 2: PWM juhitav mootor

**Eesmärk:** Vaata kuidas vool muutub mootori kiiruse muutudes

**Lisaühendus:**
- Arduino pin 9 → Transistori baas (nt TIP120 või MOSFET)
- Transistor juhtib mootorit

**Kood:**
```cpp
const int CURRENT_PIN = A0;
const int MOTOR_PIN = 9;  // PWM pin

const float VCC = 5.0;
const float SENSITIVITY = 0.036;
const float V_REF = 2.50;

void setup() {
  Serial.begin(9600);
  pinMode(MOTOR_PIN, OUTPUT);
  Serial.println("PWM(%),Vool(A)");
}

void loop() {
  // Testi erinevaid kiirusi
  for (int pwm = 0; pwm <= 255; pwm += 51) {  // 0%, 20%, 40%, ... 100%
    analogWrite(MOTOR_PIN, pwm);
    delay(2000);  // Oota stabiliseerumist
    
    // Mõõda vool (keskmine 10 mõõtmisest)
    float sum = 0;
    for (int i = 0; i < 10; i++) {
      int adc = analogRead(CURRENT_PIN);
      float voltage = adc * (VCC / 1023.0);
      sum += (voltage - V_REF) / SENSITIVITY;
      delay(10);
    }
    float avgCurrent = sum / 10.0;
    
    int percent = map(pwm, 0, 255, 0, 100);
    Serial.print(percent);
    Serial.print(",");
    Serial.println(avgCurrent, 3);
  }
  
  // Peata mootor
  analogWrite(MOTOR_PIN, 0);
  delay(5000);
}
```

**Oodatav tulemus:**
```
PWM(%)  →  Vool(A)
0       →  ~0.00A (mootor seisab)
20      →  ~0.30A (aeglane)
40      →  ~0.60A
60      →  ~0.90A
80      →  ~1.20A
100     →  ~1.50A (täiskiirus)
```

### Test 3: Ülekoormuse tuvastamine

**Eesmärk:** Kaitse mootori või süsteemi ülekoormuse eest

**Kood:**
```cpp
const int CURRENT_PIN = A0;
const int LED_PIN = 13;
const int MOTOR_PIN = 9;

const float VCC = 5.0;
const float SENSITIVITY = 0.036;
const float V_REF = 2.50;

// Ülekoormuse lävi (kohanda oma mootorile!)
const float NORMAL_CURRENT = 1.5;      // Normaalne töövool (A)
const float OVERLOAD_THRESHOLD = 2.5;  // Maksimaalne lubatud (A)

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  pinMode(MOTOR_PIN, OUTPUT);
  
  Serial.println("Vool(A),Staatus");
  
  // Käivita mootor
  analogWrite(MOTOR_PIN, 200);  // 78% kiirusest
}

void loop() {
  // Mõõda vool
  int adc = analogRead(CURRENT_PIN);
  float voltage = adc * (VCC / 1023.0);
  float current = (voltage - V_REF) / SENSITIVITY;
  
  // Kontrolli ülekoormust
  if (current > OVERLOAD_THRESHOLD) {
    digitalWrite(LED_PIN, HIGH);  // Hoiatus LED
    analogWrite(MOTOR_PIN, 0);    // PEATA MOOTOR!
    
    Serial.print(current, 2);
    Serial.println(",ÜLEKOORMATUD-PEATATUD!");
    
    delay(5000);  // Oota 5 sek enne taaskäivitamist
  } 
  else if (current > NORMAL_CURRENT * 1.2) {
    digitalWrite(LED_PIN, HIGH);  // Hoiatus
    Serial.print(current, 2);
    Serial.println(",HOIATUS-KÕRGE!");
  }
  else {
    digitalWrite(LED_PIN, LOW);
    Serial.print(current, 2);
    Serial.println(",OK");
  }
  
  delay(100);
}
```

### Võrdlus multimeetriga

**Setup:**
1. Ühenda multimeeter **jadas** (seeriaühendus) vooluahela
2. Võrdle Arduino näitu multimeetriga

**Näide:**
```
Multimeeter  |  Arduino (WCS1700)  |  Viga
0.00A        |  0.03A              |  ±0.03A (null-nihe, OK)
1.00A        |  0.98A              |  -2% (Väga hea!)
2.00A        |  1.96A              |  -2%
5.00A        |  4.90A              |  -2%
```

**Kui viga > 5%:**
- ✅ Kontrolli V_REF kalibreerimist
- ✅ Kontrolli SENSITIVITY väärtust
- ✅ Võimalik temperatuuri drift
- ✅ Kontrolli VCC = täpselt 5.0V?

---

## Kokkuvõte

✅ WCS1700 on **non-invasive** Hall-efekti vooluandur  
✅ **Kaabel läheb 9mm augu läbi** - vooluringi ei pea katkestama  
✅ **4 pind**: VCC, GND, Aout, Dout  
✅ Vahemik: **0-70A** (või ±35A sõltuvalt versioonist)  
✅ Tundlikkus: **36mV/A** (0.036V/A)  
✅ Valem: $I = \frac{V_{out} - 2.5V}{0.036V/A}$  
✅ **Galvaaniline isolatsioon 4000V** - ohutu!  
✅ Kalibreeri null-punkt täpsuse jaoks  
✅ Testi DC mootoriga enne tõsist kasutust  
✅ Jälgi ülekoormuse märke (kaitse!)  