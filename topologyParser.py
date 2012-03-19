from xml.etree.ElementTree import ElementTree

isDebug = True

class Topology:
	def __init__(self,path):
		self.tree = ElementTree()
		self.tree.parse(path)
		self.nodes = self.tree.findall('nodes/node')

	def	getHost(self):
		hostList = []
		for node in self.nodes:
			if node.get('type') == 'host':
				name = node.find('name').text
				hostList.append(name)

		return hostList

	def	getOpenflowSwitch(self):
		openflowSwitchList = []
		for node in self.nodes:
			if node.get('type') == 'openflowSwitch':
				name = node.find('name').text
				openflowSwitchList.append(name)

		return openflowSwitchList

	def getOpenflowSwitchInterface(self, switchName):
		interfaceList = []
		for node in self.nodes:
			if node.get('type') == 'openflowSwitch'	\
				and node.find('name').text == switchName:
				interfaces = node.findall('interfaces/interface')
				for interface in interfaces:
					name = interface.find('name').text
					interfaceList.append(name)

		return interfaceList
