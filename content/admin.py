from django.contrib import admin

from karpelesloanmod.content.models import HomeText, AboutBankruptcyText, LoanModificationsText, AboutText, CreditorsRightsText, ContactText, Chapter13Text, Chapter11Text, Chapter7Text, DisclaimerText

class LoanModificationsTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(LoanModificationsText, LoanModificationsTextAdmin)

