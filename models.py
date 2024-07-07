from djongo import models

# Create your models here.
class Routes(models.Model):
    number = models.CharField(max_length=50)
    Source = models.CharField(max_length=50, default='default value')
    Destination = models.CharField(max_length=50, default='default value')
    Src = models.TextField(default='[]')
    Dest = models.TextField(default='[]')
    Stops = models.TextField(default='{}')
    departure_time = models.TimeField(default=00)
    #departed = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default='notStarted')


    def __str__(self):
        return self.number

    def save(self, *args, **kwargs):
        # Ensure Src, Dest, and Stops fields are stored as JSON strings
        import json
        if isinstance(self.Src, dict):
            self.Src = json.dumps(self.Src)
        if isinstance(self.Dest, dict):
            self.Dest = json.dumps(self.Dest)
        if isinstance(self.Stops, dict):
            self.Stops = json.dumps(self.Stops)
        super().save(*args, **kwargs)

    def get_Src(self):
        import json
        return json.loads(self.Src)

    def get_Dest(self):
        import json
        return json.loads(self.Dest)

    def get_Stops(self):
        import json
        return json.loads(self.Stops)


