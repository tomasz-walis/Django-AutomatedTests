# Generated by Django 2.0.2 on 2018-07-20 10:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_auto_20171229_1056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='13 Characters', max_length=13, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(help_text='Enter book description', max_length=1000),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this book', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Enter a book genre.', max_length=200),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(help_text='Enter Language', max_length=200),
        ),
    ]
