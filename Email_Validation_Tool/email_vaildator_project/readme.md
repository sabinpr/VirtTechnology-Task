# Email Validation API

This project provides an **Email Validation API** built with **Django REST Framework** and **async Python** for validating multiple email addresses in batch. It checks email format, domain records, and attempts SMTP verification.

---

## Features

- **Email Format Validation**  
  Validates email structure using `email-validator`. Invalid formats are immediately flagged.

- **MX Record Check**  
  Checks whether the domain has valid MX records to accept emails.

- **DNS Records Lookup**  
  Fetches key DNS records for each domain:

  - **SPF**
  - **DKIM**
  - **DMARC**

- **SMTP Verification**  
  Attempts to verify the email via SMTP. Many domains block direct verification, so results may be `"unverifiable"`.

- **Batch Validation**  
  Accepts multiple emails in a single POST request and returns results for all.

- **Handles Invalid Inputs Gracefully**  
  Returns structured responses even for random strings or invalid emails.

---

## API Endpoint

**POST** `/api/validate-emails/`

### Request Body

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

### Response

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

## Instalation

1. Clone the repository:

```
git clone git@github.com:sabinpr/VirtTechnology-Task.git
cd Email_Validation_Tool/email_validator_project/
```

2. Create a virtual environment and install dependencies:

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

3. Run the Django development server:

```
python manage.py runserver

```

## Notes

- SMTP Verification Limitation: Many email providers block SMTP verification, so smtp_valid may return "unverifiable" for legitimate emails.
- Concurrency: Async calls with asyncio and aiodns make the API fast for batch validation.
- Error Handling: Invalid emails or random strings are handled gracefully without crashing the API.

## Tech Stack

- Python
- Django
- Django REST Framework
- asyncio / aiodns / aiosmtplib
- email-validator

## Author

Sabin Prajapati
