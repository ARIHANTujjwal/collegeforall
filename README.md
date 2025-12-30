# Project Title

CollegeForAll

## Description

A repo which contains list of all colleges in USA with few data points.

## My Data Source
[US Department of Education College Scorecard] (https://collegescorecard.ed.gov/)

## Getting Started

### Clone it locally
```
git clone https://github.com/yourusername/collegeforall.git
cd collegeforall
```

### Run it locally
```
uv run  derived_data.py --dir_path data/ --min_math 700 --max_math 800 --state=TX
```

## Few considerations:
- I used pagination while fetching data.
- Fetched data is huge, almost total data of 4.5GB.
- I prcoessed the fetched data to get what I needed.
- I futher split the fetched data across multiple files to limit data in each file.
- I ran logics in eventual fetched data to get different type of information.
- For SAT score of every college I used 75th percentile instead of mid-point.

## Example:
```
ariujjwal:collegedata ariujjwal$ uv run  derived_data.py --help
usage: derived_data.py [-h] --dir_path DIR_PATH [--min_math MIN_MATH] [--max_math MAX_MATH] [--min_eng MIN_ENG] [--max_eng MAX_ENG] [--state STATE]

Filter/Sort USA Colleges by SAT Scores.

options:
  -h, --help            show this help message and exit
  --dir_path DIR_PATH   Path to data json files
  --min_math MIN_MATH   Minimum SAT Math Score
  --max_math MAX_MATH   Maximum SAT Math Score
  --min_eng MIN_ENG     Minimum SAT English Score
  --max_eng MAX_ENG     Maximum SAT English Score
  --state STATE         Two-letter state (e.g., CA)
ariujjwal:collegedata ariujjwal$


ariujjwal:collegedata ariujjwal$ uv run  derived_data.py --dir_path data/ --min_math 700 --max_math 800
Loaded 6091 total colleges from fdata/

School Name                                             | Math  | English | State Code | State
------------------------------------------------------------------------------------------------------------
Columbia University in the City of New York             | 800   | 790     |  NY        | New York
Harvard University                                      | 800   | 790     |  MA        | Massachusetts
Princeton University                                    | 800   | 790     |  NJ        | New Jersey
Yale University                                         | 800   | 790     |  CT        | Connecticut
Brown University                                        | 800   | 780     |  RI        | Rhode Island
Duke University                                         | 800   | 780     |  NC        | North Carolina
Johns Hopkins University                                | 800   | 780     |  MD        | Maryland
Massachusetts Institute of Technology                   | 800   | 780     |  MA        | Massachusetts
Stanford University                                     | 800   | 780     |  CA        | California
University of Chicago                                   | 800   | 780     |  IL        | Illinois
University of Pennsylvania                              | 800   | 780     |  PA        | Pennsylvania
Carnegie Mellon University                              | 800   | 770     |  PA        | Pennsylvania
New York University                                     | 800   | 770     |  NY        | New York
Rice University                                         | 800   | 770     |  TX        | Texas
Washington University in St Louis                       | 800   | 770     |  MO        | Missouri
Dartmouth College                                       | 790   | 780     |  NH        | New Hampshire
Williams College                                        | 790   | 780     |  MA        | Massachusetts
Claremont McKenna College                               | 790   | 770     |  CA        | California
Cornell University                                      | 790   | 770     |  NY        | New York
Franklin W Olin College of Engineering                  | 790   | 770     |  MA        | Massachusetts
Harvey Mudd College                                     | 790   | 770     |  CA        | California
Northwestern University                                 | 790   | 770     |  IL        | Illinois
Pomona College                                          | 790   | 770     |  CA        | California
Swarthmore College                                      | 790   | 770     |  PA        | Pennsylvania
Vanderbilt University                                   | 790   | 770     |  TN        | Tennessee
Bowdoin College                                         | 790   | 760     |  ME        | Maine
Carleton College                                        | 790   | 760     |  MN        | Minnesota
Colby College                                           | 790   | 760     |  ME        | Maine
Emory University                                        | 790   | 760     |  GA        | Georgia
Emory University-Oxford College                         | 790   | 760     |  GA        | Georgia
Grinnell College                                        | 790   | 760     |  IA        | Iowa
Northeastern University                                 | 790   | 760     |  MA        | Massachusetts
Tufts University                                        | 790   | 760     |  MA        | Massachusetts
University of Southern California                       | 790   | 760     |  CA        | California
Case Western Reserve University                         | 790   | 750     |  OH        | Ohio
University of Missouri-Kansas City                      | 790   | 750     |  MO        | Missouri
University of Rochester                                 | 790   | 750     |  NY        | New York
Georgia Institute of Technology-Main Campus             | 790   | 740     |  GA        | Georgia
Jewish Theological Seminary of America                  | 780   | 779     |  NY        | New York
Amherst College                                         | 780   | 770     |  MA        | Massachusetts
Barnard College                                         | 780   | 770     |  NY        | New York
Georgetown University                                   | 780   | 770     |  DC        | District of Columbia
Hamilton College                                        | 780   | 770     |  NY        | New York
Haverford College                                       | 780   | 770     |  PA        | Pennsylvania
Middlebury College                                      | 780   | 770     |  VT        | Vermont
Vassar College                                          | 780   | 770     |  NY        | New York
Wellesley College                                       | 780   | 770     |  MA        | Massachusetts
Boston College                                          | 780   | 760     |  MA        | Massachusetts
Rhode Island School of Design                           | 780   | 760     |  RI        | Rhode Island
University of Notre Dame                                | 780   | 760     |  IN        | Indiana
Brandeis University                                     | 780   | 750     |  MA        | Massachusetts
Colgate University                                      | 780   | 750     |  NY        | New York
University of Michigan-Ann Arbor                        | 780   | 750     |  MI        | Michigan
University of North Carolina at Chapel Hill             | 780   | 750     |  NC        | North Carolina
University of Richmond                                  | 780   | 750     |  VA        | Virginia
University of Virginia-Main Campus                      | 780   | 750     |  VA        | Virginia
Washington and Lee University                           | 780   | 750     |  VA        | Virginia
Webb Institute                                          | 780   | 745     |  NY        | New York
Boston University                                       | 780   | 740     |  MA        | Massachusetts
Northeastern University Oakland                         | 780   | 740     |  CA        | California
The Cooper Union for the Advancement of Science and Art | 780   | 740     |  NY        | New York
University of Maryland-College Park                     | 780   | 740     |  MD        | Maryland
University of Illinois Urbana-Champaign                 | 780   | 730     |  IL        | Illinois
University of Wisconsin-Madison                         | 780   | 730     |  WI        | Wisconsin
Babson College                                          | 780   | 720     |  MA        | Massachusetts
Fisk University                                         | 780   | 700     |  TN        | Tennessee
Smith College                                           | 770   | 770     |  MA        | Massachusetts
Wesleyan University                                     | 770   | 770     |  CT        | Connecticut
Scripps College                                         | 770   | 760     |  CA        | California
Bates College                                           | 770   | 740     |  ME        | Maine
Villanova University                                    | 770   | 740     |  PA        | Pennsylvania
Wake Forest University                                  | 770   | 740     |  NC        | North Carolina
Rensselaer Polytechnic Institute                        | 770   | 730     |  NY        | New York
Santa Clara University                                  | 770   | 730     |  CA        | California
Stevens Institute of Technology                         | 770   | 730     |  NJ        | New Jersey
Stony Brook University                                  | 770   | 720     |  NY        | New York
University of Washington-Bothell Campus                 | 770   | 700     |  WA        | Washington
Soka University of America                              | 770   | 690     |  CA        | California
Colorado College                                        | 760   | 760     |  CO        | Colorado
Davidson College                                        | 760   | 750     |  NC        | North Carolina
Macalester College                                      | 760   | 750     |  MN        | Minnesota
Tulane University of Louisiana                          | 760   | 750     |  LA        | Louisiana
William & Mary                                          | 760   | 750     |  VA        | Virginia
Yeshiva University                                      | 760   | 740     |  NY        | New York
Binghamton University                                   | 760   | 730     |  NY        | New York
Fordham University                                      | 760   | 730     |  NY        | New York
Lafayette College                                       | 760   | 730     |  PA        | Pennsylvania
Lehigh University                                       | 760   | 730     |  PA        | Pennsylvania
Rhodes College                                          | 760   | 730     |  TN        | Tennessee
The University of Texas at Austin                       | 760   | 730     |  TX        | Texas
Ohio State University-Main Campus                       | 760   | 720     |  OH        | Ohio
Rutgers University-New Brunswick                        | 760   | 720     |  NJ        | New Jersey
Union College                                           | 760   | 720     |  NY        | New York
University of Massachusetts-Amherst                     | 760   | 720     |  MA        | Massachusetts
University of Minnesota-Twin Cities                     | 760   | 720     |  MN        | Minnesota
CUNY Hunter College                                     | 760   | 710     |  NY        | New York
Denison University                                      | 760   | 710     |  OH        | Ohio
New Jersey Institute of Technology                      | 760   | 710     |  NJ        | New Jersey
Rose-Hulman Institute of Technology                     | 760   | 710     |  IN        | Indiana
Hillsdale College                                       | 750   | 760     |  MI        | Michigan
Oberlin College                                         | 750   | 760     |  OH        | Ohio
Reed College                                            | 750   | 760     |  OR        | Oregon
George Washington University                            | 750   | 750     |  DC        | District of Columbia
Kenyon College                                          | 750   | 750     |  OH        | Ohio
Mount Holyoke College                                   | 750   | 750     |  MA        | Massachusetts
Occidental College                                      | 750   | 750     |  CA        | California
University of Tulsa                                     | 750   | 740     |  OK        | Oklahoma
Southern Methodist University                           | 750   | 730     |  TX        | Texas
University of Florida                                   | 750   | 730     |  FL        | Florida
Colorado School of Mines                                | 750   | 720     |  CO        | Colorado
University of Miami                                     | 750   | 720     |  FL        | Florida
CUNY City College                                       | 750   | 710     |  NY        | New York
Purdue University-Main Campus                           | 750   | 710     |  IN        | Indiana
DePauw University                                       | 750   | 680     |  IN        | Indiana
Whitman College                                         | 740   | 740     |  WA        | Washington
Gettysburg College                                      | 740   | 720     |  PA        | Pennsylvania
North Carolina State University at Raleigh              | 740   | 720     |  NC        | North Carolina
Rochester Institute of Technology                       | 740   | 720     |  NY        | New York
Bucknell University                                     | 740   | 710     |  PA        | Pennsylvania
Pepperdine University                                   | 740   | 710     |  CA        | California
United States Air Force Academy                         | 740   | 710     |  CO        | Colorado
University of Alabama in Huntsville                     | 740   | 700     |  AL        | Alabama
Centre College                                          | 740   | 683     |  KY        | Kentucky
Bryn Mawr College                                       | 730   | 740     |  PA        | Pennsylvania
Connecticut College                                     | 730   | 740     |  CT        | Connecticut
St Olaf College                                         | 730   | 740     |  MN        | Minnesota
Trinity University                                      | 730   | 735     |  TX        | Texas
Franklin and Marshall College                           | 730   | 730     |  PA        | Pennsylvania
Skidmore College                                        | 730   | 730     |  NY        | New York
Trinity College                                         | 730   | 730     |  CT        | Connecticut
Brigham Young University                                | 730   | 720     |  UT        | Utah
University of Pittsburgh-Pittsburgh Campus              | 730   | 720     |  PA        | Pennsylvania
Drexel University                                       | 730   | 700     |  PA        | Pennsylvania
United States Military Academy                          | 730   | 700     |  NY        | New York
University of the Pacific                               | 730   | 690     |  CA        | California
CUNY Bernard M Baruch College                           | 730   | 680     |  NY        | New York
University of Louisiana at Monroe                       | 730   | 620     |  LA        | Louisiana
School of Visual Arts                                   | 725   | 725     |  NY        | New York
Moore College of Art and Design                         | 723   | 688     |  PA        | Pennsylvania
The College of Wooster                                  | 720   | 730     |  OH        | Ohio
Wheaton College                                         | 720   | 720     |  IL        | Illinois
Chapman University                                      | 720   | 710     |  CA        | California
Saint Louis University                                  | 720   | 710     |  MO        | Missouri
Syracuse University                                     | 720   | 710     |  NY        | New York
Pratt Institute-Main                                    | 720   | 700     |  NY        | New York
United States Naval Academy                             | 720   | 700     |  MD        | Maryland
University of Arizona                                   | 720   | 700     |  AZ        | Arizona
University of Colorado Boulder                          | 720   | 700     |  CO        | Colorado
University of Connecticut                               | 720   | 700     |  CT        | Connecticut
Virginia Polytechnic Institute and State University     | 720   | 700     |  VA        | Virginia
Bentley University                                      | 720   | 690     |  MA        | Massachusetts
Illinois Institute of Technology                        | 720   | 690     |  IL        | Illinois
Mississippi State University                            | 720   | 690     |  MS        | Mississippi
The University of Texas at Dallas                       | 720   | 690     |  TX        | Texas
Bridgewater College                                     | 715   | 660     |  VA        | Virginia
American University                                     | 710   | 740     |  DC        | District of Columbia
Sarah Lawrence College                                  | 710   | 730     |  NY        | New York
Touro University                                        | 710   | 730     |  NY        | New York
Lawrence University                                     | 710   | 720     |  WI        | Wisconsin
CUNY Brooklyn College                                   | 710   | 710     |  NY        | New York
University of Maryland-Baltimore County                 | 710   | 700     |  MD        | Maryland
Indiana University-Bloomington                          | 710   | 690     |  IN        | Indiana
Pennsylvania State University-Main Campus               | 710   | 690     |  PA        | Pennsylvania
New York Institute of Technology                        | 710   | 680     |  NY        | New York
Viterbo University                                      | 710   | 670     |  WI        | Wisconsin
Missouri University of Science and Technology           | 708   | 670     |  MO        | Missouri
Furman University                                       | 705   | 720     |  SC        | South Carolina
Knox College                                            | 705   | 680     |  IL        | Illinois
St. John's College                                      | 700   | 750     |  NM        | New Mexico
Bard College                                            | 700   | 740     |  NY        | New York
Willamette University                                   | 700   | 730     |  OR        | Oregon
College of the Holy Cross                               | 700   | 720     |  MA        | Massachusetts
University of Vermont                                   | 700   | 720     |  VT        | Vermont
Wheaton College (Massachusetts)                         | 700   | 720     |  MA        | Massachusetts
Gonzaga University                                      | 700   | 710     |  WA        | Washington
Point Loma Nazarene University                          | 700   | 710     |  CA        | California
St Lawrence University                                  | 700   | 710     |  NY        | New York
University of Denver                                    | 700   | 710     |  CO        | Colorado
Baylor University                                       | 700   | 700     |  TX        | Texas
Creighton University                                    | 700   | 700     |  NE        | Nebraska
Providence College                                      | 700   | 700     |  RI        | Rhode Island
Seton Hall University                                   | 700   | 700     |  NJ        | New Jersey
The University of Alabama                               | 700   | 700     |  AL        | Alabama
University of Alabama at Birmingham                     | 700   | 700     |  AL        | Alabama
University of Utah                                      | 700   | 698     |  UT        | Utah
Clarkson University                                     | 700   | 690     |  NY        | New York
Clemson University                                      | 700   | 690     |  SC        | South Carolina
Drake University                                        | 700   | 690     |  IA        | Iowa
University of Georgia                                   | 700   | 690     |  GA        | Georgia
University of San Francisco                             | 700   | 690     |  CA        | California
Albany College of Pharmacy and Health Sciences          | 700   | 680     |  NY        | New York
Texas A&M University-College Station                    | 700   | 680     |  TX        | Texas
University at Buffalo                                   | 700   | 680     |  NY        | New York
MCPHS University                                        | 700   | 640     |  MA        | Massachusetts
ariujjwal:collegedata ariujjwal$ 
```
