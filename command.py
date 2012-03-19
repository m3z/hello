# -*- coding: utf-8 -*-

import os
import re
# below are defined by can.
import environmentParser

isDebug = True;

def noxCore(componentName):
	noxPath = environmentParser.getNoxPath()
	noxPort = environmentParser.getControllerPortByName(componentName)
	cmdString = 'cd '+ noxPath + ';' + \
			'./nox_core -v -i ptcp:' + noxPort + \
			' ' + componentName + ' -d'
	os.system(cmdString)
	if isDebug:
		print cmdString    


def runRfServer():
	routeflowPath = environmentParser.getRouteflowPath()
	cmdString = routeflowPath + ' &'
	os.system(cmdString)
	if isDebug:
		print cmdString

def lxcStart(name):
    cmdString = '''lxc-start -n ''' + name + ''' -d''';
    os.system(cmdString)
    print cmdString

def ovsOpenflowd(name, ip, port, hw_desc = None):
    if(hw_desc):
        cmdString = '''ovs-openflowd --hw-desc='''+ hw_desc + \
                    ' ' + name +'  tcp:' + ip + ':' + str(port) + \
                    ''' --out-of-band --detach'''
    else:
        cmdString = '''ovs-openflowd ''' + name + ' tcp:' + \
                    ip + ':' + str(port) + \
                    ''' --out-of-band --detach'''
    
    os.system(cmdString)
    print cmdString

def ifconfig(interface, action, ip = None, netmask = None):
    if(ip and netmask):
        cmdString = 'ifconfig ' + interface + ' ' + action + \
                    ' ' + ip + ' netmask ' + netmask
    else:
        cmdString = 'ifconfig ' + interface + ' ' + action

    os.system(cmdString)
    print cmdString


def ovsDpctl(entity, interface, action = 'add-if'):
    cmdString = 'ovs-dpctl ' + action + ' ' + entity + \
                ' ' + interface
    os.system(cmdString)
    print cmdString


# below are defined by zheng.

def delSlices(slicename):
        cmdString = 'fvctl --passwd-file=/root/.fvp deleteSlice ' + slicename
        os.system(cmdString)
        print cmdString

def cleanSlices():
        cmdString = "fvctl --passwd-file=/root/.fvp listSlices"
        sList = os.popen(cmdString).readlines()
        for sli in sList:
                sli = re.split(': ',sli)[1].rstrip()
                if(sli!='fvadmin' and sli!=None):
                        delSlices(sli)
                        #cmdString = "fvctl --passwd-file=/root/.fvp deleteSlice " + sli
                        #os.system(cmdString)
                        #print cmdString

def delFlowSpace(flowspaceID):
        cmdString = "fvctl --passwd-file=/root/.fvp removeFlowSpace "+ flowspaceID
        os.system(cmdString)
        print cmdString

def cleanFlowSpace():
        cmdString = "fvctl --passwd-file=/root/.fvp listFlowSpace"
        fList = os.popen(cmdString).readlines()
        for flowspace in fList:
                flowspace = re.search('(?<=id=\[)\d+',flowspace)
                if(flowspace):
                        delFlowSpace(flowspace.group())

def createSlice(slicename,controller,email):
        cmdString = "fvctl --passwd-file=/root/.fvp createSlice " + slicename + ' ' + controller + ' ' + email
        os.system(cmdString)
        print cmdString

def addFlowSpace(dpid,priority,flow_match,sliceActions):
        cmdString = 'fvctl --passwd-file=/root/.fvp addFlowSpace '+dpid+' '+priority+' '+flow_match+' '+sliceActions
        os.system(cmdString)
        print cmdString

def getDpidList():
        dpidList = []
        cmdString = "fvctl --passwd-file=/root/.fvp listDevices"
        dList = os.popen(cmdString).readlines()
        for dpid in dList:
                dpid = re.search('(?<=:\s).+',dpid).group()
                dpidList.append(dpid)
        return dpidList

def getPort(dpid):
        portList={}
        cmdString = "fvctl --passwd-file=/root/.fvp getDeviceInfo " + dpid
        pList = os.popen(cmdString).readlines()
        pList[4] = re.search('(?<=portNames=).+',pList[4]).group()
        portlist = re.split(',',pList[4])
        for port in portlist:
                port_name=re.search('.+(?=\()',port).group()
                port_no=re.search('(?<=\()\d+',port).group()
                portList[port_name]=port_no
        return portList
        
        
