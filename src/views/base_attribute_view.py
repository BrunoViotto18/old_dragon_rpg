
from typing import override
from models.attributes.builders.attribute_builder import AttributeBuilder
from views.base_view import BaseView


class BaseAttributeView(BaseView):

    def __init__(self, attribute_builder: AttributeBuilder):
        super().__init__()
        self._attribute_builder: AttributeBuilder = attribute_builder


    @override
    def on_show(self):
        labels = ['Força', 'Destreza', 'Constituição', 'Inteligência', 'Sabedoria', 'Carisma']
        values = self._attribute_builder.generate_values()

        while len(values) != 0:
            label, value = self._choose_value(labels, values)

            labels.remove(label)
            values.remove(value)

            if label == 'Força':
                self._attribute_builder.with_power(value)
            elif label == 'Destreza':
                self._attribute_builder.with_dexterity(value)
            elif label == 'Constituição':
                self._attribute_builder.with_constitution(value)
            elif label == 'Inteligência':
                self._attribute_builder.with_intelligence(value)
            elif label == 'Sabedoria':
                self._attribute_builder.with_wisdom(value)
            elif label == 'Carisma':
                self._attribute_builder.with_charisma(value)

        self._console_helper.clear_console()

        attributes = self._attribute_builder.build()

        print(f'Atributos: {attributes}')


    def _choose_value(self, labels: list[str], values: list[int]) -> tuple[str, int]:
        print('Valores disponíveis')
        for index, label in enumerate(values):
            print(f'[ {index + 1} ] {label}')

        value_index = int(input('Selecione um dos valores para ser atribuido: ')) - 1

        self._console_helper.clear_console()


        print('Atributos disponíveis')
        for index, label in enumerate(labels):
            print(f'[ {index + 1} ] {label}')

        label_index = int(input(f'Selecione o atributo para o valor {values[value_index]}: ')) - 1

        self._console_helper.clear_console()


        return labels[label_index], values[value_index]
