# Generated by Django 3.2.12 on 2022-10-03 13:19

from django.db import migrations
from django.utils import timezone

CONFIG_SECRETS = {
    "external_auth_url": "url",
    "external_auth_domain": "domain",
    "external_auth_user": "user",
    "external_auth_key": "key",
    "external_auth_admin_group": "admin-group",
    "rbac_url": "rbac-url",
}


def move_secrets(apps, schema_editor):
    Config = apps.get_model("maasserver", "Config")
    Secret = apps.get_model("maasserver", "Secret")

    now = timezone.now()
    configs = Config.objects.filter(name__in=CONFIG_SECRETS)
    # ensure all keys are there
    secret_value = dict.fromkeys(CONFIG_SECRETS)
    secret_value = {
        CONFIG_SECRETS[name]: value
        for name, value in configs.values_list("name", "value")
    }
    if any(secret_value.values()):
        now = timezone.now()
        Secret.objects.create(
            path="global/external-auth",
            value=secret_value,
            created=now,
            updated=now,
        )

    configs.delete()


class Migration(migrations.Migration):
    dependencies = [
        ("maasserver", "0284_migrate_more_global_secrets"),
    ]

    operations = [migrations.RunPython(move_secrets)]
