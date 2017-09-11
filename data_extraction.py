import json
import pandas as pd
from bs4 import BeautifulSoup

def read_json(filename):
    counter = 0
    reports = []
    with open('data/ufodata.json') as f:
        for i in f:
            counter += 1
            if counter%1000 == 0:
                print counter
            soup = BeautifulSoup(json.loads(i)['html'])
            try:
                sighting_data = soup.findAll('tr')[1].contents[1].text
                sighting_desc = soup.findAll('tr')[2].contents[1].text
            except:
                pass
            sighting = [sighting_data, sighting_desc]
            reports.append(sighting)
    return reports

def extract_data(report):
    data = []
    split = report[0].split(': ')
    data.append(split[1][:15]) # datetime occured
    data.append(split[5][:-5][:-2]) #city
    data.append(split[5][:-5][-2:]) #state
    try:
        data.append(split[6].split('Duration')[0]) # shape
    except:
        data.append(None)
    try:
        data.append(split[6].split('Duration')[1][1:]) # duration
    except:
        data.append(None)
    data.append(report[1]) # description
    return data

if __name__=='__main__':
    sightings = read_json('data/ufodata.json')
    data = []
    for r in sightings:
        if len(r) < 2:
            pass
        else:
            extracted = extract_data(r)
            data.append(extracted)

    df = pd.DataFrame(data, columns=['occurred','city','state','shape','duration','desc'])
    pd.DataFrame.to_csv(df, 'data/ufodata_complete.csv', header=True, encoding='utf-8')
