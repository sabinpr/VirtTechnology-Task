# Interview Tasks - Python Projects

This repository contains two Python projects completed as part of an interview assessment:

1. **Task A: Travelling Salesman Problem (TSP)**
2. **Task B: Scalable Email Validation API**

---

## Task A: Travelling Salesman Problem (TSP)

### Problem Statement

A salesman must visit 6 cities: **A, B, C, D, E, F**, starting and ending at **City A**.  
Distances (in kilometers) between the cities:

| From/To | A   | B   | C   | D   | E   | F   |
| ------- | --- | --- | --- | --- | --- | --- |
| A       | 0   | 10  | 15  | 20  | 25  | 30  |
| B       | 10  | 0   | 35  | 25  | 17  | 28  |
| C       | 15  | 35  | 0   | 30  | 28  | 40  |
| D       | 20  | 25  | 30  | 0   | 22  | 16  |
| E       | 25  | 17  | 28  | 22  | 0   | 35  |
| F       | 30  | 28  | 40  | 16  | 35  | 0   |

**Goal:**

- Start from City A
- Visit each city exactly once
- Return to City A
- Find the shortest possible route and total distance.

### Solution

- Implemented using a **brute-force permutation approach** in Python.
- Computes all possible routes starting from **City A**, calculates their total distances, and selects the shortest route.

**Example Output:**

```text
Shortest route: A -> B -> E -> D -> F -> C -> A
Total distance: 119 km
```

## Task B: Scalable Email Validation API

### Project Overview

This project demonstrates a Python-based email validation tool with an API using Django REST Framework.

**Features:**

- Batch Email Validation: Accepts multiple emails in a single POST request.
- Format Validation: Checks if the email structure is valid.
- DNS Validation: Checks MX records to confirm the domain can receive emails.
- SMTP Verification: Attempts to verify the email directly via SMTP (returns "unverifiable" for blocked domains).
- DNS Records: Fetches SPF, DKIM, and DMARC records for the domain.
- Async Processing: Uses asyncio, aiodns, and aiosmtplib for efficient concurrent validation of thousands of emails.
- Graceful Error Handling: Invalid emails or random strings are handled without crashing the API.

### API Endpoint

**POST** /api/validate-emails/

**Request Body Example:**

```json
{
  "emails": [
    "test@example.com",
    "hello@world.com",
    "sabinprajapati7@gmail.com",
    "invalid-email"
  ]
}
```

**Response Example:**

```json
[
  {
    "email": "test@example.com",
    "format_valid": true,
    "mx_exists": true,
    "smtp_valid": "unverifiable",
    "dns_records": {
      "spf": "v=spf1 -all",
      "dkim": "v=DKIM1; p=",
      "dmarc": "v=DMARC1;p=reject;sp=reject;adkim=s;aspf=s"
    }
  },
  {
    "email": "hello@world.com",
    "format_valid": true,
    "mx_exists": true,
    "smtp_valid": "unverifiable",
    "dns_records": {
      "spf": "v=spf1 include:_spf.google.com ~all",
      "dkim": "v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCZWjYKNFNEK3Gjg912+8N7vFs3nEEuijo38Ieshkam7chlfOYwrybfOR0d0JGDJ3pnpc7yr7CEka1iKERTljcQwcq5bKSHxHXCSHa2CPtfpWMAZjuFV7xaF8Hv6uqR/NoaRYeV/ZLBAg7CqAkq331fQrL3ycKnQBeynnqvDYT/+wIDAQAB",
      "dmarc": "v=DMARC1; p=none; rua=mailto:dmarc-reports@world.com"
    }
  },
  {
    "email": "sabinprajapati7@gmail.com",
    "format_valid": true,
    "mx_exists": true,
    "smtp_valid": "unverifiable",
    "dns_records": {
      "spf": "v=spf1 redirect=_spf.google.com",
      "dkim": "not found",
      "dmarc": "v=DMARC1; p=none; sp=quarantine; rua=mailto:mailauth-reports@google.com"
    }
  },
  {
    "email": "invalid-email",
    "format_valid": false,
    "mx_exists": false,
    "smtp_valid": false,
    "dns_records": {
      "spf": "invalid",
      "dkim": "invalid",
      "dmarc": "invalid"
    }
  }
]
```

## Author

Sabin Prajapati
