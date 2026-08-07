from fastapi import APIRouter, Depends, HTTPException

from app.core.config import get_settings
from app.core.security import require_service_token
from app.schemas.domain import SlackLinkCreate, SlackLinkRead
from app.services.store import store

router = APIRouter(
    prefix="/integrations/slack/users",
    tags=["slack integration"],
    dependencies=[Depends(require_service_token)],
)


@router.get("/{slack_user_id}", response_model=SlackLinkRead)
def get_slack_user(slack_user_id: str, slack_team_id: str) -> SlackLinkRead:
    email = store.links.get((slack_team_id, slack_user_id))
    if email is None:
        raise HTTPException(status_code=404, detail="Slack identity is not linked")
    return SlackLinkRead(user_id=store.users[email], email=email, linked=True)


@router.post("", response_model=SlackLinkRead)
def link_slack_user(payload: SlackLinkCreate) -> SlackLinkRead:
    email = str(payload.email).lower()
    user_id = store.users.get(email)
    if user_id is None:
        registration_url = (
            f"{get_settings().frontend_url}/register?email={email}"
            f"&slack_user_id={payload.slack_user_id}&slack_team_id={payload.slack_team_id}"
        )
        return SlackLinkRead(
            email=payload.email,
            linked=False,
            registration_url=registration_url,
        )
    store.links[(payload.slack_team_id, payload.slack_user_id)] = email
    return SlackLinkRead(user_id=user_id, email=payload.email, linked=True)
