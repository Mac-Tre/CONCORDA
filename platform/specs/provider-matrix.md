# Provider Integration Matrix (Baseline)

## Google
- Identity: Google OAuth 2.0 / OIDC
- Core APIs: Calendar, Drive, Gmail (optional), Meet metadata (optional)
- Typical use: shared scheduling, reminders, secure document import

## Microsoft
- Identity: Microsoft Entra ID OAuth / OIDC
- Core APIs: Microsoft Graph (Calendar, OneDrive, Outlook, Teams metadata)
- Typical use: enterprise identity + schedule coordination

## Apple
- Identity: Sign in with Apple
- Core APIs: iCloud/CloudKit (where supported), device-native sharing hooks
- Typical use: Apple-first auth and mobile sync paths

## Adobe
- Identity: Adobe IMS OAuth
- Core APIs: Adobe PDF Services, Adobe Express workflows (if enabled)
- Typical use: guided report exports and document transformations

## OpenAI
- Identity: API key or service principal
- Core APIs: responses/reasoning, tool calling, embeddings, safety classifiers (as available)
- Typical use: Corda inference, coaching generation, classification, summarization

## Extensible Third Parties
- Slack, Zoom, Notion, Dropbox, etc. can be onboarded through the same provider connection schema.

## Security Baselines
- Encrypt provider tokens at rest.
- Keep refresh token rotation metadata.
- Allow instant revoke per provider and per tenant.
- Record scope grant timestamps for audit and compliance.

