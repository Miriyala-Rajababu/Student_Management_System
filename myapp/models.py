from django.db import models


#We are implementing Mysql      

'''class Mahesh(models.Model):
    Name=models.CharField(max_length=50)
    Subject=models.CharField(max_length=20)
    def __str__(self):
        return f'{self.Name} {self.Subject}'  #it's create table name as myapp_Mahesh in mysql

    #class Meta:
        #db_table="saag"   # it's create table name as saag directly in mysql'''



from django.core.validators import EmailValidator

class Ticket(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.email}'