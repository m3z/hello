# -*- coding: utf-8 -*-

import command as cmd
import topologyParser

isDebug = True;

#ovsList = {}

def setSlices():
        cmd.createSlice('slice1','tcp:127.0.0.1:6644','usr1@visor.com')
        

def setupTopology():
	topology = topologyParser.Topology('topology.xml')
	hostList = topology.getHost()
	for host in hostList:
		cmd.lxcStart(host)

	openflowSwitchList = topology.getOpenflowSwitch()

	dpidlist = cmd.getDpidList()
	
	for openflowSwitch in openflowSwitchList:
		interfaceList = topology.getOpenflowSwitchInterface(openflowSwitch)
		
		for	 interface in interfaceList:
			cmd.ovsDpctl(openflowSwitch, interface)
        i=0
        for openflowSwitch in openflowSwitchList:
                interfaceList = topology.getOpenflowSwitchInterface(openflowSwitch)
		inportList = cmd.getPort(dpidlist[i])
		for	 interface in interfaceList:
                        cmd.addFlowSpace(dpidlist[i],'20','in_port='+ inportList[interface],'Slice:slice1=4')
                i=i+1     
                
if __name__ == '__main__':
        setSlices()
        setupTopology()
