import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel, QTreeView
import numpy as np

from hamming import Ui_MainWindow

class MainClassStart(Ui_MainWindow):
     
    def __init__(self, Form):
        print("\n --------Start Program--------")
        
        Ui_MainWindow.__init__(self)
        self.setupUi(Form)
      
        self.pushButton.clicked.connect(self.gen_ham)
        self.pushButton_2.clicked.connect(self.correct_ham)
        
        
        print("\n --------End Program--------") 
    def binToHexa(self,n):
        bnum = int(n)
        temp = 0
        mul = 1
        
        # counter to check group of 4
        count = 1
        
        # char array to store hexadecimal number
        hexaDeciNum = ['0'] * 100
        
        # counter for hexadecimal number array
        i = 0
        while bnum != 0:
            rem = bnum % 10
            temp = temp + (rem*mul)
            
            # check if group of 4 completed
            if count % 4 == 0:
                
                # check if temp < 10
                if temp < 10:
                    hexaDeciNum[i] = chr(temp+48)
                else:
                    hexaDeciNum[i] = chr(temp+55)
                mul = 1
                temp = 0
                count = 1
                i = i+1
                
            # group of 4 is not completed
            else:
                mul = mul*2
                count = count+1
            bnum = int(bnum/10)
            
        # check if at end the group of 4 is not
        # completed
        if count != 1:
            hexaDeciNum[i] = chr(temp+48)
            
        # check at end the group of 4 is completed
        if count == 1:
            i = i-1
            
        # printing hexadecimal number
        # array in reverse order
        print("\n Hexadecimal equivalent of {}: ".format(n), end="")
        while i >= 0:
            print(end=hexaDeciNum[i])
            i = i-1
        print('\n')
        #print(hexaDeciNum.decode())
        #byte_array=bytearray(hexaDeciNum)
        #byte_array = bytearray.fromhex(hexaDeciNum)
        #print(byte_array.decode())
        str1 = "" 
        # traverse in the string  
        for ele in hexaDeciNum: 
            str1 += ele  
        byte_array = bytearray.fromhex(str1)
        print("corresponding ascii value is:  ",byte_array.decode())
        ascii_val=byte_array.decode()
        #print(byte_array.decode())
        return hexaDeciNum.reverse(),ascii_val
        
    def gen_ham(self):
        print("\n --------gen_ham Started--------")
        d = self.textEdit.toPlainText()
        data=list(d)
        data.reverse()
        c,ch,j,r,h=0,0,0,0,[]

        while ((len(d)+r+1)>(pow(2,r))):
            r=r+1

        for i in range(0,(r+len(data))):
            p=(2**c)

            if(p==(i+1)):
                h.append(0)
                c=c+1

            else:
                h.append(int(data[j]))
                j=j+1

        for parity in range(0,(len(h))):
            ph=(2**ch)
            if(ph==(parity+1)):
                startIndex=ph-1
                i=startIndex
                toXor=[]

                while(i<len(h)):
                    block=h[i:i+ph]
                    toXor.extend(block)
                    i+=2*ph

                for z in range(1,len(toXor)):
                    h[startIndex]=h[startIndex]^toXor[z]
                ch+=1

        h.reverse()
        print('Hamming code generated would be:- ', end="")
        print(int(''.join(map(str, h))))
        h_generated=int(''.join(map(str, h)))
        hex_val,ascii_val=self.binToHexa(h_generated) 
        self.label.setText(str(h_generated))
        self.label_3.setText(str(hex_val))
        self.label_4.setText(str(ascii_val))
        
        '''path = self.openFile()
        print(path)
        csvFileName = path
        self.label_4.setText(path)'''
        
        print("\n ------- gen_ham Completed -------")
    
   
    def correct_ham(self):
        print("\n ------- correct_ham Started -------")
        thread1 = videoThread(self.videofileName, self.pushButton_4)
        thread1.start()
        self.pushButton_4.setText('Please Wait.... Notify When Completed')
        
    
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    mainObject = MainClassStart(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#
# End Of Program
