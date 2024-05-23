from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    date_posted = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)

class ApplicationStatus(models.Model):
    class JobStatus(models.TextChoices):
        PERSONALLY_SHORTLISTED = "PERSONALLY_SHORTLISTED", _("Personally_Shortlisted")
        COMPANY_SHORTLISTED = "COMPANY_SHORTLISTED", _("Company_Shortlisted")
        APPLIED = "APPLIED", _("Applied")
        REJECTED = "REJECTED", _("Rejected")

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=30, choices=JobStatus,
        default=JobStatus.PERSONALLY_SHORTLISTED
    )
    update_date = models.DateField(auto_now=True)