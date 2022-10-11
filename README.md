# School Search 

## Getting started
### Dependencies

* Python 3.8.9
* Pipenv (optional)

### Environment
Optionally, you can use [Pipenv](https://pypi.org/project/pipenv/) to manage your environment by running the following commands:
```
    pipenv install --python 3.8.9
    pipenv shell 
```
---
## Executing program

### Part 1: Load data from CSV and compute stats
Computes and outputs the following stats for the provided school data set: 
* Total schools
* Schools by state
* Schools by Metro-centric locale
* City with the most schools in it and its number of schools - _uses city and state to calculate the number of schools for each unique city and returns the unique city with the most schools_
* Unique cities with at least one school - _uses city and state to calculate the number of unique cities with at least one school_

Run:
```
python count_schools.py
```

#### Example response: 
```
Total Schools: 34779

Schools by State: 
   AL: 1606
   AK: 525
   AZ: 2147
   AR: 1174
   CA: 9969
   OR: 1
   NV: 1
   CO: 1730
   CT: 1120
   DE: 238
   DC: 229
   MD: 1
   C: 1
   FL: 4379
   GA: 2513
   HI: 285
   ID: 730
   IL: 4533
   IN: 2031
   OH: 1
   IA: 1565

Schools by Metro-centric locale: 
   3: 8180
   7: 4276
   4: 3829
   8: 4291
   1: 4862
   6: 2592
   2: 5383
   N: 1096
   5: 270

City with most schools: CHICAGO (657 schools)

Unique cities with at least one school: 5752
```
### Part 2: Search over school data
Searches over school name, city name, and state name from the provided data set by plain text query and returns the top 3 matches.

Run:
```
python school_search.py
```

#### Example response: 
```
Results for "elementary school highland park" (search took: 0.08498311042785645s)
1. HIGHLAND PARK HIGH SCHOOL 
   HIGHLAND PARK, IL
2. HIGHLAND PARK ELEMENTARY SCHOOL 
   MUSCLE SHOALS, AL
3. HUNTINGTON PARK NEW ELEMENTARY SCHOOL #7 
   HUNTINGTON PARK, CA
Results for "jefferson belleville" (search took: 0.07349300384521484s)
1. JEFFERSON HIGH SCHOOL 
   JEFFERSON, GA
2. JEFFERSON ELEMENTARY SCHOOL 
   JEFFERSON, GA
3. JEFFERSON MIDDLE SCHOOL 
   JEFFERSON, GA
Results for "riverside school 44" (search took: 0.0973660945892334s)
1. RIVERSIDE SCHOOL 44 
   INDIANAPOLIS, IN
2. RIVERSIDE SCHOOL 
   RIVERSIDE, CT
3. RIVERSIDE ELEMENTARY SCHOOL 
   RIVERSIDE, IA
Results for "granada charter school" (search took: 0.09452009201049805s)
1. GRANADA HILLS CHARTER HIGH 
   GRANADA HILLS, CA
2. GRANADA ELEMENTARY SCHOOL 
   GRANADA, CO
3. GRANADA UNDIVIDED HIGH SCHOOL 
   GRANADA, CO
Results for "foley high alabama" (search took: 0.08174705505371094s)
1. FOLEY HIGH SCHOOL 
   FOLEY, AL
2. FOLEY MIDDLE SCHOOL 
   FOLEY, AL
3. FOLEY ELEMENTARY SCHOOL 
   FOLEY, AL
Results for "KUSKOKWIM" (search took: 0.06340193748474121s)
1. TOP OF THE KUSKOKWIM SCHOOL 
   NIKOLAI, AK
```

---
## Additional Comments
I've love Python, so much so that I named one of my cats Py. It's been about 3 years since I last looked at Python, and I've never professionally worked in Python, but I always love coming back to it.

To improve upon the program, my next step would be to break out the functionality in `SchoolSearch.find_school_matches()` into smaller, more digestible functions.

With the logic more broken out, I would then like to focus on performance and implement more `intertools` functions. I was initially thrown off by the `itertools` documentation, so I decided to start by focusing on simply returning results with vanilla Python. I did use `itertools.chain.from_iterable` when I needed to flatmap over the values from the school data, but there are many other places where looping could be more efficient. 
