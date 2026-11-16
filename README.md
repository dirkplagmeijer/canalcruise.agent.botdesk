#### canalcruise.agent.botdesk
## The Web2.5 Layer for AI-Agents in Canal Cruises, Boat Tours & Private Charters

BotDesk Maritime introduces a cross-chain, location-agnostic maritime leisure taxonomy and hybrid Web2.5 discovery gateway for agentic AI systems (ChatGPT, Gemini, Google A2A, and MCP agents) and fleet operators, bypassing high OTA commissions.

📩 Visit [LinkedIn](https://linkedin.com) or contact **`canalcruise@agentbotdesk.com`** to connect and explore strategic partnerships or integration opportunities.

---

### 🌐 Live Web2.5 Discovery & A2A Gateway Endpoints
* **Official A2A Discovery Manifest:** `https://agentbotdesk.com`
* **JSON-RPC 2.0 Agent Endpoint:** `POST` https://agentbotdesk.com
* **Lightweight ENS Route Resolver:** `GET` https://agentbotdesk.com/route?category=canalcruise&step=1

---

### 📂 Repository Structure
* **`/core-architecture`** – Contains `M2M_ENS_REGISTRY.md` (The master M2M on-chain ENS directory for cruises, boat tours, and private charters).
* **`/schemas`** – Contains `cruise_taxonomy_schema.json` (Standardized JSON data model for capacity pools, tickets, and private charters).
* **`/sdk`** – Contains official Python and TypeScript A2A client SDKs (`botdesk_canalcruise_sdk.py` & `botdesk-canalcruise-sdk.ts`) with Sandbox mode.
* **`/web25-gateway`** – Contains `agent-card.json` (A2A discovery manifest for agentic AI systems).

---

### 🗺️ The 7-Step Maritime Taxonomy & Registry Lifecycle
1. **Discovery & Fleet Segmentation:** Scans global canal cruises, boat tours, and charters via ENS endpoints (`canalcruise.eth`, `boattour.eth`, `salonboat.eth`).
2. **Capacity Pools & Real-Time Availability:** Queries live seat and vessel pool availability per slot (`canalcruiseavailability.eth`).
3. **Verification, Identity & Policy:** Validates traveler credentials and cancellation terms (`guestidentity.eth`).
4. **Booking, Escrow & Payment:** Executes bookings and handles escrow via proprietary settlement tokens and endpoints (`makerental.eth`, `bookingescrow.eth`).
5. **Boarding & Digital Tickets:** Issues QR/NFT passes and activates self-drive sessions (`boatticket.eth`).
6. **Disembarkation & Settlement:** Completes sessions and releases escrow upon verified boarding.
7. **Cancellations & Disputes:** Handles weather incidents, refunds, and dispute resolution (`canalcruisecancellation.eth`).

---

### 🛠️ Technical Roadmap & Licensing
* **Phase 1:** Core logical frameworks, 7-step taxonomy, and Web2.5 A2A Discovery Gateway finalized.
* **Phase 2:** Compiling datasets into an OpenAPI 3.0 Specification (`openapi.yaml`).
* **Phase 3:** Connecting fleet reservation systems to the deterministic M2M routing layer.

**License:** Open-source under the MIT License. Note that the core Payment and Escrow Smart Contract Module is proprietary and requires a verified partnership and certified `settlement_token`. Inquiries via [LinkedIn](https://linkedin.com) or **`canalcruise@agentbotdesk.com`**.
