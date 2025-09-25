import asyncio
import aiodns
import aiosmtplib
from email_validator import validate_email, EmailNotValidError

SEMAPHORE = asyncio.Semaphore(10)  # Limit concurrent DNS/SMTP calls


async def get_resolver():
    loop = asyncio.get_running_loop()
    return aiodns.DNSResolver(loop=loop)


async def validate_format(email: str) -> bool:
    try:
        validate_email(email, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False


async def check_mx(domain: str) -> bool:
    try:
        resolver = await get_resolver()
        answers = await resolver.query(domain, "MX")
        return len(answers) > 0
    except:
        return False


async def get_dns_records(domain: str) -> dict:
    result = {"spf": None, "dkim": None, "dmarc": None}
    resolver = await get_resolver()

    try:
        txts = await resolver.query(domain, "TXT")
        for txt_record in txts:
            txt = txt_record.text
            if txt.startswith("v=spf1"):
                result["spf"] = txt
    except:
        result["spf"] = "not found"

    for selector in ["default", "selector1", "google"]:
        try:
            dkim_txts = await resolver.query(f"{selector}._domainkey.{domain}", "TXT")
            for txt_record in dkim_txts:
                if txt_record.text.lower().startswith("v=dkim1"):
                    result["dkim"] = txt_record.text
        except:
            continue
    if not result["dkim"]:
        result["dkim"] = "not found"

    try:
        dmarc_txts = await resolver.query(f"_dmarc.{domain}", "TXT")
        for txt_record in dmarc_txts:
            if txt_record.text.startswith("v=DMARC1"):
                result["dmarc"] = txt_record.text
    except:
        result["dmarc"] = "not found"

    return result


async def smtp_check(email: str) -> str:
    """Return 'verifiable', 'unverifiable', or False for invalid emails."""
    if "@" not in email:
        return False  # clearly invalid

    domain = email.split("@")[1]
    try:
        resolver = await get_resolver()
        answers = await resolver.query(domain, "MX")
        if not answers:
            return "unverifiable"

        mx_host = str(answers[0].exchange)
        async with SEMAPHORE:
            smtp = aiosmtplib.SMTP(timeout=5)
            await smtp.connect(mx_host)
            await smtp.helo()
            await smtp.mail("test@example.com")
            code, _ = await smtp.rcpt(email)
            await smtp.quit()
            return "verifiable" if code in [250, 251] else "unverifiable"
    except:
        return "unverifiable"


async def validate_email_full(email: str) -> dict:
    # Validate email format first
    format_valid = await validate_format(email)
    if not format_valid:
        return {
            "email": email,
            "format_valid": False,
            "mx_exists": False,
            "smtp_valid": False,
            "dns_records": {"spf": "invalid", "dkim": "invalid", "dmarc": "invalid"},
        }

    domain = email.split("@")[1]
    tasks = [
        check_mx(domain),
        get_dns_records(domain),
        smtp_check(email),
    ]
    mx_exists, dns_records, smtp_valid = await asyncio.gather(*tasks)

    return {
        "email": email,
        "format_valid": True,
        "mx_exists": mx_exists,
        "smtp_valid": smtp_valid,
        "dns_records": dns_records,
    }


async def validate_emails_batch(emails: list[str]) -> list[dict]:
    tasks = [validate_email_full(email) for email in emails]
    return await asyncio.gather(*tasks)
