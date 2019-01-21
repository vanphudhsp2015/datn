# Generated by Django 2.1.5 on 2019-01-21 15:21

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Null', max_length=250)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(default='Null')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='house',
            name='images',
            field=models.FileField(default='/default/default.png', upload_to='house/%Y/%m/%d/%H/%M/%S/'),
        ),
        migrations.AddField(
            model_name='housedetails',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='house.House'),
        ),
    ]
