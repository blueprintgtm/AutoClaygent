# Clay Integration Catalog

> **Baseline Date**: January 2026
> **Total Integrations**: 150+
> **Credit Range**: 0-30 credits per action

This catalog documents all Clay integrations with their categories, credit costs, BYOK availability, and common use cases.

---

## AI & LLM Providers

### OpenAI / GPT
- **Category**: AI
- **Credits**: 0 (with own key) or ~10-25 credits
- **BYOK**: Yes (requires 30,000 TPM for ChatGPT columns)
- **Actions**: Ask ChatGPT, Generate text, Summarize, Classify
- **Inputs**: Prompt, context variables from table columns
- **Outputs**: Generated text response
- **Best for**: Personalizing emails, classifying leads, extracting insights
- **Notes**: Most versatile AI integration. 8,192-token max output limit applies

### Anthropic (Claude)
- **Category**: AI
- **Credits**: 0 (with own key) or ~10-25 credits
- **BYOK**: Yes (requires Tier 4+ with 450,000 TPM)
- **Actions**: Generate text, Analyze, Summarize
- **Inputs**: Prompt, context variables
- **Outputs**: Generated text response
- **Best for**: Longer-form content, nuanced analysis
- **Notes**: Often better for complex reasoning tasks

### Google Gemini
- **Category**: AI
- **Credits**: 0 (with own key) or ~10-25 credits
- **BYOK**: Yes
- **Actions**: Generate text, Analyze content
- **Inputs**: Prompt, context
- **Outputs**: Generated text
- **Best for**: Multimodal tasks, web search-augmented responses

### Mistral
- **Category**: AI
- **Credits**: 0 (with own key) or ~10-25 credits
- **BYOK**: Yes
- **Actions**: Generate text
- **Inputs**: Prompt
- **Outputs**: Text response
- **Best for**: Fast, cost-effective text generation

### Cohere
- **Category**: AI
- **Credits**: 0 (with own key) or ~10-25 credits
- **BYOK**: Yes
- **Actions**: Chat API, Generate, Classify
- **Inputs**: Prompt, context
- **Outputs**: Text response
- **Best for**: Enterprise NLP tasks

### Perplexity AI
- **Category**: AI
- **Credits**: ~10-25 credits (Clay-managed only)
- **BYOK**: NO
- **Actions**: Web search with AI, Non-online AI model
- **Inputs**: Search query or prompt
- **Outputs**: AI-generated answer with sources
- **Best for**: Real-time web research, fact-checking
- **Notes**: Cannot use own API key

### DeepSeek
- **Category**: AI
- **Credits**: ~10-25 credits (Clay-managed only)
- **BYOK**: NO
- **Actions**: DeepSeek R1 reasoning model
- **Inputs**: Prompt
- **Outputs**: Reasoning-augmented response
- **Best for**: Complex reasoning tasks
- **Notes**: Cannot use own API key

### Claygent
- **Category**: AI
- **Credits**: ~15-25 credits (Clay-managed only)
- **BYOK**: NO
- **Actions**: AI agent that browses web, extracts data
- **Inputs**: Natural language instructions
- **Outputs**: Extracted data, summaries
- **Best for**: Complex web research tasks
- **Notes**: Clay's proprietary AI agent - cannot use own key

### Lavender
- **Category**: AI / Email
- **Credits**: ~5 credits
- **BYOK**: Yes
- **Actions**: Score email quality, Analyze subject lines
- **Inputs**: Email copy
- **Outputs**: Quality score, improvement suggestions
- **Best for**: Email optimization before sending

### Twain
- **Category**: AI / Sales
- **Credits**: ~5 credits
- **BYOK**: Yes
- **Actions**: Generate sales messages
- **Inputs**: Context, prospect info
- **Outputs**: Sales copy
- **Best for**: Attention-grabbing outreach

### MadKudu
- **Category**: AI / Intent
- **Credits**: ~5-10 credits
- **BYOK**: Yes
- **Actions**: Get intent data, Lead scoring
- **Inputs**: Email addresses
- **Outputs**: Intent signals, lead scores
- **Best for**: Prioritizing high-intent leads

---

## Company Data Providers

### Clearbit
- **Category**: Company Data
- **Credits**: 5-8 credits
- **BYOK**: Yes (0 credits with own key)
- **Actions**: Enrich Company, Enrich Person
- **Inputs**: Domain, email, company name
- **Outputs**: Employee count, industry, funding, technologies, social links
- **Best for**: Firmographic enrichment, tech stack detection
- **Waterfall position**: Often first for company enrichment

### Apollo.io
- **Category**: Company Data / People Data
- **Credits**: 1-2 credits
- **BYOK**: Yes (0 credits with own key)
- **Actions**: Find contacts, Enrich company, Enrich person, Job discovery
- **Inputs**: Domain, LinkedIn URL, name + company
- **Outputs**: Emails, phone numbers, job titles, company data
- **Best for**: Cost-effective starting point in waterfalls
- **Waterfall position**: Best first due to low cost

### ZoomInfo
- **Category**: Company Data / People Data
- **Credits**: ~10-15 credits (via HTTP API)
- **BYOK**: Yes (requires HTTP API setup)
- **Actions**: Enrich company, Find contacts
- **Inputs**: Domain, company name
- **Outputs**: Company details, contact information
- **Best for**: Enterprise-grade data quality
- **Notes**: Not native integration - requires HTTP API workaround

### Crunchbase
- **Category**: Company Data
- **Credits**: ~5 credits
- **BYOK**: Yes
- **Actions**: Enrich company
- **Inputs**: Domain, company name
- **Outputs**: Funding rounds, investors, growth metrics, news
- **Best for**: Funding intelligence, investor research

### BuiltWith
- **Category**: Company Data / Technographics
- **Credits**: ~5-8 credits
- **BYOK**: Yes
- **Actions**: Tech stack lookup
- **Inputs**: Domain
- **Outputs**: Technologies used, categories, install dates
- **Best for**: Selling to specific tech stacks

### HG Insights
- **Category**: Company Data / Technographics
- **Credits**: ~8-10 credits
- **BYOK**: Yes
- **Actions**: Enrich company, Tech stack data
- **Inputs**: Domain
- **Outputs**: Enterprise tech stack, IT spend estimates
- **Best for**: Enterprise technology intelligence

### Owler
- **Category**: Company Data
- **Credits**: ~3-5 credits
- **BYOK**: Yes
- **Actions**: Company lookup, Competitor analysis
- **Inputs**: Domain
- **Outputs**: Company updates, competitors, news
- **Best for**: Competitive intelligence

### Pitchbook
- **Category**: Company Data
- **Credits**: ~8-10 credits
- **BYOK**: Yes
- **Actions**: Enrich company
- **Inputs**: Domain
- **Outputs**: Funding, valuations, investors
- **Best for**: VC/PE research, investment data

### Harmonic.ai
- **Category**: Company Data
- **Credits**: ~5-8 credits
- **BYOK**: Yes
- **Actions**: Fundraising data, Company enrichment
- **Inputs**: Domain, company name
- **Outputs**: Fundraising rounds, company signals
- **Best for**: Early-stage startup intelligence

### Dealroom.co
- **Category**: Company Data
- **Credits**: ~5-8 credits
- **BYOK**: Yes
- **Actions**: Company enrichment
- **Inputs**: Domain
- **Outputs**: Funding data, startup profiles
- **Best for**: European startup data

### Semrush
- **Category**: Company Data / Traffic
- **Credits**: ~3-5 credits
- **BYOK**: Yes
- **Actions**: Traffic analytics
- **Inputs**: Domain
- **Outputs**: Monthly traffic, traffic sources
- **Best for**: Qualifying companies by web presence

### Similarweb
- **Category**: Company Data / Traffic
- **Credits**: ~5-8 credits
- **BYOK**: Yes
- **Actions**: Engagement metrics, Technology detection
- **Inputs**: Domain
- **Outputs**: Traffic rank, engagement, tech stack
- **Best for**: Competitive analysis, website performance

### Ocean.io
- **Category**: Company Data
- **Credits**: ~3-5 credits
- **BYOK**: Yes
- **Actions**: Find similar companies
- **Inputs**: Company domain
- **Outputs**: Similar companies, lookalike accounts
- **Best for**: Account expansion, lookalike modeling

### Store Leads
- **Category**: Company Data / E-commerce
- **Credits**: ~3-5 credits
- **BYOK**: Yes
- **Actions**: Find companies by domain, keyword, technology
- **Inputs**: Domain, keywords, platform
- **Outputs**: Company data, e-commerce platform details
- **Best for**: E-commerce lead generation

### HitHorizons
- **Category**: Company Data
- **Credits**: ~3-5 credits
- **BYOK**: Yes
- **Actions**: Company lookup
- **Inputs**: Domain
- **Outputs**: Firmographic data (Europe/UK focus)
- **Best for**: European company intelligence

### Crossbeam
- **Category**: Company Data
- **Credits**: ~5 credits
- **BYOK**: Yes
- **Actions**: Import EQLs, Enrich with partner data
- **Inputs**: Account identifiers
- **Outputs**: Partner overlap data, firmographic enrichment
- **Best for**: Partner ecosystem intelligence

### The Swarm
- **Category**: Company Data / Relationships
- **Credits**: ~5-8 credits
- **BYOK**: Yes
- **Actions**: Relationship scoring
- **Inputs**: Target person/company
- **Outputs**: Relationship paths, connection scores
- **Best for**: Warm intro paths, network intelligence

---

## Contact Data / Email Finders

### Hunter.io
- **Category**: Contact Data
- **Credits**: 1-2 credits
- **BYOK**: Yes (0 credits with own key)
- **Actions**: Find email, Verify email, Domain search
- **Inputs**: Name + domain, or email
- **Outputs**: Work email, verification status
- **Best for**: Cheapest email finder in waterfalls
- **Waterfall position**: First due to lowest cost
- **Hit rate**: ~60-70%

### Prospeo
- **Category**: Contact Data
- **Credits**: 2-3 credits
- **BYOK**: Yes
- **Actions**: Find work email, Enrich person
- **Inputs**: Name + domain, LinkedIn URL
- **Outputs**: Work email, person details
- **Best for**: Second position in email waterfalls

### Findymail
- **Category**: Contact Data
- **Credits**: 2-3 credits
- **BYOK**: Yes
- **Actions**: Find email, Scrape, Clean emails
- **Inputs**: Name + domain, LinkedIn URL
- **Outputs**: Work email (verified)
- **Best for**: B2B email prospecting

### Dropcontact
- **Category**: Contact Data
- **Credits**: 2-3 credits
- **BYOK**: Yes
- **Actions**: Find work email, Company enrichment
- **Inputs**: Name + domain
- **Outputs**: Work email, company name
- **Best for**: European focus, GDPR-compliant

### Enrow
- **Category**: Contact Data
- **Credits**: 2-3 credits
- **BYOK**: Yes
- **Actions**: Find email, Verify email
- **Inputs**: Name + domain
- **Outputs**: Verified work email
- **Best for**: Mid-tier email finding

### Icypeas
- **Category**: Contact Data
- **Credits**: 2-3 credits
- **BYOK**: Yes
- **Actions**: Find work email, Profile discovery
- **Inputs**: Name + domain
- **Outputs**: Work email, professional profiles
- **Best for**: European prospecting

### Snov.io
- **Category**: Contact Data
- **Credits**: 2-3 credits
- **BYOK**: Yes
- **Actions**: Find email, Verify, Domain search
- **Inputs**: Name + domain, domain
- **Outputs**: Work emails
- **Best for**: Bulk email finding

### BetterContact
- **Category**: Contact Data
- **Credits**: 3-5 credits
- **BYOK**: Yes
- **Actions**: Find work email, Find mobile
- **Inputs**: Name + company, LinkedIn URL
- **Outputs**: Work email, mobile number
- **Best for**: Combination email + phone

### FullEnrich
- **Category**: Contact Data
- **Credits**: 5-8 credits
- **BYOK**: Yes
- **Actions**: Find phone, Find work email
- **Inputs**: Social profile URL
- **Outputs**: Phone numbers, work email
- **Best for**: Mobile number discovery

### Wiza
- **Category**: Contact Data
- **Credits**: 3-5 credits
- **BYOK**: Yes
- **Actions**: Find verified emails, Find phone
- **Inputs**: LinkedIn URL, name + company
- **Outputs**: Verified email, phone
- **Best for**: LinkedIn-based prospecting

### ContactOut
- **Category**: Contact Data
- **Credits**: 10-15 credits
- **BYOK**: Yes
- **Actions**: Find mobile, Find personal email
- **Inputs**: LinkedIn URL
- **Outputs**: Mobile numbers, personal emails
- **Best for**: Mobile number fallback
- **Waterfall position**: Late due to higher cost

### Datagma
- **Category**: Contact Data
- **Credits**: 15-25 credits
- **BYOK**: Yes
- **Actions**: Find contact info, Phone enrichment
- **Inputs**: Name + company, LinkedIn URL
- **Outputs**: Email, phone, full profile
- **Best for**: Premium phone number discovery
- **Waterfall position**: Final fallback

### SignalHire
- **Category**: Contact Data
- **Credits**: 5-10 credits
- **BYOK**: Yes
- **Actions**: Find candidates
- **Inputs**: LinkedIn URL, Email, Phone
- **Outputs**: Contact details, profile data
- **Best for**: Recruiting, candidate outreach

### LeadMagic
- **Category**: Contact Data
- **Credits**: 3-5 credits
- **BYOK**: Yes
- **Actions**: Find work email, Find mobile
- **Inputs**: Name + company
- **Outputs**: Email, mobile, company data
- **Best for**: Multi-purpose contact finding

### Nimbler
- **Category**: Contact Data
- **Credits**: 3-5 credits
- **BYOK**: Yes
- **Actions**: Find email
- **Inputs**: Name + company
- **Outputs**: Work email
- **Best for**: Email discovery

### Forager
- **Category**: Contact Data
- **Credits**: 5-10 credits
- **BYOK**: Yes
- **Actions**: Find phone from social
- **Inputs**: Social profile URL
- **Outputs**: Phone numbers
- **Best for**: Phone number discovery

### Upcell
- **Category**: Contact Data
- **Credits**: 5-10 credits
- **BYOK**: Yes
- **Actions**: Find mobile from LinkedIn
- **Inputs**: LinkedIn URL
- **Outputs**: Mobile number
- **Best for**: Mobile discovery

### Mixrank
- **Category**: Contact Data
- **Credits**: 5-8 credits
- **BYOK**: Yes
- **Actions**: Enrich from email, Find email from social
- **Inputs**: Email, social profile
- **Outputs**: Contact details
- **Best for**: Cross-platform contact matching

### RocketReach
- **Category**: Contact Data
- **Credits**: 5-8 credits
- **BYOK**: Yes
- **Actions**: Enrich contact, Enrich company
- **Inputs**: Name + company, domain
- **Outputs**: Email, phone, company data
- **Best for**: Comprehensive contact enrichment

### LeadIQ
- **Category**: Contact Data
- **Credits**: 3-5 credits
- **BYOK**: Yes
- **Actions**: Enrich individual, Enrich company
- **Inputs**: LinkedIn URL, domain
- **Outputs**: Contact data, company info
- **Best for**: Sales intelligence

### People Data Labs
- **Category**: Contact Data / People Data
- **Credits**: 5 credits (phone)
- **BYOK**: Yes (0 credits with own key)
- **Actions**: Enrich person, Find mobile, Generate lists
- **Inputs**: Email, LinkedIn URL, name + company
- **Outputs**: Full profile, mobile number
- **Best for**: Cost-effective mobile numbers
- **Waterfall position**: Often first for mobile

### Swordfish
- **Category**: Contact Data
- **Credits**: 10-15 credits
- **BYOK**: Yes
- **Actions**: AI-powered enrichment
- **Inputs**: Name + company, LinkedIn URL
- **Outputs**: Contact details
- **Best for**: Premium contact data

### SMARTe
- **Category**: Contact Data
- **Credits**: 25-30 credits
- **BYOK**: Yes
- **Actions**: Find phone
- **Inputs**: Name + company
- **Outputs**: Mobile number
- **Best for**: High-value phone discovery
- **Waterfall position**: Final fallback due to high cost

---

## Email Verification

### NeverBounce
- **Category**: Contact Verification
- **Credits**: 1 credit
- **BYOK**: Yes
- **Actions**: Validate email
- **Inputs**: Email address
- **Outputs**: Validation status (valid/invalid/risky)
- **Best for**: Pre-send verification

### ZeroBounce
- **Category**: Contact Verification
- **Credits**: 1 credit
- **BYOK**: Yes
- **Actions**: Validate email, Find work email
- **Inputs**: Email, name + domain
- **Outputs**: Validation status, work email
- **Best for**: Combined finding + verification

### Debounce
- **Category**: Contact Verification
- **Credits**: 1 credit
- **BYOK**: Yes
- **Actions**: Validate email
- **Inputs**: Email address
- **Outputs**: Validation result
- **Best for**: Bulk email cleaning

### Trestle
- **Category**: Contact Verification
- **Credits**: 2-3 credits
- **BYOK**: Yes
- **Actions**: Verify phone, Name matching
- **Inputs**: Phone number, name
- **Outputs**: Verification status, contact grade
- **Best for**: Phone number verification

### SureConnect
- **Category**: Contact Verification
- **Credits**: ~3 credits
- **BYOK**: Yes
- **Actions**: Identify "likely to answer" contacts
- **Inputs**: Phone number
- **Outputs**: Contactability score
- **Best for**: Call prioritization

---

## CRM Integrations

### HubSpot
- **Category**: CRMs
- **Credits**: 0 credits (with own key)
- **BYOK**: Yes (required)
- **Actions**: Create contact, Update contact, Create company, Lookup, Add to list
- **Inputs**: Contact/company data
- **Outputs**: CRM record IDs, lookup results
- **Best for**: Syncing enriched data to CRM

### Salesforce
- **Category**: CRMs
- **Credits**: 0 credits (with own key)
- **BYOK**: Yes (required)
- **Actions**: Create/update leads, contacts, accounts, opportunities
- **Inputs**: Record data
- **Outputs**: Record IDs
- **Best for**: Enterprise CRM sync

### Pipedrive
- **Category**: CRMs
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Create/update people, organizations
- **Inputs**: Contact/company data
- **Outputs**: Record IDs
- **Best for**: SMB sales teams

### Close
- **Category**: CRMs
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Manage leads, contacts, sequences
- **Inputs**: Lead data
- **Outputs**: Record IDs
- **Best for**: Inside sales teams

### ActiveCampaign
- **Category**: CRMs
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Create/update contacts, Add to automations
- **Inputs**: Contact data
- **Outputs**: Record IDs
- **Best for**: Marketing automation integration

### Dynamics 365
- **Category**: CRMs
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Create/update/lookup records
- **Inputs**: Entity data
- **Outputs**: Record IDs
- **Best for**: Microsoft ecosystem

---

## Sales Engagement / Sequencers

### Outreach
- **Category**: Marketing & Outreach
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Create contacts, Add to sequences
- **Inputs**: Contact data, sequence ID
- **Outputs**: Prospect IDs
- **Best for**: Enterprise outbound

### Salesloft
- **Category**: Marketing & Outreach
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Manage accounts/people, Add to cadences
- **Inputs**: Contact data
- **Outputs**: Record IDs
- **Best for**: Enterprise sales engagement

### Instantly
- **Category**: Marketing & Outreach
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Add leads to campaigns
- **Inputs**: Email, campaign ID
- **Outputs**: Lead IDs
- **Best for**: Cold email at scale

### Smartlead.ai
- **Category**: Marketing & Outreach
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Create/manage leads, campaigns
- **Inputs**: Lead data
- **Outputs**: Campaign status
- **Best for**: Agency cold email

### Lemlist
- **Category**: Marketing & Outreach
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Add leads to campaigns
- **Inputs**: Lead data, campaign ID
- **Outputs**: Lead status
- **Best for**: Personalized cold email

### Reply.io
- **Category**: Marketing & Outreach
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Create contacts, Push to campaigns
- **Inputs**: Contact data
- **Outputs**: Contact IDs
- **Best for**: Multi-channel sequences

### HeyReach
- **Category**: Marketing & Outreach
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Add to LinkedIn campaigns
- **Inputs**: LinkedIn URLs
- **Outputs**: Campaign status
- **Best for**: LinkedIn outreach automation

### Gong Engage
- **Category**: Marketing & Outreach
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Push contacts to Gong Engage Flows
- **Inputs**: Contact data
- **Outputs**: Flow enrollment
- **Best for**: Revenue intelligence + engagement

---

## Databases & Spreadsheets

### Google Sheets
- **Category**: Databases
- **Credits**: 0 credits
- **BYOK**: Yes (OAuth)
- **Actions**: Lookup, Add rows, Update rows, Upload data
- **Inputs**: Sheet ID, row data
- **Outputs**: Row data
- **Best for**: Lightweight data sync

### Airtable
- **Category**: Databases
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Create/update/upsert records, Pull data
- **Inputs**: Base/table IDs, record data
- **Outputs**: Record IDs
- **Best for**: Flexible database operations

### Notion
- **Category**: Databases
- **Credits**: 0 credits
- **BYOK**: Yes (OAuth)
- **Actions**: Create/update database items
- **Inputs**: Database ID, properties
- **Outputs**: Page IDs
- **Best for**: Knowledge management integration

### Snowflake
- **Category**: Databases
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Insert/update/upsert/lookup rows
- **Inputs**: Query, row data
- **Outputs**: Query results
- **Best for**: Data warehouse sync

### Postgres
- **Category**: Databases
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Lookup rows
- **Inputs**: Query
- **Outputs**: Row data
- **Best for**: Custom database lookups

### Coda
- **Category**: Databases
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Check/create/update rows
- **Inputs**: Doc ID, table, row data
- **Outputs**: Row IDs
- **Best for**: Doc-based workflows

---

## Web Scraping & Data Collection

### ZenRows
- **Category**: Web Scraping
- **Credits**: ~3-5 credits
- **BYOK**: Yes
- **Actions**: Scrape webpage
- **Inputs**: URL
- **Outputs**: Page HTML/content
- **Best for**: Anti-bot scraping

### Bright Data
- **Category**: Web Scraping
- **Credits**: ~5-10 credits
- **BYOK**: Yes
- **Actions**: Data Collector, Web Unlocker
- **Inputs**: URL, data type
- **Outputs**: Structured data
- **Best for**: Enterprise scraping at scale

### Apify
- **Category**: Web Scraping
- **Credits**: ~5-10 credits
- **BYOK**: Yes
- **Actions**: Run actors, Scrape websites
- **Inputs**: Actor ID, inputs
- **Outputs**: Scraped data
- **Best for**: Pre-built scrapers for common sites

### PhantomBuster
- **Category**: Web Scraping
- **Credits**: ~5-10 credits
- **BYOK**: Yes
- **Actions**: Run phantoms, Extract data
- **Inputs**: Phantom ID, inputs
- **Outputs**: Extracted data
- **Best for**: Social media scraping

### ScrapeMagic
- **Category**: Web Scraping
- **Credits**: ~3-5 credits
- **BYOK**: Yes
- **Actions**: Scrape pages
- **Inputs**: URL
- **Outputs**: Page content
- **Best for**: Simple web scraping

---

## Social Media & News

### LinkedIn Community
- **Category**: Social Media
- **Credits**: ~5-10 credits
- **Actions**: Engagement insights, Audience analysis
- **Inputs**: Profile URL, content URL
- **Outputs**: Engagement data
- **Best for**: LinkedIn content strategy

### Hacker News
- **Category**: Social Media / News
- **Credits**: ~1 credit
- **Actions**: Get user details, Post details
- **Inputs**: Username, post URL
- **Outputs**: Profile data, post content
- **Best for**: Tech community targeting

### LiveData
- **Category**: Social Media
- **Credits**: ~3-5 credits
- **BYOK**: Yes
- **Actions**: Find social profile from email/name
- **Inputs**: Work email, name
- **Outputs**: Social profile URLs
- **Best for**: Social discovery

---

## Google Services

### Google Search
- **Category**: Google
- **Credits**: ~1-2 credits
- **Actions**: Search jobs, businesses, reviews, web
- **Inputs**: Search query
- **Outputs**: Search results
- **Best for**: Custom web research

### Google Maps
- **Category**: Google / Location
- **Credits**: ~1-2 credits
- **Actions**: Find businesses, Get reviews, Business info
- **Inputs**: Location, business type
- **Outputs**: Business listings, reviews
- **Best for**: Local business prospecting

### Google Shopping
- **Category**: Google / E-commerce
- **Credits**: ~1 credit
- **Actions**: Product search
- **Inputs**: Product query
- **Outputs**: Shopping results
- **Best for**: E-commerce research

### Google PageSpeed
- **Category**: Google / Analytics
- **Credits**: ~1 credit
- **Actions**: Performance analysis
- **Inputs**: URL
- **Outputs**: Performance scores, recommendations
- **Best for**: Website quality scoring

---

## Intent Data

### TrustRadius
- **Category**: Intent Data
- **Credits**: ~5-10 credits
- **BYOK**: Yes
- **Actions**: Get intent signals
- **Inputs**: Domain, category
- **Outputs**: Intent signals, review data
- **Best for**: Software buying intent

### Trigify
- **Category**: Intent Data
- **Credits**: ~5-10 credits
- **BYOK**: Yes
- **Actions**: Search engaged prospects
- **Inputs**: Content topics, social content
- **Outputs**: Engaged prospects
- **Best for**: Social intent signals

### Demandbase
- **Category**: Intent Data
- **Credits**: ~10-15 credits
- **BYOK**: Yes
- **Actions**: Account intent, Engagement data
- **Inputs**: Domain
- **Outputs**: Intent scores, engagement signals
- **Best for**: Enterprise ABM intent

---

## Communication Tools

### Slack
- **Category**: Communication
- **Credits**: 0 credits
- **BYOK**: Yes (OAuth)
- **Actions**: Send messages, Get member lists, Post notifications
- **Inputs**: Channel ID, message
- **Outputs**: Message IDs
- **Best for**: Team notifications, alerts

### Intercom
- **Category**: Communication
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Create/update contacts
- **Inputs**: Contact data
- **Outputs**: Contact IDs
- **Best for**: Customer communication sync

### Customer.io
- **Category**: Communication
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Add/update customer data
- **Inputs**: Customer data
- **Outputs**: Customer IDs
- **Best for**: Marketing automation

### Typeform
- **Category**: Communication
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Retrieve responses, Search responses
- **Inputs**: Form ID
- **Outputs**: Response data
- **Best for**: Form response processing

---

## Video & Content Creation

### HeyGen
- **Category**: AI / Video
- **Credits**: ~10-20 credits
- **BYOK**: Yes
- **Actions**: Generate avatar videos
- **Inputs**: Script, avatar settings
- **Outputs**: Video URL
- **Best for**: Personalized video outreach

### Captions
- **Category**: AI / Video
- **Credits**: ~10-20 credits
- **BYOK**: Yes
- **Actions**: Generate talking videos with AI
- **Inputs**: Script, avatar
- **Outputs**: Video URL
- **Best for**: AI-generated videos

### Sendspark
- **Category**: Video / Outreach
- **Credits**: ~5-10 credits
- **BYOK**: Yes
- **Actions**: Add to video campaign, Dynamic video
- **Inputs**: Prospect data, campaign ID
- **Outputs**: Personalized video URL
- **Best for**: Video prospecting

### Loom
- **Category**: Video
- **Credits**: ~1-2 credits
- **BYOK**: Yes
- **Actions**: Transcribe videos
- **Inputs**: Video URL
- **Outputs**: Transcript
- **Best for**: Video content processing

### Tavus
- **Category**: Video
- **Credits**: ~10-20 credits
- **BYOK**: Yes
- **Actions**: Generate personalized videos
- **Inputs**: Template, variables
- **Outputs**: Video URL
- **Best for**: AI-personalized video at scale

---

## Translation

### DeepL
- **Category**: Translation
- **Credits**: ~1-2 credits
- **BYOK**: Yes
- **Actions**: Translate text
- **Inputs**: Text, target language
- **Outputs**: Translated text
- **Best for**: High-quality translation

### Google Translate
- **Category**: Translation
- **Credits**: ~1 credit
- **BYOK**: Yes
- **Actions**: Translate text
- **Inputs**: Text, target language
- **Outputs**: Translated text
- **Best for**: Quick translation

---

## Influencer & Creator Data

### Modash
- **Category**: Influencer
- **Credits**: ~5-10 credits
- **BYOK**: Yes
- **Actions**: Enrich social media influencers
- **Inputs**: Social profile URL
- **Outputs**: Follower counts, engagement metrics
- **Best for**: Influencer marketing

### Upfluence
- **Category**: Influencer
- **Credits**: ~5-10 credits
- **BYOK**: Yes
- **Actions**: Find creators by keywords/location
- **Inputs**: Keywords, location
- **Outputs**: Creator profiles, contact info
- **Best for**: Creator discovery

### Influencer Club
- **Category**: Influencer
- **Credits**: ~5-10 credits
- **BYOK**: Yes
- **Actions**: Get creator contact details
- **Inputs**: Creator profile
- **Outputs**: Direct contact information
- **Best for**: Creator outreach

---

## Developer Tools

### GitHub
- **Category**: Developer
- **Credits**: 0 credits
- **BYOK**: Yes (OAuth)
- **Actions**: Repository lookup
- **Inputs**: Repo URL, username
- **Outputs**: Repo data, user data
- **Best for**: Developer targeting

### Linear
- **Category**: Developer
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Issue tracking
- **Inputs**: Project ID
- **Outputs**: Issue data
- **Best for**: Engineering workflows

---

## Utilities

### Bitly
- **Category**: Utilities
- **Credits**: 0 credits
- **BYOK**: Yes
- **Actions**: Shorten URLs, Track clicks
- **Inputs**: Long URL
- **Outputs**: Short URL
- **Best for**: Link tracking

### Mapbox
- **Category**: Location
- **Credits**: ~1 credit
- **BYOK**: Yes
- **Actions**: Calculate distances, Normalize geo data
- **Inputs**: Addresses, coordinates
- **Outputs**: Distance, duration, normalized address
- **Best for**: Territory planning, logistics

### APIVoid
- **Category**: Utilities
- **Credits**: ~1-2 credits
- **BYOK**: Yes
- **Actions**: Domain/email validation
- **Inputs**: Domain, email
- **Outputs**: Validation results
- **Best for**: Data quality checks

---

## Recently Added (Late 2025)

### Sumble Technographics
- **Category**: Company Data
- **Credits**: ~5 credits
- **Actions**: Tech stack analysis

### Email Bison
- **Category**: Contact Data
- **Credits**: ~2-3 credits
- **Actions**: Email discovery

### Listmint
- **Category**: Contact Data
- **Credits**: ~3-5 credits
- **Actions**: List building

### Microsoft Teams
- **Category**: Communication
- **Credits**: 0 credits
- **BYOK**: Yes (OAuth)
- **Actions**: Send messages

---

## Integration Count by Category

| Category | Count |
|----------|-------|
| Company Data | 25+ |
| Contact Data / Email Finders | 25+ |
| AI & LLM | 12+ |
| CRMs | 6 |
| Sales Engagement | 10+ |
| Email Verification | 5 |
| Databases | 6 |
| Web Scraping | 5 |
| Social Media | 8 |
| Intent Data | 4 |
| Communication | 6 |
| Video/Content | 5 |
| Google Services | 5 |
| Influencer | 3 |
| Developer | 3 |
| Translation | 2 |
| **TOTAL** | **150+** |
