from models.attributes.builders.adventurer_attribute_builder import AdventurerAttributeBuilder
from .base_attribute_view import BaseAttributeView


class AdventurerAttributeView(BaseAttributeView):

    def __init__(self):
        super().__init__(AdventurerAttributeBuilder())
