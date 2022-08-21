"""
<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns"  
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">
  <graph id="G" edgedefault="undirected">
    <node id="n0"/>
    <node id="n1"/>
    <edge id="e1" source="n0" target="n1"/>
  </graph>
</graphml>
"""

import random

print('<?xml version="1.0" encoding="UTF-8"?>\
<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\
 xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\
 http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd"\
 xmlns:y="http://www.yworks.com/xml/graphml">\
<key for="node" id="d3" yfiles.type="nodegraphics"/>\
<graph id="G" edgedefault="directed">')

N = 5
for i in range(0,N):
	I = chr(ord('A') + i)
	for j in range(0,N):
		J = chr(ord('A') + j)
		
		print("<node id=\"n" +I+J +"\">")
		print("<data key=\"d3\">")
		print("<y:ShapeNode>")
		print("<y:Geometry height=\"10.0\" width=\"10.0\"/>")
		print("<y:Fill color=\"#FFCC00\" transparent=\"false\"/>")
		print("<y:NodeLabel>" + I+J +"</y:NodeLabel>")
		print("<y:Shape type=\"ellipse\"/>")
		print("</y:ShapeNode>")
		print("</data>")
		print("</node>")

D = 3
neighbors = list(range(-D,D))
neighbors.remove(0)

# random edges from node[i] to node[i]'s neighbors
# edge is only directed outwards, can be grey or red
for i in range(0,N):
	I = chr(ord('A') + i)
	for j in range(0,N):
		J = chr(ord('A') + j)
		for x in neighbors:
			X = chr(ord('A') + i+x)
			for y in neighbors:
				Y = chr(ord('A') + j+y)
				if i+x < 0 or i+x >= N:
					continue
				if j+y < 0 or j+y >= N:
					continue
				r = random.random()
				if r < 0.3:
					print("<edge id=\"e"+I+J+X+Y +\
						"\" source=\"n" +I+J +\
						"\" target=\"n" +X+Y + "\"/>")
				else:
					continue

print("</graph></graphml>")
