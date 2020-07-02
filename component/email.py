from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from meya.text.event.say import SayEvent
from typing import List


@dataclass
class EmailComponentElement(Component):
    email: str = element_field()
    text: str = element_field()

    async def start(self) -> List[Entry]:
        self.log.info(f"Sent email to {self.email}")
        text_event = SayEvent(text=f"Sent to {self.email}")
        return self.respond(text_event)
