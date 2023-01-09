class employee:
    salary:3000
    increment=1.5

    @property
    def afterincrement(self):
        return self.salary*self.increment


    @afterincrement.setter
    def afterincrement(self):
        self.salary=self.afterincrement


obj=employee()
print(obj.afterincrement())



