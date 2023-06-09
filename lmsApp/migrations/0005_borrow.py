

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lmsApp', '0004_students_course_students_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowing_date', models.DateField()),
                ('return_date', models.DateField()),
                ('status', models.CharField(choices=[('1', 'Pending'), ('2', 'Returned')], default=1, max_length=2)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_id_fk', to='lmsApp.books')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_id_fk', to='lmsApp.students')),
            ],
            options={
                'verbose_name_plural': 'Borrowing Transactions',
            },
        ),
    ]
