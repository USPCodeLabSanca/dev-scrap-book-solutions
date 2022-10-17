import json
import os

jsonToFolders = {
    'bands': 'bandas',
    'guitar_players': 'guitarristas',
    'bassists': 'baixistas',
    'singers': 'vocalistas',
    'keyboards': 'tecladistas',
    'drummers': 'bateristas'
}

itemToFolder = {
    'band': 'bandas',
    'guitar_player': 'guitarristas',
    'bassist': 'baixistas',
    'singer': 'vocalistas',
    'keyboard': 'tecladistas',
    'drummer': 'bateristas'
}

for el in jsonToFolders:
    os.system(f'rm -r ./{jsonToFolders[el]}/*')

startHTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="../styles/index.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="../bandas.html">Bandas</a></li>
                <li><a href="../vocalistas.html">Vocalistas</a></li>
                <li><a href="../guitarristas.html">Guitarristas</a></li>
                <li><a href="../bateristas.html">Bateristas</a></li>
                <li><a href="../baixistas.html">Baixistas</a></li>
                <li><a href="../tecladistas.html">Tecladistas</a></li>
            </ul>
        </nav>
        <div>
            <a href="../index.html">
                <img src="../assets/hand.png" alt="Rock logo">
                <span>Rock Encyclopedia</span>
            </a>
        </div>
    </header>
    <main>
        <h1>{title}</h1>
        <p>{paragraphs[0]}</p>
        <p>{paragraphs[1]}</p>
'''

bandInWhichMember = '''
<div>
    <h2>Bandas</h2>
    <a href='./bandas/{siteName}'>{bandName}</a>
</div>
'''
membersOfTheBand = '''
<div>
<h2>Membros</h2>
<ul>
{strOfMembers}
</ul>
</div>
'''

endHTML = '''
    </main>
    <footer>
        <ul>
            <li>Feito com carinho por <a href="https://github.com/kibonusp">Gabriel Freitas</a> ❤️</li>
            <li><a href="https://github.com/kibonusp"><i class="fa fa-2x fa-github"></i></a></li>
            <li><a href="https://www.linkedin.com/in/gabrielfreitas-xv/"><i class="fa fa-2x fa-linkedin-square" aria-hidden="true"></i></a></li>
        </ul>
    </footer>

</body>
</html>
'''


f = open('siteData.json')

data = json.load(f)

for key in jsonToFolders:
    for entity in data[key]:
        print(data[key][entity]['paragraphs'])
        if len(data[key][entity]['paragraphs']) == 1:
            data[key][entity]['paragraphs'].append('')
        page = startHTML.format(title=entity, paragraphs=data[key][entity]['paragraphs'])
        titleFormat = '_'.join(entity.split(' ')) + '.html'
        if (key != 'bands'):
            bandFormat= '../../bandas/' + '_'.join(data[key][entity]['band'].split(' ')) + '.html'
            print(bandFormat)
            page += bandInWhichMember.format(siteName=bandFormat, bandName=data[key][entity]['band'])
        else:
            strOfMembers = ""
            band = data[key][entity]
            for member in band:
                if member != 'paragraphs':
                    siteName = f'../{itemToFolder[member]}/' + '_'.join(band[member].split(' ')) + '.html'
                    strOfMembers += f'<li><a href={siteName}>{band[member]}</a></li>'
            page += membersOfTheBand.format(strOfMembers=strOfMembers)
        
        page += endHTML
        f = open(f'./{jsonToFolders[key]}/{titleFormat}', 'w', encoding="utf-8")
        f.write(page)

'''
for key in jsonToFolders:
    f = open(f'./{jsonToFolders[key]}.html', 'r', encoding='utf8')
    lines = f.readlines()
    for el in data[key]:
        page = '_'.join(el.split(' ')) + '.html'
        pageFormat = f'./{jsonToFolders[key]}/{page}'
        lines.insert(31, f'<li><a href={pageFormat}>{el}</a></li>')
    f = open(f'./{jsonToFolders[key]}.html', 'w', encoding='utf8')
    f.writelines(lines)
    f.close()
'''