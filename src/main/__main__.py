import sys
sys.path.append("../")


from fetch import FetchExchangeInfo

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QMessageBox,QCheckBox
import xml.etree.ElementTree as ET
from data.dataSwap import Swap
from fetch import FetchArbitrage

from threading import Thread

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.swaps = []

        try:
            tree = ET.parse('swaps.xml')
            root = tree.getroot()
            for swap_node in root.findall('swap'):
                name = swap_node.find('name').text
                network = swap_node.find('network').text
                router = swap_node.find('router').text
                factory = swap_node.find('factory').text
                self.swaps.append(Swap(name, network, router, factory))
        except (ET.ParseError, FileNotFoundError):
            pass



        self.table = QTableWidget()
        self.table.cellChanged.connect(self.update_swap)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Name', 'Network', 'Router', 'Factory'])
        self.table.setRowCount(len(self.swaps))
        for row, swap in enumerate(self.swaps):
            self.table.setItem(row, 0, QTableWidgetItem(swap.Name))
            self.table.setItem(row, 1, QTableWidgetItem(swap.Network))
            self.table.setItem(row, 2, QTableWidgetItem(swap.Router))
            self.table.setItem(row, 3, QTableWidgetItem(swap.Factory))

        add_button = QPushButton('Add Swap', self)
        add_button.clicked.connect(self.add_swap)
        save_button = QPushButton('Save Swaps', self)
        save_button.clicked.connect(self.save_swaps)
        fetch_button = QPushButton('Fetch Info', self)
        fetch_button.clicked.connect(self.fetch_info)

        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(add_button)
        layout.addWidget(save_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        remove_button = QPushButton('Remove Swap', self)
        remove_button.clicked.connect(self.remove_swap)
        layout.addWidget(remove_button)

        layout.addWidget(fetch_button)

        button_fetch_arbitrage = QPushButton('Fetch Arbitrage')
        button_fetch_arbitrage.clicked.connect(self.fetch_arbitrage)
        self.checkbox_filter = QCheckBox('Filter')
        layout.addWidget(self.checkbox_filter)
        layout.addWidget(button_fetch_arbitrage)

    def update_swap(self, row, column):
        swap = self.swaps[row]
        new_value = self.table.item(row, column).text()
        if column == 0:
            swap.Name = new_value
        elif column == 1:
            swap.Network = new_value
        elif column == 2:
            swap.Router = new_value
        elif column == 3:
            swap.Factory = new_value
    def add_swap(self):
        new_swap = Swap('New Swap', '', '', '')
        self.swaps.append(new_swap)
        row = self.table.rowCount()
        self.table.setRowCount(row+1)
        self.table.setItem(row, 0, QTableWidgetItem(new_swap.Name))
        self.table.setItem(row, 1, QTableWidgetItem(new_swap.Network))
        self.table.setItem(row, 2, QTableWidgetItem(new_swap.Router))
        self.table.setItem(row, 3, QTableWidgetItem(new_swap.Factory))



    def fetch_info(self):

        selection_model = self.table.selectionModel()
        selected_indexes = selection_model.selectedIndexes()
        swap=None
        if selected_indexes:
            row = selected_indexes[0].row()

            swap = self.swaps[row]


        t = Thread(target=FetchExchangeInfo.FetchExchangeInfo, args=(swap,))
        t.start()



    def fetch_arbitrage(self):
        selection_model = self.table.selectionModel()
        selected_indexes = selection_model.selectedIndexes()
        swap = None

        if selected_indexes:
            row = selected_indexes[0].row()

            swap = self.swaps[row]

        is_filter_enabled = self.checkbox_filter.isChecked()


        t = Thread(target=FetchArbitrage.FetchArbitrage, args=(swap, is_filter_enabled))
        t.start()



    def save_swaps(self):
        root = ET.Element('swaps')
        for swap in self.swaps:
            swap_node = ET.SubElement(root, 'swap')
            name_node = ET.SubElement(swap_node, 'name')
            name_node.text = swap.Name
            network_node = ET.SubElement(swap_node, 'network')
            network_node.text = swap.Network
            router_node = ET.SubElement(swap_node, 'router')
            router_node.text = swap.Router
            factory_node = ET.SubElement(swap_node, 'factory')
            factory_node.text = swap.Factory
        tree = ET.ElementTree(root)
        tree.write('swaps.xml')

    def remove_swap(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            return
        selected_swap = self.swaps[current_row]

        confirmation = QMessageBox.question(self, "Confirm removal", "Are you sure you want to remove this swap?",
                                            QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.swaps.remove(selected_swap)
            self.table.removeRow(current_row)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()




