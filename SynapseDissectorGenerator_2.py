from ini.trakem2.display import Display
from ini.trakem2 import Project
from ini.trakem2.tree import ProjectThing
from ini.trakem2.tree import DNDTree
from ini.trakem2.display import Ball
from javax.swing.tree import DefaultMutableTreeNode

# get project, layer and project tree
p = Project.getProjects()[0]
layer = Display.getFrontLayer()
pTree = p.getProjectTree()
#rootNode = pTree.getRootNode()      # get root node of project tree, only for fully automate dissector generator
# get project, layer and project tree

#get current selection's parent tree
currentTreepath = pTree.getSelectionPath()
currentParentPath = currentTreepath.getParentPath()
dmtn = currentParentPath.getLastPathComponent()
#get current selection's parent tree

#create string array of coordinates for ball names
row = 19		#!!! This is where user can change the dissector's X dimension
column = 19		#!!! This is where user can change the dissector's Y dimension
step = 2		#!!! This is where user can change the dissecotr's fraction
rows = ['Row_'+str(x).zfill(2) for x in xrange(1,row+1)]
coordinates = ['('+str(x).zfill(2)+',' +str(y).zfill(2)+')' for x in xrange(1,row+1) for y in xrange(1,column+1)]
#create string array of coordinates for ball names


#add new balls under selection's parent, with names created before
for rowName in rows[1:len(rows)-1]:

	#create row list with X coordinates
	rowIndex = rows.index(rowName)
	project_pt1 = dmtn.getUserObject()   #project_node.getUserObject()	#get project thing
	ct1 = project_pt1.createChild("anything")
	ct1.setTitle(rowName)
	new_node1 = DefaultMutableTreeNode(ct1) 
	dmtn.add(new_node1)
	DNDTree.expandNode(pTree, DNDTree.findNode(ct1, pTree))
	newPath = new_node1.getPath()[-1]
	#create row list with X coordinates

	#analyze row and column information, to exclude the margin dissectors
	caseColumnIndex = (column+1)%2
	caseRowIndex = (rowIndex+1)%2
	caseIndex = abs(caseRowIndex - caseColumnIndex)
	#analyze row and column information, to exclude the margin dissectors

	#create ball object within each row, and name them with coordinates
	for BallName in coordinates[column*rowIndex+1+caseRowIndex:column*rowIndex+column-caseIndex:step]:
		project_pt2 = newPath.getUserObject()   #project_node.getUserObject()	#get project thing
		ct2 = project_pt2.createChild("ball")
		ct2.setTitle(BallName)
		new_node2 = DefaultMutableTreeNode(ct2) 
		newPath.add(new_node2)
		DNDTree.expandNode(pTree, DNDTree.findNode(ct2, pTree))
	#create ball object within each row, and name them with coordinates

#update the project tree to display the changes made
Display.repaint()
pTree.updateUILater()		