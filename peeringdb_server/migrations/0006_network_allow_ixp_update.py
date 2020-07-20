# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-18 05:45


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0005_lat_lon_field_rename"),
    ]

    operations = [
        migrations.AddField(
            model_name="network",
            name="allow_ixp_update",
            field=models.BooleanField(
                default=False,
                help_text=b"Specifies whether an ixp is allowed to add a netixlan entry for this network via their ixp_member data",
            ),
        ),
    ]
