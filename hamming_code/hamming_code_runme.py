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
        str1 = "" 
        while i >= 0:
            print(end=hexaDeciNum[i])
            #print(type(hexaDeciNum[i]))
            str1+=hexaDeciNum[i]
            i = i-1
        print('\n')
        #print(hexaDeciNum.decode())
        #byte_array=bytearray(hexaDeciNum)
        #byte_array = bytearray.fromhex(hexaDeciNum)
        #print(byte_array.decode())

        # traverse in the string  
        #for ele in hexaDeciNum: 
        #	str1 += ele
        #	str1 = ele+str1
        #print(str1)
        #str1.decode("hex")
        #byte_array = bytearray.fromhex(str1)
        #print("corresponding ascii value is:  ",byte_array.decode())
        #print(byte_array.decode())
        
        #print("\n Corresponding ASCII value is : ",hexToASCII(str1))
        #return hexaDeciNum.reverse()
        return str1
    # Python3 program to convert hexadecimal
    # string to ASCII format string
    def hexToASCII(self,hexx):
     
        # initialize the ASCII code string as empty.
        ascii = ""
     
        for i in range(0, len(hexx), 2):
     
            # extract two characters from hex string
            part = hexx[i : i + 2]
     
            # change it into base 16 and
            # typecast as the character
            ch = chr(int(part, 16))
     
            # add this char to final ASCII string
            ascii += ch
         
        return ascii    
        
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
        hex_val=self.binToHexa(h_generated) 
        ascii_val=self.hexToASCII(hex_val) 
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
        '''thread1 = videoThread(self.videofileName, self.pushButton_4)
        thread1.start()
        self.pushButton_4.setText('Please Wait.... Notify When Completed')'''
        print('Enter the hamming code received')
        #d=input()
        d = self.textEdit_2.toPlainText()
        data=list(d)
        data.reverse()
        c,ch,j,r,error,h,parity_list,h_copy=0,0,0,0,0,[],[],[]

        for k in range(0,len(data)):
            p=(2**c)
            h.append(int(data[k]))
            h_copy.append(data[k])
            if(p==(k+1)):
                c=c+1
                
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
                parity_list.append(h[parity])
                ch+=1
        parity_list.reverse()
        error=sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))
        #label numbers- 14,16,11,9,19
        if((error)==0):
            print('\nThere is no error in the hamming code received')
            self.label_19.setText('There is no error in the hamming code received')
            self.label_16.setText(d)
            hex_val=self.binToHexa(d)
            ascii_val=self.hexToASCII(hex_val)
            self.label_11.setText(hex_val)
            self.label_9.setText(ascii_val)
            self.label_14.setText("")
        elif((error)>=len(h_copy)):
            print('\nError cannot be detected')
            self.label_19.setText('Error cannot be detected')
            
            self.label_16.setText("")
            self.label_11.setText("")
            self.label_9.setText("")
            self.label_14.setText("")
        else:
            print('\nError is in',error,'bit')
            self.label_14.setText(str(error))

            if(h_copy[error-1]=='0'):
                h_copy[error-1]='1'

            elif(h_copy[error-1]=='1'):
                h_copy[error-1]='0'
                print('\nAfter correction hamming code is:- ')
            h_copy.reverse()
            print(int(''.join(map(str, h_copy))))
            #binToHexa(int(''.join(map(str, h_copy))))       
            ans=int(''.join(map(str, h_copy)))
            ans=str(ans)
            hex_val=self.binToHexa(ans)
            ascii_val=self.hexToASCII(hex_val)
            
            self.label_16.setText(ans)
            self.label_11.setText(hex_val)
            self.label_9.setText(ascii_val)
            
            self.label_19.setText("")
    
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
