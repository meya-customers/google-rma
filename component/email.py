from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from meya.orb.composer_spec import ComposerSpec
from meya.text.event.say import SayEvent
from meya.util.generate_id import generate_member_id
from typing import List


@dataclass
class EmailComponentElement(Component):
    email: str = element_field()
    text: str = element_field()

    async def start(self) -> List[Entry]:
        self.log.info(f"Sent email to {self.email}")
        text_event = SayEvent(
            member_id=generate_member_id(self.entry.bot_id),
            text=f"Sent to {self.email}",
            thread_id=self.entry.thread_id,
            composer=ComposerSpec(),
            quick_replies=[],
        )
        return self.respond(text_event)
