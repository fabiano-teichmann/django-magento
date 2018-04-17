# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminAssert(models.Model):
    assert_id = models.AutoField(primary_key=True)
    assert_type = models.CharField(max_length=20, blank=True, null=True)
    assert_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_assert'


class AdminRole(models.Model):
    """
        Admin  role table master
    """
    role_id = models.AutoField(primary_key=True)
    parent_id = models.PositiveIntegerField()
    tree_level = models.PositiveSmallIntegerField()
    sort_order = models.PositiveSmallIntegerField()
    role_type = models.CharField(max_length=1)
    user_id = models.PositiveIntegerField()
    role_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_role'


class AdminRule(models.Model):
    rule_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(AdminRole, models.DO_NOTHING)
    resource_id = models.CharField(max_length=255, blank=True, null=True)
    privileges = models.CharField(max_length=20, blank=True, null=True)
    assert_id = models.PositiveIntegerField()
    role_type = models.CharField(max_length=1, blank=True, null=True)
    permission = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_rule'


class AdminUser(models.Model):
    """
        Table users
    """
    user_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=32, blank=True, null=True)
    lastname = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    username = models.CharField(unique=True, max_length=40, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    logdate = models.DateTimeField(blank=True, null=True)
    lognum = models.PositiveSmallIntegerField()
    reload_acl_flag = models.SmallIntegerField()
    is_active = models.SmallIntegerField()
    extra = models.TextField(blank=True, null=True)
    rp_token = models.TextField(blank=True, null=True)
    rp_token_created_at = models.DateTimeField(blank=True, null=True)
    customer_group_id = models.CharField(max_length=1024)
    description = models.TextField(blank=True, null=True)
    emails = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_user'

    class AmastyAmorderattrOrderAttribute(models.Model):
        """
        Verify doctor is authorized access report
        """
        entity_id = models.AutoField(primary_key=True)
        order = models.ForeignKey('SalesFlatOrder', models.DO_NOTHING, unique=True)
        doctor_authorization = models.PositiveIntegerField()
        doctor_not_listed = models.CharField(max_length=255)

        class Meta:
            managed = False
            db_table = 'amasty_amorderattr_order_attribute'