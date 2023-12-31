# Generated by Django 4.2.2 on 2023-06-29 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recipt", "0004_remove_recipt_list_alter_recipt_device_id_product"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipt",
            name="date",
        ),
        migrations.AddField(
            model_name="recipt",
            name="month",
            field=models.IntegerField(null=True, verbose_name="결제월"),
        ),
        migrations.AddField(
            model_name="recipt",
            name="year",
            field=models.IntegerField(null=True, verbose_name="결제년"),
        ),
        migrations.AlterField(
            model_name="recipt",
            name="category",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="recipt.category",
                verbose_name="카테고리",
            ),
        ),
    ]
