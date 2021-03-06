# Generated by Django 3.0 on 2020-06-25 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('date_change', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиент',
            },
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('date_change', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('text', models.TextField(verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Вариант',
                'verbose_name_plural': 'Варианты',
            },
        ),
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('date_change', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date_start', models.DateField(verbose_name='Дата старта')),
                ('date_end', models.DateField(verbose_name='Дата окончания')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('date_change', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('text', models.TextField(verbose_name='Вопрос')),
                ('type_qustion', models.CharField(choices=[('text', 'Текст'), ('one', 'Один вариант'), ('few', 'Несколько вариантов')], max_length=255, verbose_name='Тип вопроса')),
                ('options', models.ManyToManyField(blank=True, null=True, to='api.Options', verbose_name='Варианты ответов')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Polls', verbose_name='Опрос')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='DialogControll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('date_change', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Clients', verbose_name='Клиент')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Questions', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Диалог контроллер',
                'verbose_name_plural': 'Диалог контроллер',
            },
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('date_change', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('text', models.TextField(max_length=2000, verbose_name='Ответ')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Clients', verbose_name='Клиент')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Questions', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
