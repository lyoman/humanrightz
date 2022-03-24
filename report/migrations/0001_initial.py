# Generated by Django 3.2.11 on 2022-03-24 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owners', models.CharField(max_length=250)),
                ('when_it_started_operating', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='ReportedCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reported', models.DateTimeField()),
                ('type_of_violation', models.CharField(choices=[('Forced Displacement', 'Forced Displacement'), ('Exposure to pollutants', 'Exposure to pollutants'), ('Loss of land or economic assets', 'Loss of land or economic assets'), ('Desecration of cultural heritage including graves', 'Desecration of cultural heritage including graves'), ('Torture and intimidation / harrassment', 'Torture and intimidation / harrassment'), ('Curtailed freedom of movement', 'Curtailed freedom of movement'), ('Exposure to degraded environment', 'Exposure to degraded environment'), ('Limited access to water', 'Limited access to water'), ('Denied access to social services like Health facilities, School, Markets place', 'Denied access to social services like Health facilities, School, Markets place'), ('Forced and unpaid labour', 'Forced and unpaid labour'), ('Child labour', 'Child labour'), ('Murder / killings', 'Murder / killings')], max_length=250)),
                ('description_of_victims', models.CharField(choices=[('Community member (individual/group)', 'Community member (individual/group)'), ('Women', 'Women'), ('Girls', 'Girls'), ('Youth', 'Youth'), ('Household', 'Household'), ('Mining company', 'Mining company'), ('Traditional leader', 'Traditional leader'), ('Farmer', 'Farmer'), ('Community activist', 'Community activist'), ('School children', 'School children')], max_length=250)),
                ('names_of_vitims', models.CharField(max_length=250)),
                ('victim_age', models.CharField(max_length=250)),
                ('victim_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Famale & Male', 'Male & Female')], max_length=250)),
                ('describe_gender', models.CharField(blank=True, max_length=250, null=True)),
                ('victim_phone_number', models.CharField(max_length=250)),
                ('victim_address', models.CharField(max_length=250)),
                ('description_of_perpetrator', models.CharField(choices=[('Member of Parliament', 'Member of Parliament'), ('Mining company security guards', 'Mining company security guards'), ('Artisanal miners ', 'Artisanal miners '), ('Politician', 'Politician'), ('Government security agencies (police, army)', 'Government security agencies (police, army)'), ('Councilors', 'Councilors')], max_length=250)),
                ('motivations_behind_incident', models.CharField(choices=[('Political', 'Political'), ('To conceal illicit activities and corruption', 'To conceal illicit activities and corruption'), ('To exercise Power', 'To exercise Power'), ('To instill fear', 'To instill fear'), ('Economic interest', 'Economic interest')], max_length=250)),
                ('what_happened', models.TextField(blank=True)),
                ('how_it_happened', models.TextField(blank=True)),
                ('evidence_files', models.ImageField(upload_to='transpired_description/')),
                ('community_description', models.TextField(blank=True)),
                ('location', models.CharField(max_length=250)),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=6)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=6)),
                ('identity_verification', models.FileField(upload_to='identity_verification/')),
                ('active', models.BooleanField(default=True)),
                ('read_status', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='report.companydetail')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]