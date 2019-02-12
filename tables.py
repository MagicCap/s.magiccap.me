from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class LinkShortener(Model):
    class Meta:
        read_capacity_units = 3
        write_capacity_units = 1
        region = "eu-west-2"
        table_name = "magiccap_link_shortener"

    short = UnicodeAttribute(hash_key=True)
    url = UnicodeAttribute()
