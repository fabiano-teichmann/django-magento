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


class AdminnotificationInbox(models.Model):
    notification_id = models.AutoField(primary_key=True)
    severity = models.PositiveSmallIntegerField()
    date_added = models.DateTimeField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    is_read = models.PositiveSmallIntegerField()
    is_remove = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'adminnotification_inbox'

class CoreStore(models.Model):
    store_id = models.PositiveSmallIntegerField(primary_key=True)
    code = models.CharField(unique=True, max_length=32, blank=True, null=True)
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)
    group = models.ForeignKey('CoreStoreGroup', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    sort_order = models.PositiveSmallIntegerField()
    is_active = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'core_store'

class CoreStoreGroup(models.Model):
    group_id = models.PositiveSmallIntegerField(primary_key=True)
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    root_category_id = models.PositiveIntegerField()
    default_store_id = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'core_store_group'


class CoreTranslate(models.Model):
    key_id = models.AutoField(primary_key=True)
    string = models.CharField(max_length=255)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    translate = models.CharField(max_length=255, blank=True, null=True)
    locale = models.CharField(max_length=20)
    crc_string = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'core_translate'
        unique_together = (('store', 'locale', 'crc_string', 'string'),)


class CatalogCategoryEntity(models.Model):
    """
        Table category master  content pk product
    """
    entity_id = models.AutoField(primary_key=True)
    entity_type_id = models.PositiveSmallIntegerField()
    attribute_set_id = models.PositiveSmallIntegerField()
    parent_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    path = models.CharField(max_length=255)
    position = models.IntegerField()
    level = models.IntegerField()
    children_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_category_entity'


class CatalogProductEntity(models.Model):
    """
        table master product
    """
    entity_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute_set = models.ForeignKey('EavAttributeSet', models.DO_NOTHING)
    type_id = models.CharField(max_length=32)
    sku = models.CharField(max_length=64, blank=True, null=True)
    has_options = models.SmallIntegerField()
    required_options = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity'


class CoreUrlRewrite(models.Model):
    url_rewrite_id = models.AutoField(primary_key=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    id_path = models.CharField(max_length=255, blank=True, null=True)
    request_path = models.CharField(max_length=255, blank=True, null=True)
    target_path = models.CharField(max_length=255, blank=True, null=True)
    is_system = models.PositiveSmallIntegerField(blank=True, null=True)
    options = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(CatalogCategoryEntity, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_url_rewrite'
        unique_together = (('request_path', 'store'), ('id_path', 'is_system', 'store'),)


class CoreVariable(models.Model):
    variable_id = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_variable'


class CoreVariableValue(models.Model):
    value_id = models.AutoField(primary_key=True)
    variable = models.ForeignKey(CoreVariable, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    plain_value = models.TextField(blank=True, null=True)
    html_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_variable_value'
        unique_together = (('variable', 'store'),)


class CoreWebsite(models.Model):
    website_id = models.PositiveSmallIntegerField(primary_key=True)
    code = models.CharField(unique=True, max_length=32, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    sort_order = models.PositiveSmallIntegerField()
    default_group_id = models.PositiveSmallIntegerField()
    is_default = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_website'

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

class CustomerEntity(models.Model):
    entity_id = models.AutoField(primary_key=True)
    entity_type_id = models.PositiveSmallIntegerField()
    attribute_set_id = models.PositiveSmallIntegerField()
    website = models.ForeignKey(CoreWebsite, models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    group_id = models.PositiveSmallIntegerField()
    increment_id = models.CharField(max_length=50, blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.PositiveSmallIntegerField()
    disable_auto_group_change = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'customer_entity'
        unique_together = (('email', 'website'),)



class SalesFlatOrder(models.Model):
    """
        Pedido
    """
    entity_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    coupon_code = models.CharField(max_length=255, blank=True, null=True)
    protect_code = models.CharField(max_length=255, blank=True, null=True)
    shipping_description = models.CharField(max_length=255, blank=True, null=True)
    is_virtual = models.PositiveSmallIntegerField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING, blank=True, null=True)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_global_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_invoiced_cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_offline_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_online_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_paid = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_qty_ordered = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_base_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_offline_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_online_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_paid = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_qty_ordered = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    can_ship_partially = models.PositiveSmallIntegerField(blank=True, null=True)
    can_ship_partially_item = models.PositiveSmallIntegerField(blank=True, null=True)
    customer_is_guest = models.PositiveSmallIntegerField(blank=True, null=True)
    customer_note_notify = models.PositiveSmallIntegerField(blank=True, null=True)
    billing_address_id = models.IntegerField(blank=True, null=True)
    customer_group_id = models.SmallIntegerField(blank=True, null=True)
    edit_increment = models.IntegerField(blank=True, null=True)
    email_sent = models.PositiveSmallIntegerField(blank=True, null=True)
    forced_shipment_with_invoice = models.PositiveSmallIntegerField(blank=True, null=True)
    payment_auth_expiration = models.IntegerField(blank=True, null=True)
    quote_address_id = models.IntegerField(blank=True, null=True)
    quote_id = models.IntegerField(blank=True, null=True)
    shipping_address_id = models.IntegerField(blank=True, null=True)
    adjustment_negative = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    adjustment_positive = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_adjustment_negative = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_adjustment_positive = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_due = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    payment_authorization_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_due = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    customer_dob = models.DateTimeField(blank=True, null=True)
    increment_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    applied_rule_ids = models.CharField(max_length=255, blank=True, null=True)
    base_currency_code = models.CharField(max_length=3, blank=True, null=True)
    customer_email = models.CharField(max_length=255, blank=True, null=True)
    customer_firstname = models.CharField(max_length=255, blank=True, null=True)
    customer_lastname = models.CharField(max_length=255, blank=True, null=True)
    customer_middlename = models.CharField(max_length=255, blank=True, null=True)
    customer_prefix = models.CharField(max_length=255, blank=True, null=True)
    customer_suffix = models.CharField(max_length=255, blank=True, null=True)
    customer_taxvat = models.CharField(max_length=255, blank=True, null=True)
    discount_description = models.CharField(max_length=255, blank=True, null=True)
    ext_customer_id = models.CharField(max_length=255, blank=True, null=True)
    ext_order_id = models.CharField(max_length=255, blank=True, null=True)
    global_currency_code = models.CharField(max_length=3, blank=True, null=True)
    hold_before_state = models.CharField(max_length=255, blank=True, null=True)
    hold_before_status = models.CharField(max_length=255, blank=True, null=True)
    order_currency_code = models.CharField(max_length=255, blank=True, null=True)
    original_increment_id = models.CharField(max_length=50, blank=True, null=True)
    relation_child_id = models.CharField(max_length=32, blank=True, null=True)
    relation_child_real_id = models.CharField(max_length=32, blank=True, null=True)
    relation_parent_id = models.CharField(max_length=32, blank=True, null=True)
    relation_parent_real_id = models.CharField(max_length=32, blank=True, null=True)
    remote_ip = models.CharField(max_length=255, blank=True, null=True)
    shipping_method = models.CharField(max_length=255, blank=True, null=True)
    store_currency_code = models.CharField(max_length=3, blank=True, null=True)
    store_name = models.CharField(max_length=255, blank=True, null=True)
    x_forwarded_for = models.CharField(max_length=255, blank=True, null=True)
    customer_note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    total_item_count = models.PositiveSmallIntegerField()
    customer_gender = models.IntegerField(blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_hidden_tax_amnt = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    coupon_rule_name = models.CharField(max_length=255, blank=True, null=True)
    paypal_ipn_customer_notified = models.IntegerField(blank=True, null=True)
    gift_message_id = models.IntegerField(blank=True, null=True)
    base_interest = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    interest = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_juros = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    juros = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    desconto = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_desconto = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_order'


class EavAttributeSet(models.Model):
    attribute_set_id = models.PositiveSmallIntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute_set_name = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'eav_attribute_set'
        unique_together = (('entity_type', 'attribute_set_name'),)


class EavEntity(models.Model):
    entity_id = models.AutoField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute_set_id = models.PositiveSmallIntegerField()
    increment_id = models.CharField(max_length=50, blank=True, null=True)
    parent_id = models.PositiveIntegerField()
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'eav_entity'

class EavEntityType(models.Model):
    entity_type_id = models.PositiveSmallIntegerField(primary_key=True)
    entity_type_code = models.CharField(max_length=50)
    entity_model = models.CharField(max_length=255)
    attribute_model = models.CharField(max_length=255, blank=True, null=True)
    entity_table = models.CharField(max_length=255, blank=True, null=True)
    value_table_prefix = models.CharField(max_length=255, blank=True, null=True)
    entity_id_field = models.CharField(max_length=255, blank=True, null=True)
    is_data_sharing = models.PositiveSmallIntegerField()
    data_sharing_key = models.CharField(max_length=100, blank=True, null=True)
    default_attribute_set_id = models.PositiveSmallIntegerField()
    increment_model = models.CharField(max_length=255, blank=True, null=True)
    increment_per_store = models.PositiveSmallIntegerField()
    increment_pad_length = models.PositiveSmallIntegerField()
    increment_pad_char = models.CharField(max_length=1)
    additional_attribute_table = models.CharField(max_length=255, blank=True, null=True)
    entity_attribute_collection = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eav_entity_type'
