import pytest

from component.submit_rma import SubmitRmaComponent
from meya.element.element_test import create_component_start_entry
from meya.element.element_test import create_flow_next_entry
from meya.element.element_test import create_log_message_entry
from meya.element.element_test import create_user
from meya.element.element_test import verify_process_element
from meya.log.level import Level
from meya.orb.composer_spec import ComposerEventSpec
from meya.text.event.say import SayEvent
from meya.util.generate_id import generate_member_id


@pytest.mark.asyncio
async def test_submit_rma_component():
    component = SubmitRmaComponent()
    firstname = "Firstname"
    lastname = "Lastname"
    component_start_entry = create_component_start_entry(component)
    text_event = SayEvent(
        composer=ComposerEventSpec(),
        member_id=generate_member_id(component_start_entry.bot_id),
        quick_replies=[],
        text="Submitted your RMA, your reference ~0",
        thread_id=component_start_entry.thread_id,
    )
    next_entry = create_flow_next_entry(component_start_entry)
    log_entry = create_log_message_entry(
        component_start_entry,
        level=Level.INFO,
        message="Submitted RMS",
        context={"firstname": firstname, "lastname": lastname},
    )
    await verify_process_element(
        component,
        component_start_entry,
        [text_event, next_entry, log_entry],
        user=create_user(data=dict(firstname=firstname, lastname=lastname)),
    )
