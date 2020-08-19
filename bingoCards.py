#!/usr/bin/env python3


#   author:		https://github.com/m0nkeyplay
#   August 18, 2020 - original script written
#   Free to use
#   Free to modify and make better

import random
import datetime

#   Create an printable HTML file of as many bingo cards as you wish.

#   Customizable (kinda), but hey, it's free, you can customize it more and that's great!

#   Varibles to chose from
#########################################################
#   How many cards do you want?
cards = 50

#   Do you want a header for each card?
#   We take images or Text
#   Size matters - suggested sizes are here for you

cardHeader = ' &nbsp; '
#cardHeader = '<img src="image source" width="600" height="100"/>'

#   What do you want for Free Space
#   Images are fine.  I've found 100x100 works best

freeSpace = '<img src="monkeyHead.jpg" width="100" height="100"/>'
#freeSpace = 'FREE<br />SPACE' #Or Choose Write in Some Text

pageStart = """<html>
<head>
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
h1 {
    font-family: font-family: Arial, Helvetica, sans-serif;
    font-size: 60px;
}
.pagebreak { page-break-after: always; }
</style>
</head>
<body><center>
"""

pageEnd = "</body></html>"

def make_card():
    y = 1
    listB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    listI = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    listN = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
    listG = [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
    listO = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
    b = []
    i = []
    n = []
    g = []
    o = []

    while y <= 5:
        random.shuffle(listB)
        random.shuffle(listI)
        random.shuffle(listN)
        random.shuffle(listG)
        random.shuffle(listO)
        b.append(listB.pop())
        i.append(listI.pop())
        n.append(listN.pop())
        g.append(listG.pop())
        o.append(listO.pop())
        y+=1

    card = """  <h1>&nbsp;</h1>
                <h1>%s</h1>
                <table>
                <tr>
                <th>B</th><th>I</th><th>N</th><th>G</th><th>O</th>
                </tr>
    """%cardHeader

    z = 0
    while z <= 4:
        if z == 2:
            card += """<tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        </tr>"""%(str(b[z]),str(i[z]),freeSpace,str(g[z]),str(o[z]))
        else:
            card += """<tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        </tr>"""%(str(b[z]),str(i[z]),str(n[z]),str(g[z]),str(o[z]))
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