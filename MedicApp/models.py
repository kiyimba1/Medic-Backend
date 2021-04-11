from django.db import models

# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    license_no = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    added_on = models.DateField(auto_now_add=True)



class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    medical_type = models.CharField(max_length=255)
    buy_price = models.CharField(max_length=255)
    sell_price = models.CharField(max_length=255)
    c_gst = models.CharField(max_length=255)
    s_gst = models.CharField(max_length=255)
    batch_no = models.CharField(max_length=255)
    shelf_no = models.CharField(max_length=255)
    expire_date = models.DateField()
    mfg_date = models.DateField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    in_stock_total = models.CharField(max_length=255)
    qty_in_strip = models.CharField(max_length=255)
    added_on = models.DateField(auto_now_add=True)

class MedicalDetails(models.Model):
    id = models.AutoField(primary_key=True)
    medicine_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    salt_name = models.CharField(max_length=255)
    salt_name = models.CharField(max_length=255)
    salt_qyt = models.CharField(max_length=255)
    salt_qyt_type = models.CharField(max_length=255)
    added_on = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255)

class Customer(models.Model):
    id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    added_on = models.DateField(auto_now_add=True)

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    added_on = models.DateField(auto_now_add=True)

class BillDetails(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    medical_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    qty = models.CharField(max_length=255)
    addec_on = models.DateField(auto_now_add=True)

class CustomerRequest(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    medical_details = models.ForeignKey(MedicalDetails, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    request_date = models.DateField(auto_now_add=True)

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    joining_date = models.DateField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    added_on = models.DateField(auto_now_add=True)

class EmployeeSalary(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_date = models.DateField()
    salary_amount = models.CharField(max_length=255)
    added_on = models.DateField(auto_now_add=True)

class EmployeeBank(models.Model):
    id = models.AutoField(primary_key=True)
    bank_account_no = models.CharField(max_length=255)
    ifsc = models.CharField(max_length=255)
    employee_id=models.ForeignKey(Employee, on_delete=models.CASCADE)

class CompanyAccount(models.Model):
    id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(max_length=255)
    transaction_amount = models.CharField(max_length=255)
    transaction_date = models.DateField()
    payment_method = models.CharField(max_length=255)

class CompanyBank(models.Model):
    id = models.AutoField(primary_key=True)
    bank_account_no = models.CharField(max_length=255)
    ifsc = models.CharField(max_length=255)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)