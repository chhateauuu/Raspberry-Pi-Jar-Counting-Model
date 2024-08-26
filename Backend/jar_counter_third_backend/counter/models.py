from django.db import models

class JarCount(models.Model):
    count = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    shift1_start = models.TimeField(default="08:00")
    shift2_start = models.TimeField(default="20:00")

    class Meta:
        indexes = [
            models.Index(fields=['timestamp']),
        ]

    def __str__(self):
        return f"{self.count} jars at {self.timestamp}"

class ShiftTiming(models.Model):
    shift1_start = models.TimeField(default="08:00")
    shift2_start = models.TimeField(default="20:00")

    def __str__(self):
        return f"Shift 1 starts at {self.shift1_start}, Shift 2 starts at {self.shift2_start}"

