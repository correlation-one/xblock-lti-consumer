# Generated by Django 3.2.14 on 2022-11-29 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lti_consumer', '0015_add_remaining_fields_to_lti_config'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lticonfiguration',
            name='lti_1p3_launch_url',
        ),
        migrations.RemoveField(
            model_name='lticonfiguration',
            name='lti_1p3_oidc_url',
        ),
        migrations.RemoveField(
            model_name='lticonfiguration',
            name='lti_1p3_tool_keyset_url',
        ),
        migrations.RemoveField(
            model_name='lticonfiguration',
            name='lti_1p3_tool_public_key',
        ),
    ]
