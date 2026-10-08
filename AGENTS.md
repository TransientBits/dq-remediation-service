# AGENTS.md

## Service purpose

This repository contains the SAP Data Quality remediation service. It asynchronously consumes DQ
issues, validates their message contracts, processes each issue idempotently, routes it to a
classical or intelligent healer, validates the resulting proposal, and persists the proposal and
processing evidence for review.

The service proposes fixes; it must not modify original source data. If evidence is insufficient
or conflicting, return a manual-investigation outcome rather than inventing a fix.

## Runtime and technology

- Python, FastAPI, Pydantic, and `uv`
- PostgreSQL through Psycopg 3
- Azure Service Bus
- OpenAI Agents SDK for the intelligent-healer workflow
- Neo4j through the official Python driver

The API and message-consuming worker are separate processes. Do not implement the consumer as a
FastAPI background task.

## Design philosophy

- Keep FastAPI endpoints thin: validate HTTP input, call a service, and translate its result.
- Put feature orchestration in services; keep domain rules in domain and healer modules.
- Keep SQL in infrastructure repositories/providers, not in endpoints, services, or domain code.
- Keep SDK-specific types and behavior inside infrastructure adapters.
- Use Pydantic for canonical platform models and external boundaries.
- Use small, typed Protocol ports at meaningful provider or replacement boundaries; avoid generic
  base classes, unnecessary interfaces, deep inheritance, and speculative frameworks.
- Keep domain code independent of web, database, message-broker, graph, and LLM SDKs.
- Make message processing idempotent and explicit about retries, dead-lettering, correlation, and
  acknowledgement. Complete a message only after its outcome has been persisted successfully.
- Treat LLM output as untrusted: validate structured output deterministically before persistence
  or human review. LLMs must not execute unrestricted database operations or modify source data.
- Preserve source values and enough issue, strategy, evidence, validation, status, and timestamp
  information to explain every proposal.

## Healer boundaries

- Route issues through configuration using `rule_id`.
- Classical strategies are named, deterministic or statistical implementations.
- The intelligent healer uses a one-way planning step, an iterative investigator with controlled
  SQL and Knowledge Graph specialists, and a one-way proposal-generation step.
- Do not add planner/investigator replanning or proposal/investigator feedback loops in this POC.

## Implementation guidance

- Follow the existing feature-oriented structure under `services/` and concrete provider structure
  under `infrastructure/`.
- Implement incrementally, prioritizing a reliable end-to-end classical-healing path before the
  intelligent healer.
- Make focused changes, reuse established patterns, and test the behavior affected by each change.
- Avoid empty placeholders, unrelated cleanup, and features outside the agreed POC scope.
