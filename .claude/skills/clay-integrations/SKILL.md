---
name: clay-integrations
description: Check if Clay has native integrations for a data enrichment task before building a custom Claygent. Invoke at the start of any Claygent building request to suggest faster, cheaper native options.
allowed-tools: Read
---

# Clay Native Integrations Check

Before building a custom Claygent, check if Clay already has a native integration that solves the user's need. Native integrations are typically faster, cheaper, and more reliable than custom Claygents.

---

## When to Invoke This Skill

Invoke this skill **immediately** when a user describes what they want to build, BEFORE starting Discovery phase. Examples:

- "I want to find phone numbers for my leads"
- "Can you build something to get emails?"
- "I need to enrich company data"
- "Help me find funding information"

---

## Workflow

### Step 1: Parse the User's Goal

Identify the core data need from what the user said:

| Data Category | Keywords to Look For |
|---------------|---------------------|
| **Phone numbers** | phone, mobile, cell, direct dial, contact number |
| **Emails** | email, work email, personal email, contact email |
| **Email verification** | verify, validate, check email, deliverability |
| **Company data** | firmographics, employee count, company size, industry, revenue |
| **Funding data** | funding, investors, raised, series, valuation |
| **Tech stack** | technologies, tech stack, tools, software, platforms |
| **Traffic data** | website traffic, visitors, pageviews |
| **Intent data** | intent, buying signals, engagement |
| **Decision makers** | decision makers, contacts at company, who works at |

### Step 2: Search the Integrations Catalog

Read `references/clay-integrations.md` (at the repo root) and find integrations that match:
- The data type the user needs
- The input data they have (domain, email, LinkedIn URL, name+company)

### Step 3: Quick Reference Table

Use this table to quickly identify relevant integrations:

| User's Goal | Top Native Integrations |
|-------------|------------------------|
| Find phone numbers | People Data Labs (5 credits, BYOK), ContactOut (10-15 credits), Datagma (15-25 credits), BetterContact (3-5 credits) |
| Find mobile numbers | People Data Labs (5 credits, BYOK), ContactOut (10-15 credits), SMARTe (25-30 credits), Upcell (5-10 credits) |
| Find work emails | Hunter.io (1-2 credits, BYOK), Apollo (1-2 credits, BYOK), Prospeo (2-3 credits), Findymail (2-3 credits) |
| Find personal emails | ContactOut (10-15 credits), RocketReach (5-8 credits) |
| Verify emails | NeverBounce (1 credit), ZeroBounce (1 credit), Debounce (1 credit) |
| Verify phone | Trestle (2-3 credits), SureConnect (3 credits) |
| Get tech stack | BuiltWith (5-8 credits, BYOK), HG Insights (8-10 credits), Clearbit (5-8 credits) |
| Get funding data | Crunchbase (5 credits, BYOK), Pitchbook (8-10 credits), Harmonic.ai (5-8 credits) |
| Get company data | Clearbit (5-8 credits, BYOK), Apollo (1-2 credits, BYOK), ZoomInfo (10-15 credits) |
| Get website traffic | Semrush (3-5 credits), Similarweb (5-8 credits) |
| Find similar companies | Ocean.io (3-5 credits) |
| Get intent signals | TrustRadius (5-10 credits), Demandbase (10-15 credits), Trigify (5-10 credits) |

### Step 4: Show Relevant Options (If Matches Found)

If you find 1+ matching native integrations, show this output:

```
================================================================================
                     WAIT — CLAY MIGHT ALREADY DO THIS
================================================================================

   Before we build a custom Claygent, let me check...

   You want to: [user's goal in plain language]

   Clay has native integrations for this:

   ┌─────────────────────────────────────────────────────────────────────────┐
   │  OPTION 1: [Integration Name]                                          │
   │  Credits: X credits | BYOK: Yes/No                                     │
   │  Best for: [use case from catalog]                                     │
   ├─────────────────────────────────────────────────────────────────────────┤
   │  OPTION 2: [Integration Name]                                          │
   │  Credits: X credits | BYOK: Yes/No                                     │
   │  Best for: [use case from catalog]                                     │
   └─────────────────────────────────────────────────────────────────────────┘

   Native integrations are:
   ✓ Faster (no web browsing)
   ✓ More reliable (structured APIs)
   ✓ Often cheaper (especially with BYOK)

================================================================================

What would you like to do?
━━━━━━━━━━━━━━━━━━━━━━━━━━
(A) Use native integration → I'll show you how to set it up
(B) Build custom Claygent → For cases natives can't handle
(C) Hybrid approach → Use native first, Claygent as fallback

```

### Step 5: Handle User's Choice

#### Choice (A): Native Integration

Show full setup instructions:

```
================================================================================
                    SETTING UP [INTEGRATION NAME]
================================================================================

STEP 1: Add the Column
----------------------
In your Clay table:
  1. Click "+" to add a new column
  2. Select "Enrich data" (or "Find data" for contact finders)
  3. Find "[Integration Name]" in the list
  4. Select the action: [specific action from catalog]

STEP 2: Configure Inputs
------------------------
Map your columns:
  - [Input field] → Your [column name] column

STEP 3: BYOK (Optional - Save Credits)
--------------------------------------
[If BYOK=Yes]:
  This integration supports Bring Your Own Key.
  Go to Settings → Integrations → [Integration] → Add your API key

  With BYOK: 0 credits per row
  Without: ~X credits per row

[If BYOK=No]:
  This integration doesn't support BYOK. Clay manages the API.
  Cost: ~X credits per row

STEP 4: Run It
--------------
  1. Select a few test rows
  2. Right-click → "Run selected rows"
  3. Verify results look correct
  4. Run on full dataset

================================================================================
```

**After setup instructions, ALWAYS offer the fallback option:**

```
================================================================================

   Native integration is set up!

   Want me to also build a Claygent fallback for cases where
   [Integration Name] doesn't find a result?

   (A) Yes, build a fallback Claygent
   (B) No, the native integration is enough

================================================================================
```

- If user says (A) → Return "PROCEED_TO_DISCOVERY" with fallback context
- If user says (B) → Return "COMPLETE" - session ends successfully

#### Choice (B): Custom Claygent

Show acknowledgment and proceed:

```
   Got it! Building a custom Claygent.

   Native integrations are great for standard lookups, but they can't:
   - Synthesize information from multiple pages
   - Apply custom logic or rules
   - Handle edge cases gracefully
   - Extract data from non-standard sources

   That's where Claygents shine. Let's build yours.
```

Return "PROCEED_TO_DISCOVERY" - continue to Discovery phase.

#### Choice (C): Hybrid Approach

Show waterfall strategy:

```
================================================================================
                        HYBRID WATERFALL STRATEGY
================================================================================

   Smart thinking! Here's the play:

   1. FIRST: Use native integration (fast, cheap, reliable)
      → Add [Integration] column
      → Run on all rows

   2. THEN: Build a Claygent for failures/gaps
      → Filter to rows where [Integration] returned null
      → Run Claygent only on those

   This gives you:
   ✓ Speed from native APIs
   ✓ Fallback coverage from Claygent
   ✓ Lower cost (Claygent only runs when needed)

   Let's start with the native integration setup, then build the fallback.

================================================================================
```

Show native setup first (same as Choice A), then automatically proceed to Discovery for the Claygent fallback.

### Step 6: Skip When No Match

If the user's request doesn't match any native integration, **skip this skill entirely** and proceed directly to Discovery:

**Examples that should SKIP the check:**
- "Determine if company is B2B based on pricing page"
- "Find the CEO's communication style from blog posts"
- "Analyze job postings for hiring patterns"
- "Extract custom data from About Us pages"
- "Score companies based on my specific criteria"

For these, simply say:

```
   That's exactly what Claygents are for — custom logic that APIs can't handle.
   Let me understand your requirements...
```

And return "PROCEED_TO_DISCOVERY" immediately.

---

## Return Values

This skill returns one of:

| Return Value | Meaning |
|--------------|---------|
| `PROCEED_TO_DISCOVERY` | Continue to Discovery phase (user chose B, C, or A+fallback) |
| `COMPLETE` | Session complete (user chose A and declined fallback) |

---

## Reference File

The full integrations catalog is at: `references/clay-integrations.md` (at the repo root).

This contains 150+ Clay integrations with:
- Credit costs (Clay-managed vs BYOK)
- BYOK availability
- Input/output fields
- Best-for descriptions
- Waterfall position recommendations
