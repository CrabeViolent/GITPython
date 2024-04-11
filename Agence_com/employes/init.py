from employe import Employe
from employeDAO import EmployeDao

employe = Employe("Micheal","Jackson","MBAP123","CS","IT")
message = EmployeDao.add(employe)
print(message)

#read_one = EmployeDao.read_one("MBAP123")
#print(read_one)