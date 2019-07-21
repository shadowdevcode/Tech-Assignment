# Generated by Django 2.2.3 on 2019-07-21 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='ref_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='ref_code',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_on', models.DateTimeField(auto_now=True)),
                ('referee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referee', to='auth_accounts.Customer')),
                ('referrer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrer', to='auth_accounts.Customer')),
            ],
        ),
    ]
