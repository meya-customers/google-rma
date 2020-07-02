import meya.util.uuid

from dataclasses import dataclass
from meya.component.element import Component
from meya.entry import Entry
from meya.text.event.say import SayEvent
from typing import List


@dataclass
class SubmitRmaComponent(Component):
    async def start(self) -> List[Entry]:
        self.log.info(
            "Submitted RMS",
            context={
                "firstname": self.user.firstname,
                "lastname": self.user.lastname,
            },
        )
        text_event = SayEvent(
            text=f"Submitted your RMA, your reference {meya.util.uuid.uuid4_hex()}"
        )
        return self.respond(text_event)
