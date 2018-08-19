Project to collect tweets related #SOS messages on #KeralaFloods and other input search keywords, real-time updates to a public Google Sheets doc. The live sheet is here - https://docs.google.com/spreadsheets/d/1F8qn0sgBZy36RMakWYh2draP56Uacv1ASHw8F8U36vw/edit#gid=0

Steps done so far:
1) Collected all major cities, towns and other places in Kera from Wikipedia and Web.
2) Gathering Twitter stream data using Producer-Consumer framework using queue
3) Language Identification and Translation using Google Translate API
4) Soundex based algorithm to find similar sounding placenames in Kerala
5) Real-time updating in the Live Google Sheets with filtered tweets containing place names only (collected in Step 1) 

Future Works:
1) Better de-duplication with better caching implementation
2) Better classification algorithm to identify real SOS tweets
3) To intimate the nearest help/relief center with the sos tweet obtained using Google location API


