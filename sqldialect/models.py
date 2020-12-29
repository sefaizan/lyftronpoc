from django.db import models


class SqlDialect(models.Model):
    name = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    credential = models.TextField()


class SourceDatatype(models.Model):
    name = models.CharField(max_length=100)
    source = models.ForeignKey(SqlDialect, on_delete=models.CASCADE)


class TargetDatatype(models.Model):
    name = models.CharField(max_length=100)
    target = models.ForeignKey(SqlDialect, on_delete=models.CASCADE)


class DatatypeMapping(models.Model):
    source_datatype = models.ForeignKey(SourceDatatype, on_delete=models.CASCADE)
    target_datatype = models.ForeignKey(TargetDatatype, on_delete=models.CASCADE)
