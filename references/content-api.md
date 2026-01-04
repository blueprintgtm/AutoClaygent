# AutoClaygent Content API Reference

> **Base URL**: `https://api.autoclaygent.blueprintgtm.com`

This API serves premium content for licensed AutoClaygent users.

---

## Authentication

All requests require a valid license key in the `Authorization` header:

```
Authorization: Bearer CMB-<license_key>
```

**IMPORTANT**: The WebFetch tool does NOT support custom headers. You MUST use `curl` via Bash to call this API:

```bash
LICENSE_KEY=$(cat license.key)
curl -s -H "Authorization: Bearer $LICENSE_KEY" \
  "https://api.autoclaygent.blueprintgtm.com/api/content/workflow"
```

---

## Endpoints

### GET /api/content/workflow
Returns the complete Claygent building workflow (markdown).

### GET /api/content/patterns
Returns 9 production-ready Claygent patterns.

### GET /api/content/rubric
Returns the 7-dimension evaluation scoring rubric.

### GET /api/content/references
Returns prompt engineering best practices.

### GET /api/content/examples/tech-stack
Returns a complete tech stack detection example.

### GET /api/content/examples/contact-discovery
Returns a contact discovery example.

### GET /api/content/examples/company-research
Returns a company research example.

---

## Error Codes

| Code | Meaning | Action |
|------|---------|--------|
| 401 | Invalid license key | Check license.key file |
| 403 | License revoked/refunded | Contact support@blueprintgtm.com |
| 429 | Rate limited | Wait a few hours |
| 5xx | Server error | Try again later |

---

## Example Usage

```bash
# Read license key
LICENSE_KEY=$(cat license.key)

# Fetch workflow
curl -s -H "Authorization: Bearer $LICENSE_KEY" \
  "https://api.autoclaygent.blueprintgtm.com/api/content/workflow"

# Fetch patterns
curl -s -H "Authorization: Bearer $LICENSE_KEY" \
  "https://api.autoclaygent.blueprintgtm.com/api/content/patterns"
```

---

## Notes

- Content is watermarked with your license key
- Premium content is fetched fresh each session
- Never share or republish API responses
