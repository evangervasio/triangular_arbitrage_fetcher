import xml.etree.ElementTree as ET
class dataSet:
    def __init__(self, swapList, selectedSwap):
        self.swapList = swapList
        self.selectedSwap=selectedSwap

        tree = ET.parse('swaps.xml')
        root = tree.getroot()


