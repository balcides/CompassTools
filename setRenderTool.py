import maya.cmds as cmds
import maya.mel as mel
	
uWidth = 250

# BUTTONS ======================================

def enablePrimaryVis(*args):
	print 'Render Vis enabled'
	setAttributes('primaryVisibility', 1)
  
def disablePrimaryVis(*args):
	print 'Render Vis disabled'
	setAttributes('primaryVisibility', 0)
  
def cleanupScene(*args):
	print "Scene file cleaned up"
	cmds.delete(all=True, constructionHistory=True)
	mel.eval('cleanUpScene 1;')


#COMMANDS ===============================================

#Restores common attributes unneeded for rendering
def setAttributes(*args):   
	selection = cmds.ls(sl=True)
	for obj in selection:
	    #cmds.setAttr( obj+'.primaryVisibility', 1)
	    cmds.setAttr( obj+'.'+ args[0], args[1])
	    
#LAUNCH WINDOW ========================================
def launchTool():
	myWindow = cmds.window( title='Compass Tools', width=uWidth )
	cmds.columnLayout( adjustableColumn=True )
	cmds.button( label='Enable Primary Visibility', command=enablePrimaryVis )
	cmds.button( label='Disable Primary Visibility', command=disablePrimaryVis )
	cmds.button( label='Scene Cleanup', command=cleanupScene )
	cmds.showWindow()
	allowedAreas = ['right', 'left']
	#cmds.dockControl( area='left', content=myWindow, allowedArea=allowedAreas, label='testing', width=uWidth )
	
