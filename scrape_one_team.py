from lxml import html
import requests

f1_in = open('team1', 'r')
f_out = open('results', 'w')
names1 = []
sr1 = []

for line in f1_in:
    names1.append(line)

for player in names1:
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
        sr1.append(int(pl_sr[0]))
    else:
        f_out.write(player+"; SR = NOT FOUND\n")
total = 0
for i in sr1:
    total += i
avg = total/len(sr1)
f_out.write("\nTeam Avg SR = "+str(avg)+"\n")

#Comments:
"""
http://docs.python-guide.org/en/latest/scenarios/scrape/
http://econpy.pythonanywhere.com/ex/001.html
https://www.w3schools.com/xml/xpath_syntax.asp
https://www.overbuff.com/players/pc/Frebreez3-1341
https://www.overbuff.com/players/pc/Sparkii621-1227
"""
