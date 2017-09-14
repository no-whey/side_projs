from lxml import html
import requests
import glob

teams = glob.glob("team*")

f_in = []
for i in range(1, len(teams)+1):
    f_in.append(open('team'+str(i), 'r'))
f_out = open('results', 'w')

for i in range(0, len(f_in)):
    f_out.write("--------------------------------\n")
    names = []
    sr = []
    for line in f_in[i]:
        names.append(line)

    for player in names:
        for let in player:
            if let is '#':
                player = player.replace(let, '-')
            if let is '\n':
                player = player.replace(let, '')
        page_url = 'https://www.overbuff.com/players/pc/'+player
        page = requests.get(page_url)
        tree = html.fromstring(page.content)
        pl_sr = tree.xpath('//span[@class="color-stat-rating"]/text()')

        if(len(pl_sr)!=0):
            f_out.write(player+"; SR = "+ pl_sr[0] +"\n")
            sr.append(int(pl_sr[0]))
        else:
            f_out.write(player+"; SR = NOT FOUND\n")
    total = 0
    for j in sr:
        total += j
    avg = total/len(sr)
    f_out.write("\nTeam "+str(i+1)+" Avg SR = "+str(avg)+"\n")
    f_out.write("--------------------------------\n")

#Comments:
"""
http://docs.python-guide.org/en/latest/scenarios/scrape/
http://econpy.pythonanywhere.com/ex/001.html
https://www.w3schools.com/xml/xpath_syntax.asp
https://www.overbuff.com/players/pc/Frebreez3-1341
https://www.overbuff.com/players/pc/Sparkii621-1227
"""
