# ADR: Adopt Redis as Distributed Cache Layer

Status: Proposed
Date: 2025-09-17

System architecture decision:

## Drivers

- Response time constraints arise as client load increases.
- Database is under heavy traffic and latency becomes a problem.
- Need for distributed cache solution that scales better.

## Context
- The application currently relies solely on database queries.
- High-request paths liad to database bottlenecks.
 - We need a cache layer that can handle high-volume reads/writes and scale linearly.

- This AGR assumes that the primary use case is for database read/WRITE optimization.

## Options

- **Redis as a distributed cache.**  Reliable, feature-rich, supports data estructures and high-availability.
- Memcached:  Simpler but less feature-rich (string key only, no persistence.) - single-node focus.
 - Db-only:  No external cache, app and primary database deals with increased load.

## Decision

- We have decided to adopt Redis as the distributed cache layer.

## Consequences

- PERFORMANCE elevated - should see reduced latency and database load.
 - OPERATIONAL COMPLEXITY increased but manageable through redis cluster or replication.
- CACHE INVALIDATION and eventual consistency management required.
 - New system component to monitor, maintain, test, and operate.

## Links/Traceability

- [GitHub Issue #1](https://github.com/dblanari/copilot-agent/issues/1) - cache layer investigation request.

## Validation

- Deployment testing with mockup datasets.
- Response latency metrics validated during performance tests.
- Redis cluster failover scenario to assess high-availability.