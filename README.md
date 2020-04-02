# bs-bulletin-parser

Parses text of daily bulleting from Canton BS for covid19 data for the following data:
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
