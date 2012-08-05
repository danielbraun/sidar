from django.db import models

class Discipline(models.Model):
	name = models.CharField(max_length=50)



class Designer(models.Model):
	name          = models.CharField(max_length=50)
	photo         = models.ImageField()
	birth_date    = models.DateField()
	death_date    = models.DateField()
	birth_country = models.ForeignKey("Country")
	philosophy    = models.TextField()
	is_active     = models.BooleanField()
	generation    = models.ForeignKey("Generation")

class Work(models.Model):
	title        = models.CharField(max_length=50)
	subjects     = models.ManyToManyField("Subject")
	discipline   = models.ForeignKey("Discipline")
	category     = models.ForeignKey("Category")
	publish_date = models.DateField()
	client       = models.ForeignKey("Client")
	techqniue    = models.ForeignKey("Technique")
	height       = models.DecimalField(max_digits=5, decimal_places=2)
	width        = models.DecimalField(max_digits=5, decimal_places=2)
	description  = models.TextField()
	country      = models.ForeignKey("Country")
	collection   = models.ForeignKey("Collection")







