"""Project-specific context module."""

from __future__ import annotations

PROJECT_CONTEXT = {
  "project_name": "SelfFunding Model Router",
  "track": "Best Bankr LLM Gateway Use",
  "pitch": "A self-funding model router that picks inference backends by task class, cost, and urgency while preserving auditability and spending limits.",
  "overlap_targets": [
    "Bond.credit",
    "Uniswap Agentic Finance",
    "Lido stETH Treasury",
    "PayWithLocus",
    "Venice Private Agents",
    "MetaMask Delegations"
  ],
  "goals": [
    "discover a bounded opportunity",
    "plan a dry-run-first action",
    "verify receipts and proofs"
  ]
}


def seed_targets() -> list[str]:
    """Return the first batch of overlap targets for planning."""
    return list(PROJECT_CONTEXT['overlap_targets'])
