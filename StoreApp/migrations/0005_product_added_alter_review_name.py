# Generated by Django 4.1.6 on 2023-02-10 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0004_remove_review_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='StoreApp.user'),
        ),
    ]
