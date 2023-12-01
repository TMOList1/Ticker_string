from django.db import migrations, models

class Migration(migrations.Migration):
	initial = True

	dependencies = [
	]

	operations = [
		migrations.CreateModel(
			name='VideoRequest',
			fields=[
				('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('text', models.TextField()),
				('created_at', models.DateTimeField(auto_now_add=True)),
			],
		),
	]
