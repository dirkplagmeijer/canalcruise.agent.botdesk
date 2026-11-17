from google.adk.agents import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a

def resolve_m2m_endpoint(category: str, step: int) -> dict:
    """Maps the 7-step canal cruise lifecycle to verified BotDesk ENS endpoints while keeping settlement proprietary."""
    routes = {
        "canalcruise": {
            1: {"endpoint": "canalcruise.eth", "action": "discovery"},
            2: {"endpoint": "canalcruiseavailability.eth", "action": "availability_check"},
            3: {"endpoint": "guestidentity.eth", "action": "verification"},
            4: {"endpoint": "bookingescrow.eth", "action": "booking_lock", "requires": "certified_settlement_token"},
            5: {"endpoint": "boatticket.eth", "action": "digital_ticket_issuance"},
            6: {"endpoint": "paymentescrow.eth", "action": "settlement_release", "requires": "certified_settlement_token"},
            7: {"endpoint": "canalcruisecancellation.eth", "action": "arbitration_refunds"},
        }
    }
    return routes.get(category.lower(), {}).get(step, {"error": "Invalid step or category"})

# The ADK Gateway Agent handling incoming A2A requests
gateway_agent = Agent(
    name="botdesk_canalcruise_gateway",
    model="gemini-2.5-flash",
    instruction=(
        "Route incoming canal cruise, boat tour, and private charter requests across the 7-step M2M lifecycle. "
        "Return the corresponding verified .eth endpoint and enforce a certified settlement_token for booking and settlement."
    ),
    tools=[resolve_m2m_endpoint]
)

# Exposes the agent directly as an A2A server (reads your existing agent-card.json)
a2a_app = to_a2a(gateway_agent, agent_card="agent-card.json")
