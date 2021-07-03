class Address:
    def __init__(self,addnum,street):
	#add comments
        self.addnum=addnum
        self.addstreet=street
    def show(self):
        print('adrress num:',self.addnum,'street,',self.addstreet)
add1=Address(input('enter address num'),input('enter street'))
add1.show()



