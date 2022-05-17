# Generated by Django 4.0.4 on 2022-05-17 06:07

from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course_number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('decan_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kafedra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('tel_number', models.CharField(max_length=100)),
                ('kafedra_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diplom_ish.kafedra')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diplom_ish.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('tel_number', models.CharField(max_length=100)),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diplom_ish.faculty')),
                ('kurs_number_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diplom_ish.course_number')),
            ],
        ),
        migrations.CreateModel(
            name='Baho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baho', model_utils.fields.StatusField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='2', max_length=100, no_check_for_status=True)),
                ('fan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diplom_ish.subject')),
                ('talaba_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diplom_ish.student')),
            ],
        ),
    ]