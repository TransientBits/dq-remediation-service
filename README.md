# sap-dq-remediation-service

The remediation service asynchronously consumes Data Quality issues, routes each issue to a
classical or intelligent healer, validates generated outcomes, and persists proposals for review.
It proposes fixes but does not modify source data.

## Development setup

```powershell
uv venv .venv
.\.venv\Scripts\Activate.ps1
uv sync
Copy-Item .env.example .env
uv run uvicorn dq_remediation.main:app --reload
```

The FastAPI process and the message-consuming worker are separate runtime processes. The worker
will be wired to the consumer implementation as that feature is built; it must not run as a
FastAPI background task.

## Project structure

- `src/dq_remediation/api`: HTTP endpoints and routing
- `src/dq_remediation/services`: issue-processing and proposal orchestration
- `src/dq_remediation/domain`: canonical models, routing, and proposal validation
- `src/dq_remediation/healers`: classical and intelligent healing implementations
- `src/dq_remediation/contracts`: HTTP and message contracts
- `src/dq_remediation/ports`: provider-independent application boundaries
- `src/dq_remediation/infrastructure`: PostgreSQL, Service Bus, Neo4j, and agent adapters
- `db/migrations`: database migrations
- `tests`: unit tests, integration tests, and fixtures
