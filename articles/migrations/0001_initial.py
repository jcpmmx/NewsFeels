# Generated by Django 2.1.4 on 2018-12-12 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(choices=[('CNN', 'cnn')], max_length=10)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('published', models.DateTimeField()),
                ('url', models.URLField(verbose_name='URL')),
                ('content', models.TextField()),
                ('sentiment_label', models.CharField(choices=[('POSITIVE', 'positive'), ('NEGATIVE', 'negative'), ('NEUTRAL', 'neutral')], max_length=10)),
                ('sentiment_score', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
