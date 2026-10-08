from app.api.services.assistant_service import AssistantService


def test_generate_response_returns_message() -> None:
    service = AssistantService()
    result = service.generate_response("hola")

    assert "hola" in result
