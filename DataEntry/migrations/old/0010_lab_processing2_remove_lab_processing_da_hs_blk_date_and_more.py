# Generated by Django 4.2.1 on 2023-06-08 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DataEntry", "0009_exposure2_remove_exposure_atsugi_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="lab_processing2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("da_hs_blk_spiked", models.TextField(max_length=20)),
                ("da_hs_blk_int_std", models.TextField(max_length=20)),
                ("da_hs_blk_method", models.TextField(max_length=20)),
                ("da_hs_blk_date", models.TextField(max_length=20)),
                ("da_hs_blk_wbrush_spiked", models.TextField(max_length=20)),
                ("da_hs_blk_wbrush_int_std", models.TextField(max_length=20)),
                ("da_hs_blk_wbrush_method", models.TextField(max_length=20)),
                ("da_hs_blk_wbrush_date", models.TextField(max_length=20)),
                ("da_hs_l_spiked", models.TextField(max_length=20)),
                ("da_hs_l_int_std", models.TextField(max_length=20)),
                ("da_hs_l_method", models.TextField(max_length=20)),
                ("da_hs_l_date", models.TextField(max_length=20)),
                ("da_hs_r_spiked", models.TextField(max_length=20)),
                ("da_hs_r_int_std", models.TextField(max_length=20)),
                ("da_hs_r_method", models.TextField(max_length=20)),
                ("da_hs_r_date", models.TextField(max_length=20)),
                ("da_hs_r_wbrush_spiked", models.TextField(max_length=20)),
                ("da_hs_r_wbrush_int_std", models.TextField(max_length=20)),
                ("da_hs_r_wbrush_method", models.TextField(max_length=20)),
                ("da_hs_r_wbrush_date", models.TextField(max_length=20)),
                ("da_hs_l_wbrush_spiked", models.TextField(max_length=20)),
                ("da_hs_l_wbrush_int_std", models.TextField(max_length=20)),
                ("da_hs_l_wbrush_method", models.TextField(max_length=20)),
                ("da_hs_l_wbrush_date", models.TextField(max_length=20)),
            ],
        ),
        migrations.RemoveField(model_name="lab_processing", name="da_hs_blk_date",),
        migrations.RemoveField(model_name="lab_processing", name="da_hs_blk_int_std",),
        migrations.RemoveField(model_name="lab_processing", name="da_hs_blk_method",),
        migrations.RemoveField(model_name="lab_processing", name="da_hs_blk_spiked",),
        migrations.RemoveField(
            model_name="lab_processing", name="da_hs_blk_wbrush_date",
        ),
        migrations.RemoveField(
            model_name="lab_processing", name="da_hs_blk_wbrush_int_std",
        ),
        migrations.RemoveField(
            model_name="lab_processing", name="da_hs_blk_wbrush_method",
        ),
        migrations.RemoveField(
            model_name="lab_processing", name="da_hs_blk_wbrush_spiked",
        ),
        migrations.RemoveField(model_name="lab_processing", name="da_hs_l_date",),
        migrations.RemoveField(model_name="lab_processing", name="da_hs_l_int_std",),
        migrations.RemoveField(model_name="lab_processing", name="da_hs_l_method",),
        migrations.RemoveField(model_name="lab_processing", name="da_hs_l_spiked",),
        migrations.RemoveField(
            model_name="lab_processing", name="da_hs_l_wbrush_date",
        ),
        migrations.RemoveField(
            model_name="lab_processing", name="da_hs_l_wbrush_int_std",
        ),
        migrations.RemoveField(
            model_name="lab_processing", name="da_hs_l_wbrush_method",
        ),
        migrations.RemoveField(
            model_name="lab_processing", name="da_hs_l_wbrush_spiked",
        ),
        migrations.RemoveField(model_name="lab_processing", name="da_hs_r_date",),
        migrations.RemoveField(model_name="lab_processing", name="da_hs_r_int_std",),
        migrations.RemoveField(model_name="lab_processing", name="da_hs_r_method",),
        migrations.RemoveField(model_name="lab_processing", name="da_hs_r_spiked",),
        migrations.RemoveField(
            model_name="lab_processing", name="da_hs_r_wbrush_date",
        ),
        migrations.RemoveField(
            model_name="lab_processing", name="da_hs_r_wbrush_int_std",
        ),
        migrations.RemoveField(
            model_name="lab_processing", name="da_hs_r_wbrush_method",
        ),
        migrations.RemoveField(
            model_name="lab_processing", name="da_hs_r_wbrush_spiked",
        ),
    ]