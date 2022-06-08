# Generated by Django 4.0.5 on 2022-06-08 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('Server', 'Server'), ("Personal client's data", "Personal client's data"), ('Company contracts', 'Company contracts')], max_length=22)),
                ('owner', models.CharField(choices=[('System administrator', 'System administrator'), ('Director', 'Director')], editable=False, max_length=20)),
                ('category', models.CharField(choices=[('Edoc', 'Edoc'), ('Hardware', 'Hardware')], editable=False, max_length=8)),
                ('location', models.CharField(choices=[('Server', 'Server'), ('Cabinet', 'Cabinet')], editable=False, max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyRisk',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('danger_type', models.CharField(choices=[('Accessibility', 'Accessibility'), ('Confidentiality', 'Confidentiality'), ('Integrity', 'Integrity')], max_length=15)),
                ('danger', models.CharField(max_length=100)),
                ('danger_source', models.CharField(max_length=50)),
                ('implementation_mechanism', models.TextField(max_length=300)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.asset')),
            ],
        ),
    ]