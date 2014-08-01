import maya.cmds as cmds

uWidth = 250

def enablePrimaryVis(*args):
  print 'Render Vis enabled'
  
def disablePrimaryVis(*args):
  print 'Render Vis disabled'
  
def cleanupScene():
	print "Scene file cleaned up"

def launchTool():
	myWindow = cmds.window( title='Compass Tools', width=uWidth )
	cmds.columnLayout( adjustableColumn=True )
	cmds.button( label='Enable Primary Visibility', command=enablePrimaryVis )
	cmds.button( label='Disable Primary Visibility', command=disablePrimaryVis )
	cmds.button( label='Scene Cleanup', command=cleanupScene )
	cmds.showWindow()
	allowedAreas = ['right', 'left']
	#cmds.dockControl( area='left', content=myWindow, allowedArea=allowedAreas, label='testing', width=uWidth )
	
#launchTool()
	