# 03-aws-reliability-security-postgres

A production-minded Database Reliability Engineering toolkit: HA lab, backup/PITR drills, and zero-downtime migration playbooks.

Focus: Postgres reliability, security-by-default habits, and migration-ready operations.


## Why this repo exists
This is a portfolio-grade, runnable toolkit that demonstrates how I approach database reliability work:
safe changes, predictable operations, and recovery you can actually trust.

## The top pains this repo addresses
1) Making databases boring again—high availability, predictable performance, safe backups, and zero/low-downtime migrations with solid tooling and runbooks.
2) Replacing manual, risky changes with automated delivery—repeatable infrastructure, safe deployments, and drift-free environments (IaC + CI/CD + GitOps).
3) Controlling cloud spend while meeting performance targets—capacity planning, right-sizing, and automation that prevents cost regressions.

## Quick demo (local)
Prereqs: Docker + Docker Compose.

```bash
make demo
```

What you get:
- a Postgres primary + replica setup
- PgBouncer for connection pooling
- scripts to verify replication and run backup/restore drills

## Design decisions (high level)
- Prefer drills and runbooks over “tribal knowledge”.
- Keep the lab small but realistic (replication + pooling + backup).
- Make failure modes explicit and testable.

## What I would do next in production
- Add PITR with WAL archiving + periodic restore tests.
- Add SLOs (p95 query latency, replication lag) and alert thresholds.
- Add automated migration checks (preflight, locks, backout plan).

## Test modes (demo vs production)

This repository supports exactly two test execution modes controlled by `TEST_MODE`:

- `demo`: runs **mocked/static** checks only (no Docker, no cloud credentials)
- `production`: runs **real integration** checks when correctly configured (Docker Compose)

Run demo-mode tests:

```bash
make test
```

Run production-mode tests (guarded):

```bash
PRODUCTION_TESTS_CONFIRM=1 make test-production
```

If production prerequisites are missing, the runner prints a precise list of what to set/install.

## Sponsorship and authorship

Sponsored by:
CloudForgeLabs  
https://cloudforgelabs.ainextstudios.com/  
support@ainextstudios.com

Built by:
Freddy D. Alvarez  
https://www.linkedin.com/in/freddy-daniel-alvarez/

For job opportunities, contact:  
it.freddy.alvarez@gmail.com

## License

Personal and other non-commercial use is free.

Commercial use requires paid permission. Contact `it.freddy.alvarez@gmail.com`.

Note: the included `LICENSE` is intentionally **not** an OSI-approved open-source license. It is a noncommercial license that aligns with the “personal use free, commercial use paid” model.
