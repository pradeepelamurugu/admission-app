from django.db import models


# staff_choice=(
#     (True , 'accept'),
#     (False , 'reject'),
# )

class Student(models.Model):
    name = models.CharField(max_length=30)
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    school_name = models.CharField(max_length=60)
    tenth_mark = models.IntegerField()
    twelth_mark = models.IntegerField()
    email = models.EmailField()
    phone_num = models.IntegerField()
    # status = models.BooleanField(choices=staff_choice)
    status = models.CharField(max_length=30)




    def __str__(self):
        return self.name

