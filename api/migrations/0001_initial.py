# Generated by Django 3.2.3 on 2021-05-22 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_1', phone_field.models.PhoneField(help_text='Número do telefone 1', max_length=31, verbose_name='Número do telefone 1')),
                ('phone_2', phone_field.models.PhoneField(blank=True, help_text='Número do telefone 2', max_length=31, verbose_name='Número do telefone 2')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
            ],
        ),
        migrations.CreateModel(
            name='DestinationAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=100, verbose_name='Nome da Rua')),
                ('street_number', models.IntegerField(verbose_name='Número da Rua')),
                ('postcode_number', models.CharField(max_length=10, verbose_name='Cep')),
                ('city', models.CharField(max_length=100, verbose_name='Cidade')),
                ('state_name', models.CharField(max_length=20, verbose_name='Nome do Estado')),
            ],
        ),
        migrations.CreateModel(
            name='PartsDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Demanda Finalizada')),
                ('image_status', models.FileField(upload_to='demands/completion/')),
                ('contact_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_information', to='api.contactinformation', verbose_name='Informações de contato')),
                ('destination_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_address', to='api.destinationaddress', verbose_name='Endereço de entrega')),
                ('part_description', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='part_description', to='api.partsdescription', verbose_name='Descrição da peça')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]
