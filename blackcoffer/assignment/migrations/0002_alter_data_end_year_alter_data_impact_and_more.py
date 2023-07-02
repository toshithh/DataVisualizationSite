# Generated by Django 4.2.1 on 2023-05-20 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='end_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='impact',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='insight',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='intensity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='likelihood',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='pestle',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='published',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='region',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='relevance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='sector',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='source',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='start_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]