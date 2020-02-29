# dependencies
import requests
import pandas as pd
def pubmed_call_api(pmids):
    #empty list for publication locations and dates
    location = []
    pub_date = []
    titles = []
    base_url = 'https://api.ncbi.nlm.nih.gov/lit/ctxp/v1/pubmed/?format=csl&id='
    for id in pmids:
        #query api and write locations and dates
        response = requests.get(f'{base_url}{id}').json()

        #append location
        try:
            location.append(response['publisher-place'])
        except:
            location.append('N/A')
        
        #append date
        try:
            date_unf = response['issued']['date-parts'][0]
            year = date_unf[0]
            month = date_unf[1]
            day = date_unf[2]
            pub_date.append(f'{year}-{month}-{day}')
        except:
            location.append('N/A')

        #append title
        try:
            titles.append(response['title'])
        except:
            titles.append('N/A')
    location_date_df = pd.DataFrame({'Title': titles, 'Location': location, 'Publication Date': pub_date})
    location_date_df.to_CSV('location_date')