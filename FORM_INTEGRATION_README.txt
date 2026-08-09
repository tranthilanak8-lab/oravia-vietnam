ORAVIA V14 — FORM & LEAD INTEGRATION

Current state
- Visa, Tour and Cruise forms exist.
- Forms are intentionally demo-only until a real backend/provider is selected.
- Do NOT put API keys, SMTP passwords, payment credentials or passport data in front-end HTML.

Recommended production flow
Website form
  -> secure form/API endpoint
  -> spam/rate-limit check
  -> lead database / CRM
  -> internal notification email
  -> customer confirmation email
  -> follow-up / quote
  -> payment only after confirmation

Required production fields
- Service
- Product / enquiry type
- Full name
- Email
- Phone / WhatsApp (optional but recommended)
- Nationality
- Travel date
- Travellers
- Message
- Consent checkbox
- Timestamp
- Source page / UTM fields

Visa document handling
- Do not accept passport scans through the basic public form.
- Use a separate authenticated/expiring secure upload mechanism when documents are required.
- Restrict access to authorised staff.
- Set retention/deletion rules before launch.

Security requirements
- HTTPS
- Server-side validation
- CAPTCHA or equivalent bot protection
- Rate limiting
- CSRF protection where applicable
- Input sanitisation
- Email-domain authentication (SPF/DKIM/DMARC)
- No secrets in client-side JavaScript
- Backups and access controls

Provider decision still required
Choose ONE production route before launch:
A. Hosted form + CRM
B. Website backend + database + email provider
C. WordPress form + CRM/email integration
D. Custom serverless form endpoint

Do not connect live forms until the business email, CRM destination and privacy/retention rules are confirmed.
