# M2M ENS Registry — Canal Cruises & Charters (`canalcruise.agent.botdesk`)
### The Definitive On-Chain Routing Directory for Maritime Leisure, Canal Tours & Private Boat Rentals

#### Core Protocol & Shared Agent Layer (Universal)
* **Protocol Root:** `botdesk.eth`
* **Agent Permissions & Budgets:** `agentconsent.eth`, `agentallowance.eth`, `agentallowances.eth`

---

#### Step 1: Discovery & Fleet Segmentation (The Market Scan)
* **Global Canal & City Cruises:** `canalcruise.eth`, `canalcruises.eth`, `canaltour.eth`, `canaltours.eth`, `citycruise.eth`
* **General Boat Tours & Trips:** `boattour.eth`, `boattours.eth`, `boattrips.eth`
* **Local Consumer Entry (NL/BE):** `rondvaart.eth`, `rondvaartboot.eth`
* **Private Charters, Salon Boats & Self-Drive Rentals:** `privatecruises.eth`, `privateboattour.eth`, `salonboat.eth`, `boatrental.eth`

#### Step 2: Capacity Pools & Real-Time Availability (ARI Lookup)
* **Live Seat & Vessel Pool Availability:** `canalcruiseavailability.eth`, `boattouravailability.eth`

#### Step 3: Verification, Identity & Policy (Compliance & Terms)
* **Guest & Operator Verification (DID / ZKP):** `guestidentity.eth`, `guestverification.eth`
* **Cancellation & Booking Terms:** `cancellationterms.eth`

#### Step 4: Booking, Escrow & Payment (Locking the Transaction)
* **Shared Settlement Layer:** Requires a certified `settlement_token` issued by the proprietary settlement module to authorize binding bookings and on-chain escrow.
* **Charter & Tour Execution:** `makerental.eth`
* **Escrow, Payments & Split-Billing:** `bookingescrow.eth`, `paymentescrow.eth`, `rentalpayment.eth`, `bookinginvoice.eth`

#### Step 5: Boarding, Digital Tickets & Session Start (Physical Handover)
* **Digital Boarding Passes & QR/NFT Tickets:** `boatticket.eth`, `boattourticket.eth`
* **Vessel Session Activation:** `startrental.eth`

#### Step 6: Disembarkation & Settlement (Completion & Release)
* **Escrow Release & Completion:** Automated release of `bookingescrow.eth` / `paymentescrow.eth` upon verified ticket scan or charter completion.

#### Step 7: Cancellations, Refunds & Disputes (Post-Cruise & Weather Incidents)
* **Tour & Cruise Cancellations:** `canalcruisecancellation.eth`, `boattourcancellation.eth`, `bookingcancellation.eth`
* **Refunds & Dispute Resolution:** `canalcruiserefund.eth`, `boattourrefund.eth`, `bookingrefund.eth`, `bookingdispute.eth`
