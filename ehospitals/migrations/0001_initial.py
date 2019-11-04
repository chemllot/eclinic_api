# Generated by Django 2.2.6 on 2019-11-04 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('action_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('name', models.CharField(default='ex: Infus', max_length=100)),
                ('rate', models.IntegerField(default=1)),
                ('is_publish', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('drug_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('name', models.CharField(default='ex: Paracetamol', max_length=100)),
                ('rate', models.IntegerField(default=1)),
                ('is_publish', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('enrollment_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('enrollment_date', models.DateField(auto_now_add=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('is_publish', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Patient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('kit_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('name', models.CharField(default='ex: Stetoskop', max_length=100)),
                ('rate', models.IntegerField(default=1)),
                ('is_publish', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('room_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('name', models.CharField(default='ex: Mawar', max_length=100)),
                ('capacity', models.IntegerField(default=1)),
                ('rate', models.IntegerField(default=1)),
                ('fill', models.IntegerField(default=0)),
                ('is_full', models.BooleanField(default=False)),
                ('is_publish', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('treatment_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('treatment_date', models.DateField(auto_now_add=True)),
                ('total', models.IntegerField(default=0)),
                ('is_publish', models.BooleanField(default=False)),
                ('enrollment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ehospitals.Enrollment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TreatmentKit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(default='ex: Your description')),
                ('price', models.IntegerField(default=0)),
                ('is_publish', models.BooleanField(default=True)),
                ('kit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ehospitals.Kit')),
                ('treatment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ehospitals.Treatment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TreatmentDrug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(default='ex: Your description')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=0)),
                ('is_publish', models.BooleanField(default=True)),
                ('kit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ehospitals.Kit')),
                ('treatment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ehospitals.Treatment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TreatmentDoctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(default='ex: Your description')),
                ('price', models.IntegerField(default=0)),
                ('is_publish', models.BooleanField(default=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Doctor')),
                ('treatment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ehospitals.Treatment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TreatmentAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(default='ex: Your description')),
                ('price', models.IntegerField(default=0)),
                ('is_publish', models.BooleanField(default=True)),
                ('action', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ehospitals.Action')),
                ('treatment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ehospitals.Treatment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentHospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('payment_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('amount', models.IntegerField(default=0)),
                ('pay', models.IntegerField(default=0)),
                ('change', models.IntegerField(default=0)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_publish', models.BooleanField(default=False)),
                ('enrollment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ehospitals.Enrollment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='enrollment',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ehospitals.Room'),
        ),
    ]
