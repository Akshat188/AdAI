# Generated by Django 3.2.3 on 2021-06-05 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='designer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('contribution', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='themes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('business_type', models.CharField(choices=[('t1', 'type1'), ('t2', 'type2'), ('t3', 'type3')], default='t1', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneno', phonenumber_field.modelfields.PhoneNumberField(help_text='Contact phone number', max_length=128, region=None, unique=True)),
                ('isVerified', models.BooleanField(default=False)),
                ('counter', models.IntegerField(default=0)),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('business_name', models.CharField(max_length=30)),
                ('business_address', models.CharField(max_length=50)),
                ('business_type', models.CharField(choices=[('t1', 'type1'), ('t2', 'type2'), ('t3', 'type3')], default='t1', max_length=2)),
                ('business_phone', phonenumber_field.modelfields.PhoneNumberField(help_text='Contact phone number', max_length=128, region=None)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.users', to_field='phoneno')),
            ],
        ),
        migrations.CreateModel(
            name='user_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.users', to_field='phoneno')),
            ],
        ),
        migrations.CreateModel(
            name='sent_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_schedule', models.DateField()),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.userfields')),
                ('theme_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.themes')),
            ],
        ),
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images_theme')),
                ('designer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.designer')),
                ('theme_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.themes')),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(help_text='Contact phone number', max_length=128, region=None)),
                ('status', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.users', to_field='phoneno')),
            ],
        ),
    ]
