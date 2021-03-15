from django.db import models

# Create a Blog model


class Blog(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')
	
	def __str__(self):
		return self.title

	def summary(self):
		if len(self.body) > 250:
			return self.body[:250].rsplit(' ',1)[0] + " [...]"
		else:
			return self.body

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')


	#title
#pub date
#body
#image

# Add a blog app to the settings

# Create a migration

# Migrate

# add to the admin

