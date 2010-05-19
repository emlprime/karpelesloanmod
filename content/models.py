from django.db import models

from django.template.defaultfilters import slugify

class HomeText(models.Model):
    """ Model for the admin-editable home page text, both below and above the fold
    """
    date = models.DateField()
    header = models.CharField(max_length=255)
    above_fold = models.TextField()
    header_2 = models.CharField(max_length=255, null=True, blank=True)
    below_fold = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)


class AboutBankruptcyText(models.Model):
    """ Model for the about text on about bankruptcy page
    """
    text = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

class LoanModificationsText(models.Model):
    """ Model for the about text on Loan Modifications page
    """
    text = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

class AboutText(models.Model):
    """ Model for the about text on About page
    """
    text = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

class CreditorsRightsText(models.Model):
    """ Model for the about text on Creditor's Rights page
    """
    text = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

class ContactText(models.Model):
    """ Model for the about text on Contact page
    """
    text = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

class Chapter7Text(models.Model):
    """ Model for the about text on chapter 7 page
    """
    text = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

class Chapter11Text(models.Model):
    """ Model for the about text on chapter 11 page
    """
    text = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

class Chapter13Text(models.Model):
    """ Model for the about text on Chapter 13 page
    """
    text = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

class Attorney(models.Model):
    """ Model for the attorneys on the Attorney page
    """

    name = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    about = models.TextField()

    def __unicode__(self):
        return self.name

class DisclaimerText(models.Model):
    """ Model for the disclaimer text
    """
    
    disclaimer_text = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

