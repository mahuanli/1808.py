class Home():

	def __init__(self,area,type,address):

		self.area = area

		self.type = type

		self.address = address

		self.jiaju = []

	def __str__(self):

		msg = "面积是%d,户型是%s,地址是%s,家具有%s"%(self.area,self.type,self.address,str(self.jiaju[0].name))

		return msg


	def add(self,jj):

		self.jiaju.append(jj)

	def tell_area(self):
		all_a = 0


class Bed():

	def __init__(self,area,name):

		self.area = area

		self.name = name


home = Home(300,"城堡","陕西")

bed = Bed(8,"公主床")

home.add(bed)

print(home)
