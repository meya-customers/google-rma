import meya.util.uuid

from dataclasses import dataclass
from meya.component.element import Component
from meya.entry import Entry
from meya.orb.composer_spec import ComposerSpec
from meya.text.event.say import SayEvent
from meya.util.generate_id import generate_member_id
from typing import List


@dataclass
class RmaComponentElement(Component):
    async def start(self) -> List[Entry]:
        self.log.info(
            "Submitted RMS",
            context={
                "firstname": self.user.firstname,
                "lastname": self.user.lastname,
            },
        )
        text_event = SayEvent(
            member_id=generate_member_id(self.entry.bot_id),
            text=f"Submitted your RMA, your reference {meya.util.uuid.uuid4_hex()}",
            thread_id=self.entry.thread_id,
            composer=ComposerSpec(),
            quick_replies=[],
        )
        return self.respond(text_event)
