# bs-bulletin-parser

Parses text of daily bulleting from Canton BS for covid19 data for the following data:

https://www.gd.bs.ch/medienseite/medienmitteilungen.html

```
NUMCUL_CONF_RESIDENTS
DAILY_DECEASED
DAILY_CONF
NUMCUL_RELEASED
NUMCUL_DECEASED
NUMCUL_CONF
NUMCUL_HOSP
NUMCUL_HOSP_RESIDENTS
NUMCUL_ICU
```

Copy daily bulletin text into an ascii file (or run example below) and run as follows:


```
python main.py --filename fixtures/test-1.txt
```
which then prints the results on the screen
```
>> WARNING:root:Error parsing: 61-jähriger

>> NUMCUL_CONF_RESIDENTS    : 691
>> NUMCUL_RELEASED          : 323
>> NUMCUL_HOSP_RESIDENTS    : 88
>> DAILY_DECEASED           : 2
>> NUMCUL_CONF              : 1095
>> NUMCUL_HOSP              : 108
>> NUMCUL_ICU               : 16

```

There is some basic text preprocessing where all german number words like "zwei", "hundert" etc. are replaced by their numerical values before actual parsing.
Some edge cases are also converted such as "ein", "eine", "einen" -> 1
This works for all numbers up to 100 plus a few common cases such as "tausend"


## Implementation Detail
Parsing is performed by using a custom trained named-entity-recognition model in spacy. `(nlp/*)`

Latest training data update: 2020-04-01

