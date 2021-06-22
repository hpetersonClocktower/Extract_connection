# Tableau & Affinity Connection Using Tableau's Extract API
The data_fetch.py file is a python solution that connects Affinity to Tableau using Tableau's Extract API. This solution reaches out to the Affinity API to generate a tde file that can be used as a data source when uploaded to Tableau.

## Set up
The other files required were not uploaded to git due to their size however they can be downloaded from Tableau ![here](https://www.tableau.com/products/api-download?utm_campaign_id=2017049&utm_campaign=Prospecting-ALL-ALL-ALL-ALL-ALL&utm_medium=Paid+Search&utm_source=Google+Search&utm_language=EN&utm_country=USCA&kw=&adgroup=CTX-Trial-Products-DSA&adused=DSA&matchtype=b&placement=&gclid=EAIaIQobChMIl5_g5Z-s8QIVIQ_nCh1LgA8FEAAYASAAEgLHYfD_BwE&gclsrc=aw.ds).

## Running the file
Download the Extract API using the link found in the Set up section. Place the data_fetch.py file in the top directory of the Extract API. In terminal in the top directory run python data_fetch.py
This should create the tde file with relevant Affinity data. Proceed to upload this dat to Tableau as an additional data source by openning a workbook, navigating to the Data Source tab on the far right, and adding the data source.
Note that the Affinity API Key is not in the data_fetch.py file. For the Affinity data to remain secure it is important that this API Key is never pushed to git. Prior to running the data_fetch.py file be sure to manually add the API key in. Note that the API key can be found in Affinity.

## Remaining Work
The API call needs to be modified to gather the desired data from Affinity. After this the data needs to be formatted properly and written to the affinityExtract.tde file. Finally the output file will need to be manually uploaded to Tableau each time the data needs refreshing.
