from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from meya.orb.composer_spec import ComposerEventSpec
from meya.text.event.say import SayEvent
from meya.util.generate_id import generate_member_id
from typing import List


@dataclass
class TestComponentElement(Component):
    foo: str = element_field()

    async def start(self) -> List[Entry]:
        self.log.info(f"TEST COMPONENT")
        text = f"foo={self.foo}"
        text_event = SayEvent(
            member_id=generate_member_id(self.entry.bot_id),
            text=text,
            thread_id=self.entry.thread_id,
            composer=ComposerEventSpec(),
            quick_replies=[],
        )
        return self.respond(text_event)
