# Generated by Django 2.2.3 on 2019-08-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_auto_20190802_2228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studyrecord',
            options={'verbose_name': '学习记录', 'verbose_name_plural': '学习记录'},
        ),
        migrations.AddField(
            model_name='studyrecord',
            name='content',
            field=models.CharField(default='悄咪咪的学了些东西', max_length=1024, verbose_name='学到了什么'),
        ),
    ]
