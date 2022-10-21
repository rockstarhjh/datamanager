# Generated by Django 4.1 on 2022-10-07 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('product', models.CharField(blank=True, max_length=50, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=10, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('sumprice', models.IntegerField(blank=True, null=True)),
                ('tax', models.IntegerField(blank=True, null=True)),
                ('totalprice', models.IntegerField(blank=True, null=True)),
                ('inoutcompany', models.CharField(blank=True, max_length=50, null=True)),
                ('incomeprice', models.IntegerField(blank=True, null=True)),
                ('division', models.CharField(blank=True, max_length=10, null=True)),
                ('paymethod', models.CharField(blank=True, max_length=45, null=True)),
                ('remark', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'acount',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('comnum', models.CharField(blank=True, max_length=30, null=True)),
                ('ceo', models.CharField(blank=True, max_length=30, null=True)),
                ('tel', models.CharField(blank=True, max_length=50, null=True)),
                ('fax', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('item', models.CharField(blank=True, max_length=30, null=True)),
                ('delivery', models.CharField(blank=True, max_length=200, null=True)),
                ('cellphone', models.CharField(blank=True, max_length=30, null=True)),
                ('post', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('division', models.CharField(blank=True, max_length=10, null=True)),
                ('remark', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'company',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('idproducts', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, db_collation='utf8mb4_unicode_ci', max_length=45, null=True)),
                ('p_name', models.CharField(blank=True, db_collation='utf8mb4_unicode_ci', max_length=45, null=True)),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('idstocks', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('category', models.CharField(max_length=45)),
                ('p_name', models.CharField(max_length=45)),
                ('company', models.CharField(max_length=45)),
                ('in_field', models.IntegerField(blank=True, null=True)),
                ('out_field', models.IntegerField(blank=True, null=True)),
                ('return_field', models.IntegerField(blank=True, null=True)),
                ('lost_field', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(max_length=45)),
                ('remark', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'stocks',
                'managed': False,
            },
        ),
    ]
