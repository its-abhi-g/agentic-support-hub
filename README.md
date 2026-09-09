# Agentic Support Hub MVP

## Overview

Agentic Support Hub is an AI-powered enterprise support platform designed to automate support interactions related to:

- ChatGPT Enterprise
- OpenAI API
- Codex
- Partner U
- Hackathon Enablement
- Access & Troubleshooting Workflows

The platform combines Semantic Search, Retrieval-Augmented Generation (RAG), LLM-powered responses, Case Management, Escalation Workflows, and Operational Dashboards to deliver an AI-first support experience.

---

## Problem Statement

Enterprise users frequently require support related to access requests, product onboarding, API usage, authentication, troubleshooting, and learning resources.

Traditional support models depend heavily on manual intervention, resulting in repetitive workloads and slower resolution times.

This project demonstrates an Agentic AI approach where:

- AI resolves common support requests.
- Human support handles exceptions.
- Every interaction becomes a support case.
- Low-confidence responses are automatically escalated.
- Knowledge is grounded using approved documentation.

---

## Objectives

- Reduce manual support effort.
- Enable AI-first support.
- Implement case management.
- Enable confidence-based escalation.
- Maintain a searchable support knowledge base.
- Provide operational analytics.

---

# Solution Architecture

## High-Level Flow

```text
User
  ↓
Streamlit Support Hub
  ↓
Supervisor Agent
  ↓
Product Classification
  ↓
Semantic Retrieval (RAG)
  ↓
Knowledge Base (MySQL)
  ↓
Sentence Transformer Embeddings
  ↓
Ollama (Llama 3.2)
  ↓
AI Response
  ↓
Case Management
  ↓
Dashboard & Analytics
```

---

## Core Components

### 1. Support Assistant

Responsible for:

- Question Intake
- Product Identification
- Case Creation
- Response Generation
- Escalation Routing

### 2. Knowledge Base

Stores:

- ChatGPT Knowledge Articles
- OpenAI API Articles
- Codex Articles
- Partner U Articles
- Support Procedures

### 3. Semantic Retrieval Layer

Uses:

- Sentence Transformers
- Embeddings
- Cosine Similarity Search

to retrieve the most relevant support content.

### 4. Local LLM Layer

Uses:

- Ollama
- Llama 3.2

to generate grounded support responses.

### 5. Case Management Layer

Tracks:

- Case ID
- Product
- Question
- Response
- Escalation Status

### 6. Dashboard Layer

Provides:

- Total Cases
- Escalations
- AI Resolved Cases
- Knowledge Articles
- Product Distribution
- Recent Cases
- Escalation Monitoring

---

# Features

## Support Assistant

✅ Natural language support requests

✅ Product classification

✅ Case ID generation

✅ Knowledge-based retrieval

✅ LLM-generated responses

✅ Confidence scoring

✅ Human escalation workflow

---

## RAG (Retrieval-Augmented Generation)

✅ Knowledge article repository

✅ Embedding generation

✅ Semantic search

✅ Context-based response generation

---

## Escalation Workflow

✅ Confidence threshold evaluation

✅ Low-confidence escalation

✅ Escalation tracking

✅ Human-review routing

---

## Dashboard

✅ Total cases

✅ Escalation count

✅ AI resolved count

✅ Knowledge article count

✅ Product distribution

✅ Resolution overview

✅ Recent cases

✅ Recent escalations

---

# Technology Stack

## Backend

- Python

## Frontend

- Streamlit

## Database

- MySQL Community Edition

## LLM

- Ollama
- Llama 3.2

## Semantic Search

- Sentence Transformers
- Cosine Similarity

## Analytics

- Pandas
- Plotly

## Environment Management

- Python Virtual Environment
- Python Dotenv

---

# Project Structure

```text
agentic-support-hub/

├── agents/
│
├── dashboard/
│   ├── dashboard.py
│   └── dashboard_view.py
│
├── database/
│   ├── case_service.py
│   ├── load_knowledge.py
│   └── search_knowledge.py
│
├── documents/
│   └── knowledge_seed.json
│
├── rag/
│   ├── retriever.py
│   ├── semantic_search.py
│   └── store_embeddings.py
│
├── services/
│   ├── llm_service.py
│   └── support_service.py
│
├── ui/
│   └── app.py
│
├── .env
├── README.md
└── requirements.txt
```

---

# Database Design

## Cases Table

Stores:

- Case ID
- Product
- Category
- Status
- Question
- AI Response
- Timestamp

## Knowledge Table

Stores:

- Knowledge Articles
- Product Mapping
- Embeddings

## Escalations Table

Stores:

- Escalated Cases
- Escalation Reason
- Timestamp

---

# Confidence-Based Decision Flow

## High Confidence

```text
Confidence >= 0.40
```

Action:

```text
Generate AI Response
Update Case
Mark as AI Resolved
```

---

## Low Confidence

```text
Confidence < 0.40
```

Action:

```text
Create Escalation Record
Notify Human Review Path
Return Escalation Response
```

---

# Example Scenarios

## Scenario 1

Question:

```text
How do I install Codex?
```

Outcome:

```text
Product = Codex
Knowledge Retrieved
AI Resolved
```

---

## Scenario 2

Question:

```text
How to setup code AI intelligence in my system?
```

Outcome:

```text
Low Confidence
Escalated To Human Review
```

---

# Dashboard KPIs

The dashboard currently tracks:

- Total Cases
- AI Resolved Cases
- Escalation Count
- Knowledge Articles
- Product Distribution
- Resolution Overview
- Recent Cases
- Recent Escalations

---

# How To Run

## Activate Virtual Environment

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Launch Application

```bash
streamlit run ui/app.py
```

## Open Browser

```text
http://localhost:8501
```

---

# Current MVP Stack

- Python
- Streamlit
- MySQL
- Sentence Transformers
- Ollama
- Llama 3.2
- Plotly

---

# Future OpenAI Production Migration

The solution architecture has been intentionally designed to support migration to the OpenAI ecosystem.

## Current MVP

```text
Ollama
Llama 3.2
MySQL
Sentence Transformers
Streamlit
```

## Target OpenAI Architecture

```text
GPT-5
Responses API
Agents SDK
Vector Stores
File Search
ChatGPT Enterprise
```

This allows the MVP to demonstrate complete functionality while remaining compatible with future enterprise OpenAI adoption.

---

# Key Learnings

- Agentic Workflow Design
- Retrieval-Augmented Generation (RAG)
- Case Management Systems
- Human-in-the-Loop Escalation
- Semantic Search
- Local LLM Integration
- Dashboard Analytics
- AI Support Automation

---

# Author

**Abhishek Gupta**  
Software Engineer  
Agentic Support Hub MVP
