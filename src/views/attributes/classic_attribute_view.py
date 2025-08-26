from typing import override
from models.attributes.attributes import Attributes
from models.attributes.builders.attribute_builder import AttributeBuilder
from models.attributes.builders.classic_attribute_builder import ClassicAttributeBuilder
from views.base_view import BaseView


class ClassicAttributeView(BaseView[Attributes]):

    def __init__(self):
        super().__init__()
        self.builder: AttributeBuilder = ClassicAttributeBuilder()


    @override
    def on_show(self):
        values = self.builder.generate_values()

        self.builder\
            .with_power(values[0])\
            .with_dexterity(values[1])\
            .with_constitution(values[2])\
            .with_intelligence(values[3])\
            .with_wisdom(values[4])\
            .with_charisma(values[5])

        attributes = self.builder.build()
        self._output = attributes

        print(f'Atributos: {attributes}')
