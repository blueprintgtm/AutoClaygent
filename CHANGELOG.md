# AutoClaygent Changelog

## [2026-01-20] - Auth Flow & Setup Fixes

### Fixed
- **Content API 404 errors**: Premium content endpoints (`/api/content/workflow`, `/api/content/patterns`, etc.) now correctly serve content. Previously, content files were excluded from Vercel deployment.
- **Supabase MCP package name**: Fixed incorrect npm package reference in CLAUDE.md setup instructions. Changed from `@supabase/mcp-server` (doesn't exist) to `@supabase/mcp-server-supabase@latest` (correct package).

### What you need to do
If you cloned the repo before this date:
```bash
git pull origin main
```
Then restart Claude Code to pick up the updated CLAUDE.md instructions.

---

## [2026-01-13] - Initial Release

- AutoClaygent skill for building production-ready Claygent prompts
- License-based content protection with Stripe integration
- Webhook server for local testing
- Reference documentation for Clay JSON rules, templates, and integrations
