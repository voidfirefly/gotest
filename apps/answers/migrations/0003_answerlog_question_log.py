# Generated by Django 2.0.3 on 2018-06-02 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0002_answerlog'),
        ('questions', '0002_questionlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerlog',
            name='question_log',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.QuestionLog'),
        ),
    ]