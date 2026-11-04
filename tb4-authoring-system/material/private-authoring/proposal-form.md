# Proposal form answers

Fill this for every proposal, beside `proposal.md`. Copy the answers into the live form. Keep each of the three long fields under 2048 bytes. `proposal.md` stays heading-free and under 2000 characters.

```
category:
subcategory:
programming_language:
expert_time_hours:
expert_time_quantity: build time (C-EXPERT-TIME), not drafting time and not solve time
runs_as_root:
single_container:
```

## Title

What the task asks for, in one line.

## Proposal Markdown

Point at `proposal.md`. The body covers the task, the starting inputs, the expected outcome, programmatic verification, why the naive approach fails and why the work is useful, and why an engineer who already knows the answer can implement it in a few hours.

## Where the task comes from

The real request, incident, or workflow this task is based on.

## The larger problem it belongs to

The bigger engineering problem this task is one part of.

## What solving it is worth

Who benefits when this is solved, and how.

## Environment

- [ ] The task runs as root. The environment's final user is root; no USER line switches to another account.
- [ ] Everything runs in one container. No separate database, web server, or other service next to the task container.
