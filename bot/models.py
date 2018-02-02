from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.CharField(max_length=250)
    bot = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Message(models.Model):
    body = models.TextField()
    date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Object(models.Model):
    name = models.CharField(max_length=50, null=False, default="thing")
    description = models.TextField(null=True)
    parent_id = models.IntegerField(null=True)
    color = models.CharField(max_length=50, null=True)
    material = models.CharField(max_length=50, null=True)
    size_x = models.IntegerField(null=True)
    size_y = models.IntegerField(null=True)
    size_z = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    volume = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    status = models.IntegerField(null=True)
    created_date = models.CharField(max_length=50, null=True)
    created_time = models.CharField(max_length=50, null=True)
    created_place = models.CharField(max_length=50, null=True)
    temp_status = models.CharField(max_length=100, null=True)
    temp_degree = models.IntegerField(null=True)
    temporary = models.NullBooleanField(null=True, default=False)

    def get(self):
        return {
            "name": self.name,
            "description": self.description,
            "parent": self.parent_id,
            "color": self.color,
            "material": self.material,
            "weight": self.weight,
        }


class S2P(models.Model):
    NP = models.CharField(max_length=100, null=True)
    VP = models.CharField(max_length=100, null=True)


class S3P(models.Model):
    NP = models.CharField(max_length=100, null=True)
    VP = models.CharField(max_length=100, null=True)
    ADJP = models.CharField(max_length=100, null=True)


class Sentence(models.Model):
    Count = models.IntegerField(null=True, default=0)
    Positive = models.NullBooleanField(default=True)
    Possibility = models.IntegerField(null=True, default=100)
    T1 = models.CharField(max_length=50, null=True)
    T2 = models.CharField(max_length=50, null=True)
    T3 = models.CharField(max_length=50, null=True)
    T4 = models.CharField(max_length=50, null=True)
    T5 = models.CharField(max_length=50, null=True)
    T6 = models.CharField(max_length=50, null=True)
    T7 = models.CharField(max_length=50, null=True)
    T8 = models.CharField(max_length=50, null=True)
    T9 = models.CharField(max_length=50, null=True)
    T10 = models.CharField(max_length=50, null=True)
    T11 = models.CharField(max_length=50, null=True)
    T12 = models.CharField(max_length=50, null=True)
    T13 = models.CharField(max_length=50, null=True)
    T14 = models.CharField(max_length=50, null=True)
    T15 = models.CharField(max_length=50, null=True)
    T16 = models.CharField(max_length=50, null=True)
    T17 = models.CharField(max_length=50, null=True)
    T18 = models.CharField(max_length=50, null=True)
    T19 = models.CharField(max_length=50, null=True)
    T20 = models.CharField(max_length=50, null=True)

    def get(self):
        final = ""
        if self.T1 is not None: final += str(self.T1) + " "
        if self.T2 is not None: final += str(self.T2) + " "
        if self.T3 is not None: final += str(self.T3) + " "
        if self.T4 is not None: final += str(self.T4) + " "
        if self.T5 is not None: final += str(self.T5) + " "
        if self.T6 is not None: final += str(self.T6) + " "
        return final
