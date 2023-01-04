from django.db import models
import uuid
import qrcode
import base64
from io import BytesIO

MATERIAL_CHOICES = (
    ("PLA", "PLA"),
    ("ABS", "ABS"),
    ("PETG", "PETG"),
    ("ASA", "ASA"),
    ("HIPS", "HIPS"),
    ("Nylon", "Nylon"),
    ("PC", "PC"),
    ("PP", "PP"),
    ("TPU", "TPU"),
    ("Special", "Special"),
)


# Create your models here.
class Filament(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    brand = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=MATERIAL_CHOICES)
    material = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity_in_kg = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"[{self.material}] {self.brand} - {self.name}"

    @property
    def price_per_kg(self):
        return round(self.price / self.quantity_in_kg, 2)

    @property
    def permanent_url(self):
        return f"http://filament.jlugao.com/filaments/{self.uuid}/"

    @property
    def price_in_reais(self):
        return "R$ " + str(self.price_per_kg).replace(".", ",")

    @property
    def qr_code_for_permanent_url(self):
        qr = qrcode.make(self.permanent_url)
        with BytesIO() as buffer:
            qr.save(buffer, format="PNG")
            b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return f"data:image/png;base64,{b64}"


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
