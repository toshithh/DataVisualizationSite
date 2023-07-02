# Generated by Django 4.2.1 on 2023-05-20 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assignment', '0005_delete_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.IntegerField(null=True)),
                ('intensity', models.IntegerField(null=True)),
                ('sector', models.CharField(max_length=30, null=True)),
                ('topic', models.CharField(max_length=30)),
                ('insight', models.CharField(max_length=300, null=True)),
                ('url', models.CharField(max_length=255, null=True)),
                ('region', models.CharField(max_length=30, null=True)),
                ('start_year', models.IntegerField(null=True)),
                ('impact', models.IntegerField(null=True)),
                ('added', models.DateTimeField()),
                ('published', models.DateTimeField(null=True)),
                ('country', models.CharField(max_length=30)),
                ('relevance', models.IntegerField(null=True)),
                ('pestle', models.CharField(max_length=20, null=True)),
                ('source', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=255)),
                ('likelihood', models.IntegerField(null=True)),
            ],
        ),
    ]