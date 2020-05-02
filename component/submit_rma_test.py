import pytest

from component.submit_rma import RmaComponentElement
from meya.component.entry.start import ComponentStartEntry
from meya.db.model.user import UserModel
from meya.element.element_test import to_spec_dict
from meya.element.element_test import verify_process_element
from meya.flow.entry.next import FlowNextEntry
from meya.log.entry.message import LogMessageEntry
from meya.log.level import Level
from meya.log.scope import Scope
from meya.orb.composer_spec import ComposerSpec
from meya.text.event.say import SayEvent
from meya.util.generate_id import generate_member_id
from unittest.mock import MagicMock


# example test...remove `_x` to enable
@pytest.mark.skip(reason="Need to load element from TypeRegistry")
@pytest.mark.asyncio
async def _xtest_submit_rma_component():
    bot_id = "test_bot"
    component = RmaComponentElement()
    stack = []
    data = {"foo": "bar"}
    flow = "rma_test"
    firstname = "Firstname"
    lastname = "Lastname"
    start_component_entry = ComponentStartEntry(
        bot_id=bot_id,
        spec=to_spec_dict(component),
        data=data,
        flow=flow,
        index=0,
        stack=stack,
        thread_id="t-0",
    )
    component.entry = start_component_entry
    text_event = SayEvent(
        composer=ComposerSpec(),
        member_id=generate_member_id(bot_id),
        quick_replies=[],
        text="Submitted your RMA, your reference ~0",
        thread_id="t-0",
    )
    next_entry = FlowNextEntry(
        bot_id=bot_id,
        data=data,
        flow=flow,
        index=0,
        stack=stack,
        thread_id="t-0",
    )
    log_entry = LogMessageEntry(
        args=[],
        context={
            "firstname": firstname,
            "lastname": lastname,
            "sub_entry": {"id": None, "type": "engine.meya.component.start"},
        },
        level=Level.INFO,
        message="Submitted RMS",
        scope=Scope.SYSTEM,
        timestamp=1561492810010,
    )
    await verify_process_element(
        element=component,
        sub_entry=start_component_entry,
        expected_pub_entries=[text_event, next_entry, log_entry],
        bot_id=bot_id,
        user=UserModel(
            __user_id__=MagicMock(),
            __data__=dict(firstname=firstname, lastname=lastname),
        ),
    )
