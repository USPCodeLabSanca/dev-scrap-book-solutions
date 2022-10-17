import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

def getFirstTwoParagraphs(title):
    titleFormat = '_'.join(title.split(' '))
    try:
        html = urlopen(f'https://pt.wikipedia.org/wiki/{titleFormat}')
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print(e)
        return None
    bs = BeautifulSoup(html, 'html.parser')
    paragraphs =  [p.getText().rstrip() for p in bs.find('div', {'id': 'bodyContent'}).find_all('p', limit=4)]
    print(paragraphs)
    paragraphs = [p for p in paragraphs if len(p) > 50]
    print(paragraphs)
    return paragraphs[:2]

if __name__ == '__main__':
    f = open('info.json')

    data = json.load(f)
    f.close()
    
    bands = {band['band_name']: {'paragraphs': []} for band in data}
    for band in data:
        bands[band['band_name']]['drummer'] = band['drummer']
        bands[band['band_name']]['singer'] = band['singer']
        bands[band['band_name']]['guitar_player'] = band['guitar_player']
        if 'bassist' in band:
            bands[band['band_name']]['bassist'] = band['bassist']
        if 'keyboard' in band:
            bands[band['band_name']]['keyboard'] = band['keyboard']
            
    guitar_players = {band['guitar_player']: {'band': band['band_name'], 'paragraphs': []} for band in data}
    drummers = {band['drummer']: {'band': band['band_name'], 'paragraphs': []} for band in data}
    bassists = {band['bassist']: {'band': band['band_name'], 'paragraphs': []} for band in data if 'bassist' in band}
    singers = {band['singer']: {'band': band['band_name'], 'paragraphs': []} for band in data}
    keyboard = {band['keyboard']: {'band': band['band_name'], 'paragraphs': []} for band in data if 'keyboard' in band}
    
    newFileDict = {'bands': bands, 
                   'guitar_players': guitar_players, 
                   'drummers': drummers,
                   'bassists': bassists,
                   'singers': singers,
                   'keyboards': keyboard
    }
    keysData = ['band_name', 'guitar_player', 'bassist', 'singer', 'keyboard', 'drummer']
    keysNewDict = ['bands', 'guitar_players', 'bassists', 'singers', 'keyboards', 'drummers']
    
    for band in data:
        for i, key in enumerate(keysData):
            if key in band:
                if i == 0:
                    print(f'==== {band[key]} ====')
                else:
                    print(f'\t{band[key]}')
                paragraphs = getFirstTwoParagraphs(band[key])
                if paragraphs != None:
                    newFileDict[keysNewDict[i]][band[key]]['paragraphs'] = paragraphs

    print(newFileDict)
    
    with open('siteData.json', 'w') as f:
        json.dump(newFileDict, f, indent=2)
        print("'siteData.json' file was created")