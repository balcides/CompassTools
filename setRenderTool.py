import maya.cmds as cmds
import maya.mel as mel
from functools import partial

uWidth = 250
uAlign='right'

print "loading script..."

# BUTTON SCRIPTS ======================================

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

def getAttributes():
	#attribute = 'primaryVisibility'
	attributes = ['castsShadows','receiveShadows','motionBlur','primaryVisibility','visibleInReflections','visibleInRefractions','doubleSided']
	selection = cmds.ls(sl=True)
	for sel in selection:
		print sel
		relatives = cmds.listRelatives(sel, shapes=True)
		for rel in relatives:
			for attribute in attributes:
				try:
					this = cmds.getAttr(rel + '.' + attribute)
					print attribute + " = " + str(this)
					#cmds.checkBox(label='Primary Visibility', value=this)
				except:
					print "doesnt have " + attribute
	print ""

#Restores common attributes unneeded for rendering
def setAttributes(*args):   
	selection = cmds.ls(sl=True)
	for obj in selection:
	    #cmds.setAttr( obj+'.primaryVisibility', 1)
	    cmds.setAttr( obj+'.'+ args[0], args[1])
		
#Updates the checkboxes on selection
def updateAttr():
	#cmds.scriptJob( killAll=True, force=True)
	jobNum = cmds.scriptJob( event= ["SelectionChanged", getAttributes], protected=False)
	jobs = cmds.scriptJob( listJobs=True )
	#print jobs

def setCheckBox(Label, CommandAttribute):
	return cmds.checkBox( label=Label, align=uAlign, value=True, onCommand=partial (setAttributes, CommandAttribute, 1),  offCommand=partial (setAttributes, CommandAttribute, 0))

	
def printtest():
	print 'this is working'

cmds.scriptJob( killAll=True, force=True)
updateAttr()
	
#LAUNCH WINDOW ========================================
def launchTool():
	#if(cmds.window(myWindow, exists=True):
		#cmds.deleteUI(myWindow)
	myWindow = cmds.window( title='Compass Render Tools', width=uWidth )
	myLayout = cmds.columnLayout( adjustableColumn=True, columnAlign=uAlign)
	setCheckBox('Casts Shadow', 'castsShadows')
	setCheckBox('Recieves Shadows', 'receiveShadows')
	setCheckBox('Motion Blur', 'motionBlur')
	setCheckBox('Primary Visibility', 'primaryVisibility')
	setCheckBox('Visible In Reflections', 'visibleInReflections')
	setCheckBox('Visible In Refractions', 'visibleInRefractions')
	setCheckBox('Double Sided', 'doubleSided')
	cmds.separator( height=10, style='in' )
	cmds.button( label='Scene Cleanup', command=cleanupScene )
	cmds.button( label='Render Scene', command='cmds.RenderIntoNewWindow()')
	print myWindow
	#print cmds.window(myWindow, frontWindow=True)
	cmds.showWindow(myWindow)
	allowedAreas = ['right', 'left']
	#cmds.dockControl( area='left', content=myWindow, allowedArea=allowedAreas, label='testing', width=uWidth )
	


