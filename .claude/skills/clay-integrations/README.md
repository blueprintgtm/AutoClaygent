# Clay Integrations Skill

Check if Clay has native integrations for a task before building a custom Claygent.

## When to Use

Invoke this skill at the **start of any Claygent building request** to check if Clay already has a native integration that solves the user's need.

## What It Does

1. Parses the user's stated goal (e.g., "find phone numbers")
2. Searches the integrations catalog for matches
3. Shows relevant options with credit costs and BYOK availability
4. Offers 3 choices:
   - **(A) Native**: Use the native integration (with optional Claygent fallback)
   - **(B) Claygent**: Build a custom Claygent
   - **(C) Hybrid**: Native first, Claygent for gaps

## Why It Matters

Native integrations are:
- **Faster**: No web browsing required
- **Cheaper**: Especially with BYOK
- **More reliable**: Structured API responses

## Files

- `SKILL.md` - Full skill definition and workflow
- `references/integrations-catalog.md` - 150+ Clay integrations catalog

## Example

**User**: "I want to find phone numbers for my leads"

**Skill**: Shows People Data Labs (5 credits), ContactOut (10-15 credits), Datagma (15-25 credits) as options, then asks user to choose native, Claygent, or hybrid approach.
