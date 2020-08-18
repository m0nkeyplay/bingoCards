#!/usr/bin/env python3
import random
import datetime

#   Create an printable HTML file of as many bingo cards as you wish.

#   Customizable (kinda), but hey, it's free, you can customize it more and that's great!

#   Varibles to chose from
#########################################################
#   How many cards do you want?
cards = 100
#   What do you want for Free Space
#   Images are fine.  I've found 100x100 works best

freeSpace = '<img src="monkeyHead.jpg" width="100" height="100"/>'
#freeSpace = 'FREE<br />SPACE' #Or Choose Write in Some Text

pageStart = """<html><head>
<style>
table, th, td {
  border: 1px solid black;
}
table {
  width: 80%;
}
th {
  height: 50px;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 40px;
  background-color: #d3d3d3;
}
td {
    text-align: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 40px;
    height: 100px;
    width: 20%
}
.pagebreak { page-break-after: always; }
</style>
</head>
<body><center>
"""

pageEnd = "</body></html>"

def make_card():
    x = 1
    y = 1
    b = []
    i = []
    n = []
    g = []
    o = []
    bb = []
    ii = []
    nn = []
    gg = []
    oo =[]

    while x <= 15:
        b.append(x)
        x += 1
    while x <= 30:
        i.append(x)
        x += 1
    while x <= 45:
        n.append(x)
        x += 1
    while x <= 60:
        g.append(x)
        x += 1
    while x <= 75:
        o.append(x)
        x += 1
    while y <= 5:
        random.shuffle(b)
        random.shuffle(i)
        random.shuffle(n)
        random.shuffle(g)
        random.shuffle(o)
        bb.append(b.pop())
        ii.append(i.pop())
        nn.append(n.pop())
        gg.append(g.pop())
        oo.append(o.pop())
        y+=1

    card = """  <h1>&nbsp;</h1>
                <h1>&nbsp;</h1>
                <h1>&nbsp;</h1>
                <table>
                <tr>
                <th>B</th><th>I</th><th>N</th><th>G</th><th>O</th>
                </tr>
    """
    z = 0
    while z <= 4:
        if z == 2:
            card += """<tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        </tr>"""%(str(bb[z]),str(ii[z]),freeSpace,str(gg[z]),str(oo[z]))
        else:
            card += """<tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        </tr>"""%(str(bb[z]),str(ii[z]),str(nn[z]),str(gg[z]),str(oo[z]))
        z+=1

    card += """</table>
                <div class="pagebreak"></div>"""
    return(card)

if __name__ == '__main__':
    start = 1
    ourTime = datetime.datetime.now()
    fileName = 'bingoCards'+str(ourTime).split('.')[1]+'.html'
    printCard = open(fileName,'w')
    printCard.write(pageStart)
    while start <= cards:
        printCard.write(make_card())
        start += 1
    printCard.write(pageEnd)
    printCard.close()
    print("Created %s.  Print them out and enjoy your games!"%fileName)