Hadoop and MapReduce by Haiqiong Yao
July 4, 2012

NameNode web UI: http://192.168.1.102:50070
JobTracker web UI: http://192.168.1.102:50030
TaskTracker web UI: http://192.168.1.102:500760

1. Streaming
commands in src/command.txt
(1) write a sampling script in python to get sample of cite75_99.txt.
CiteSample.py, input/cite75_99.txt, input/cite_sample.txt, 
The sample takes 10% data from the original one randomly.
(2) get the max of the 9th col of patent_sample.txt.
FeatureMax.py, input/patent_sample.txt, output/claim
(3) get the avg claim for each country from patent_sample.txt.
CountryClaim.py, CountryAvgClaim.py, input/patent_sample.txt, output/country_avg_claim
(4) count the number of patents granted each year with Aggregate.
GrantNumMapper.py, LongValueSum aggregate, input/patent_sample.txt, output/grant_per_year
(5) count the number of unique country per year
CountryPerYearMapper.py, UniqValueCount aggregate, input/patent_sample.txt, output/country_per_year
(6) use histogram aggregate


2. 
