# -*- coding: utf-8 -*-

import command as cmd
import topologyParser


isDebug = True;


openflowSwitchList = ['switch0','switch1']


def cleanAll():
        cmd.cleanSlices()
        cmd.cleanFlowSpace()

def startOVS():
        
        openflowSwitchList = topology.getOpenflowSwitch()
	for openflowSwitch in openflowSwitchList:
		cmd.ovsOpenflowd(openflowSwitch, '127.0.0.1', 6633)
	


if __name__ == '__main__':
        cleanAll()
        startOVS()
