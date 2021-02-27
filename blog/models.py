from django.db import models

# Create a Blog model


class Blog(models.Model):
	title = models.CharField(max_length=255)
	pub_title = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')
	#title
#pub date
#body
#image

# Add a blog app to the settings

# Create a migration

# Migrate

# add to the admin

