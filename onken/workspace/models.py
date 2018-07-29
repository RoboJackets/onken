from django.db import models
from onken.public.models import Workspace

class Vendor(models.Model):
    status_choices = (
        ('unapproved', 'Unapproved'),
        ('approved', 'Approved'),
        ('preferred', 'Preferred'),
        ('unavailable', 'Unavailable'),
    )

    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    nationality = models.CharField(max_length=128)
    billing_address = models.TextField()
    gt_vendor_id = models.IntegerField(null=True)
    status = models.CharField(max_length=24, choices=status_choices)
    sales_contact = models.TextField(null=True)
    customer_id = models.CharField(max_length=128, null=True)
    web_account = models.BooleanField(default=False)
    website = models.CharField(max_length=128, null=True)
    part_url_schema = models.CharField(max_length=128, null=True)
    shipping_quote_required = models.BooleanField(default=False)
    tax_exempt = models.BooleanField(default=False)
    requisition_guidance = models.TextField(null=True)