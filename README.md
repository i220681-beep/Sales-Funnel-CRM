# Sales Funnel CRM (Data Structures)

A small CRM/sales-pipeline simulator built to demonstrate core data structures in a real business workflow: managing leads, follow-ups, and customer records for a sales team.

**[Live interactive demo →](https://m-ibtisam.github.io/sales-funnel-crm/)** *(update link once GitHub Pages is enabled — see below)*

## What it does

- **Lead queue (FIFO)** — new leads enter a queue and are processed fairly, in order, with no lead skipped.
- **Follow-up stack (LIFO)** — the most recent follow-up task surfaces first, like a to-do list that prioritises what just happened.
- **Sorting** — rank customers by deal potential using Bubble, Selection, or Insertion sort.
- **Searching** — find a customer by name (linear search) or by ID (binary search on a sorted index).

## Why it's interesting beyond the coursework

It's a working model of a real product decision every sales/CRM tool has to make: *what order do things get handled in, and why*. FIFO vs. LIFO isn't just a textbook contrast here — it maps directly onto "don't make leads wait" vs. "don't let momentum on a hot follow-up go cold," which is the kind of trade-off a product owner has to reason about and design for.

## Contents

- `sales_funnel_system.py` — original Python implementation (Queue, Stack, Sorting, Searching, console menu)
- `index.html` — browser-based interactive version of the same logic, for demoing without a Python environment

## Run it locally

```bash
python sales_funnel_system.py
```

## Team

Ibtisam Kayani · Ahsan Chohan — Data Structures for Business Applications, FAST-NUCES
