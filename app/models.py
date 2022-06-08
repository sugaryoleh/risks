from django.db.models import Model, AutoField, TextChoices, CharField, TextField, ForeignKey, RESTRICT
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Asset(Model):
    class AssetName(TextChoices):
        SERVER = 'Server', _('Server')
        PERSONAL_DATA = 'Personal client\'s data', _('Personal client\'s data')
        COMPANY_CONTRACTS = 'Company contracts', _('Company contracts')

    class AssetOwner(TextChoices):
        SYSADMIN = 'System administrator', _('System administrator')
        DIRECTOR = 'Director', _('Director')

    class AssetCategory(TextChoices):
        EDOC = 'Edoc', _('Edoc')
        HARDWARE = 'Hardware', _('Hardware')

    class Location(TextChoices):
        SERVER = 'Server', _('Server')
        CABINET = 'Cabinet', _('Cabinet')

    id = AutoField(primary_key=True)
    name = CharField(max_length=22, choices=AssetName.choices)
    owner = CharField(max_length=20, choices=AssetOwner.choices, editable=False)
    category = CharField(max_length=8, choices=AssetCategory.choices, editable=False)
    location = CharField(max_length=7, choices=Location.choices, editable=False)

    def save(self, *args, **kwargs):
        if self.name == self.AssetName.SERVER:
            self.owner = self.AssetOwner.SYSADMIN
            self.location = self.Location.CABINET
            self.category = self.AssetCategory.HARDWARE
        elif self.name == self.AssetName.PERSONAL_DATA:
            self.owner = self.AssetOwner.DIRECTOR
            self.location = self.Location.SERVER
            self.category = self.AssetCategory.EDOC
        elif self.name == self.AssetName.COMPANY_CONTRACTS:
            self.owner = self.AssetOwner.DIRECTOR
            self.location = self.Location.SERVER
            self.category = self.AssetCategory.EDOC
        else:
            raise ValueError('Asset name must be {}, {} or {}'.format(self.AssetName.SERVER,
                                                                      self.AssetName.PERSONAL_DATA,
                                                                      self.AssetName.COMPANY_CONTRACTS))
        super(Asset, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)


class CompanyRisk(Model):

    class DangerType(TextChoices):
        ACCESSIBILITY = 'Accessibility', _('Accessibility')
        CONFIDENTIALITY = 'Confidentiality', _('Confidentiality')
        INTEGRITY = 'Integrity', _('Integrity')

    id = AutoField(primary_key=True)
    asset = ForeignKey(Asset, on_delete=RESTRICT)
    danger_type = CharField(max_length=15, choices=DangerType.choices)
    danger = CharField(max_length=100)
    danger_source = CharField(max_length=50)
    implementation_mechanism = TextField(max_length=300)

    def get_absolute_url(self):
        return reverse('risk-update', kwargs={'pk': self.pk})
