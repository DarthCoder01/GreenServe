# GreenServe 🌱⚡

**Carbon-Aware SLA-Tiered Scheduler for LLM Inference**

GreenServe is a prototype scheduling system that reduces the carbon footprint of Large Language Model (LLM) inference workloads by leveraging real-time carbon intensity signals from WattTime.

Instead of treating every inference request equally, GreenServe classifies requests into SLA tiers and schedules them based on both urgency and grid carbon intensity.

---

## Problem Statement

Modern AI systems consume significant amounts of energy.

Traditional schedulers prioritize performance metrics such as latency and throughput but ignore the environmental impact of when computations are executed.

Electricity grids experience periods of:

* **Low-carbon energy availability (Green Periods)**
* **High-carbon energy availability (Dirty Periods)**

Executing non-urgent workloads during greener periods can significantly reduce emissions without affecting critical user experience.

---

## Solution

GreenServe introduces a carbon-aware scheduling layer for AI inference systems.

The scheduler continuously monitors carbon intensity signals and applies SLA-based policies:

| SLA Tier | Priority    | Behavior                                                            |
| -------- | ----------- | ------------------------------------------------------------------- |
| Gold     | Critical    | Always execute immediately                                          |
| Silver   | Important   | Execute immediately under normal conditions                         |
| Bronze   | Best-Effort | Defer during high-carbon periods and execute during greener periods |

This enables environmental optimization while preserving service guarantees.

---

## Features

* Live WattTime carbon signal integration
* Carbon intensity monitoring dashboard
* SLA-tiered request handling
* FastAPI backend
* Interactive frontend dashboard
* Request queue simulation
* Carbon-aware scheduling decisions
* Real-time scheduler visualization

---

## Architecture

```text
                WattTime API
                      │
                      ▼
             Carbon Service
                      │
                      ▼
         Carbon-Aware Scheduler
                      │
                      ▼
              Queue Manager
                      │
                      ▼
                 FastAPI API
                      │
                      ▼
             Web Dashboard UI
```

---

## Current Prototype

### Implemented

* WattTime API integration
* Carbon forecast retrieval
* Carbon intensity visualization
* SLA-based scheduling decisions
* Request queue management
* FastAPI backend services
* Interactive dashboard frontend

### In Progress

* Dynamic queue state management
* Automatic deferred-job execution
* Carbon savings estimation
* Historical analytics

### Future Work

* vLLM integration
* Continuous batching support
* Dynamic SLA adaptation
* Multi-region carbon optimization
* Carbon savings benchmarking
* Production deployment

---

## Tech Stack

### Backend

* Python
* FastAPI
* Requests
* Uvicorn

### Frontend

* HTML
* CSS
* JavaScript

### Carbon Data

* WattTime API

### Version Control

* Git
* GitHub

---

## Running the Project

### Clone Repository

```bash
git clone https://github.com/DarthCoder01/GreenServe.git
cd GreenServe
```

### Create Virtual Environment

```bash
python3 -m venv GreenServe
source GreenServe/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
WATTTIME_USERNAME=your_username
WATTTIME_PASSWORD=your_password
```

### Start Backend

```bash
uvicorn main:app --reload
```

### Open Dashboard

Open:

```text
index.html
```

or serve it locally using:

```bash
python3 -m http.server 8080
```

---

## Example Scheduling Decision

### Dirty Energy Period

```text
Carbon Intensity: 1017

Gold   → Running
Silver → Running
Bronze → Deferred
```

### Green Energy Period

```text
Carbon Intensity: 890

Gold   → Running
Silver → Running
Bronze → Running
```

---

## Research Motivation

This project explores how carbon-aware scheduling can be incorporated into AI serving infrastructure.

The long-term goal is to integrate GreenServe with vLLM and evaluate:

* Carbon reduction
* SLA compliance
* Throughput impact
* Latency trade-offs

---

## Authors

Ashith Rao K and Team

PES University

HPE Career Preview Program (CPP)

---

## License

MIT License
