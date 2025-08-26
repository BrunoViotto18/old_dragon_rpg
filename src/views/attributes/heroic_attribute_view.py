from models.attributes.builders.heroic_attribute_builder import HeroicAttributeBuilder
from .base_attribute_view import BaseAttributeView


class HeroicAttributeView(BaseAttributeView):

    def __init__(self):
        super().__init__(HeroicAttributeBuilder())
