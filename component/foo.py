from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from meya.text.event.say import SayEvent
from typing import List


@dataclass
class TestComponentElement(Component):
    foo: str = element_field()

    async def start(self) -> List[Entry]:
        self.log.info(f"TEST COMPONENT")
        text = f"foo={self.foo}"
        text_event = SayEvent(text=text)
        return self.respond(text_event)
