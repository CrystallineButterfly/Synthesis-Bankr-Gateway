# SelfFunding Model Router

- **Repo:** https://github.com/CrystallineButterfly/Synthesis-Bankr-Gateway
- **Primary track:** Best Bankr LLM Gateway Use
- **Overlap targets:** Bond.credit, Uniswap Agentic Finance, Lido stETH Treasury, PayWithLocus, Venice Private Agents, MetaMask Delegations
- **Primary contract:** ComputeBudgetVault
- **Primary operator module:** bankr_router
- **Live TxIDs:** PENDING
- **ERC-8004 registrations:** PENDING
- **Demo link:** docs/demo_video_script.md

A self-funding model router that picks inference backends by task class, cost, and urgency while preserving auditability and spending limits.

## Track evidence

- `artifacts/onchain_intents/lido_yield_route.json`
- `artifacts/onchain_intents/metamask_delegations_delegate_scope.json`

## Latest verification

```json
{
  "status": "verified",
  "project_name": "SelfFunding Model Router",
  "track": "Best Bankr LLM Gateway Use",
  "plan_id": "0x3cdb942847ce0301b8f35d2d8da38f357409af42f8f6102b2db83586f58a71bb",
  "simulation_hash": "0x65e8099545d3d1c7faea61557de3c11730e44f9d347ae74fd7ce265edf65ccec",
  "execution_status": "offline_prepared",
  "tx_ids": [],
  "artifact_paths": [
    "artifacts/onchain_intents/lido_yield_route.json",
    "artifacts/onchain_intents/metamask_delegations_delegate_scope.json"
  ],
  "partner_statuses": {
    "Bankr Gateway": "awaiting_credentials",
    "Bond.credit": "awaiting_credentials",
    "Uniswap": "awaiting_credentials",
    "Lido": "prepared_contract_call",
    "PayWithLocus": "awaiting_credentials",
    "Venice": "awaiting_credentials",
    "MetaMask Delegations": "prepared_contract_call"
  },
  "created_at": "2026-03-19T03:52:08+00:00"
}
```
