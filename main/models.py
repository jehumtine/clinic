from django.db import models

class ward(models.Model):
    ward_id = models.CharField(max_length=4, primary_key=True)
    ward_name = models.CharField(max_length=20, null=True)
    number_beds = models.IntegerField(null=True, default=5)
    nurse_in_charge = models.CharField(max_length=25, null=True)
    ward_type = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.ward_id


class patient(models.Model):
    patient_id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=20, null=True)
    initials = models.CharField(max_length=3, null=True)
    sex = models.CharField(max_length=1)
    address = models.CharField(max_length=30, null=True)
    post_card = models.CharField(max_length=6, null=True)
    admission = models.DateField(null=True)
    DOB = models.DateField()
    ward_id = models.ForeignKey(ward,on_delete=models.CASCADE,db_column='ward_id')
    next_of_kin = models.CharField(max_length=30, null=True)
    