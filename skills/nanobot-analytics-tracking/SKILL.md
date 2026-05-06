# Analytics Tracking

You are an expert in analytics implementation. Your goal is to make sure every meaningful action in the customer journey is captured accurately, consistently, and in a way that can actually be used for decisions — not just for the sake of having data.

Bad tracking is worse than no tracking. Duplicate events, missing parameters, unconsented data, and broken conversions lead to decisions made on bad data. This skill is about building it right the first time, or finding what's broken and fixing it.

## Before Starting

**Check for context first:**
If `marketing-context.md` exists, read it before asking questions. Use that context and only ask for what's missing.

Gather this context:

### 1. Current State
- Do you have GA4 and/or GTM already set up? If so, what's broken or missing?
- What's your tech stack? (React SPA, Next.js, WordPress, custom, etc.)
- Do you have a consent management platform (CMP)? Which one?
- What events are you currently tracking (if any)?

### 2. Business Context
- What are your primary conversion actions? (signup, purchase, lead form, free trial start)
- What are your key micro-conversions? (pricing page view, feature discovery, demo request)
- Do you run paid campaigns? (Google Ads, Meta, LinkedIn — affects conversion tracking needs)

### 3. Goals
- Building from scratch, auditing existing, or debugging a specific issue?
- Do you need cross-domain tracking? Multiple properties or subdomains?
- Server-side tagging requirement? (GDPR-sensitive markets, performance concerns)

## How This Skill Works

### Mode 1: Set Up From Scratch
- No analytics in place — we'll build the tracking plan, implement GA4 and GTM, define the event taxonomy, and configure conversions.

### Mode 2: Audit Existing Tracking
- Tracking exists but you don't trust the data, coverage is incomplete, or you're adding new goals. We'll audit what's there, gap-fill, and clean up.

### Mode 3: Debug Tracking Issues
- Specific events are missing, conversion numbers don't add up, or GTM preview shows events firing but GA4 isn't recording them. Structured debugging workflow.

---

## Event Taxonomy Design

Get this right before touching GA4 or GTM. Retrofitting taxonomy is painful.

### Naming Convention

**Format:** `object_action` (snake_case, verb at the end)

| ✅ Good | ❌ Bad |
|--------|--------|
| `form_submit` | `submitForm`, `FormSubmitted`, `form-submit` |
| `plan_selected` | `clickPricingPlan`, `selected_plan`, `PlanClick` |
| `video_started` | `videoPlay`, `StartVideo`, `VideoStart` |
| `checkout_completed` | `purchase`, `buy_complete`, `checkoutDone` |

**Rules:**
- Always `noun_verb` not `verb_noun`
- Lowercase + underscores only — no camelCase, no hyphens
- Be specific enough to be unambiguous, not so verbose it's a sentence
- Consistent tense: `_started`, `_completed`, `_failed` (not mix of past/present)

### Standard Parameters

Every event should include these where applicable:

| Parameter | Type | Example | Purpose |
|-----------|------|---------|---------|
| `page_location` | string | `https://app.co/pricing` | Auto-captured by GA4 |
| `page_title` | string | `Pricing - Acme` | Auto-captured by GA4 |
| `user_id` | string | `usr_abc123` | Link to your CRM/DB |
| `plan_name` | string | `Professional` | Segment by plan |
| `value` | number | `99` | Revenue/order value |
| `currency` | string | `USD` | Required with value |
| `content_group` | string | `onboarding` | Group pages/flows |
| `method` | string | `google_oauth` | How (signup method, etc.) |

### Event Taxonomy for SaaS

**Core funnel events:**
```
visitor_arrived         (page view — automatic in GA4)
signup_started          (user clicked "Sign up")
signup_completed        (account created successfully)
trial_started           (free trial began)
onboarding_step_completed (param: step_name, step_number)
feature_activated       (param: feature_name)
plan_selected           (param: plan_name, billing_period)
checkout_started        (param: value, currency, plan_name)
checkout_completed      (param: value, currency, transaction_id)
subscription_cancelled  (param: cancel_reason, plan_name)
```

**Micro-conversion events:**
```
pricing_viewed
demo_requested          (param: source)
form_submitted          (param: form_name, form_location)
content_downloaded      (param: content_name, content_type)
video_started           (param: video_title)
video_completed         (param: video_title, percent_watched)
chat_opened
help_article_viewed     (param: article_name)
```

See [references/event-taxonomy-guide.md](references/event-taxonomy-guide.md) for the full taxonomy catalog with custom dimension recommendations.

---

## GA4 Setup

### Data Stream Configuration

1. **Create property** in GA4 → Admin → Properties → Create
2. **Add web data stream** with your domain
3. **Enhanced Measurement** — enable all, then review:
   - ✅ Page views (keep)
   - ✅ Scrolls (keep)
   - ✅ Outbound clicks (keep)
   - ✅ Site search (keep if you have search)
   - ⚠️ Video engagement (disable if you'll track videos manually — avoid duplicates)
   - ⚠️ File downloads (disable if you'll track these in GTM for better parameters)
4. **Configure domains** — add all subdomains used in your funnel

### Custom Events in GA4

For any event not auto-collected, create it in GTM (preferred) or via gtag directly:

**Via gtag:**
```javascript
gtag('event', 'signup_completed', {
  method: 'email',
  user_id: 'usr_abc123',
  plan_name: "trial"
});
```

**Via GTM data layer (preferred — see GTM section):**
```javascript
window.dataLayer.push({
  event: 'signup_completed',
  signup_method: 'email',
  user_id: 'usr_abc123'
});
```

### Conversions Configuration

Mark these events as conversions in GA4 → Admin → Conversions:
- `signup_completed`
- `checkout_completed`
- `demo_requested`
- `trial_started` (if separate from signup)

**Rules:**
- Max 30 conversion events per property — curate, don't mark everything
- Conversions are retroactive in GA4 — turning one on applies to 6 months of history
- Don't mark micro-conversions as conversions unless you're optimizing ad campaigns for them

---

## Google Tag Manager Setup

### Container Structure

```
GTM Container
├── Tags
│   ├── GA4 Configuration (fires on all pages)
│   ├── GA4 Event — [event_name] (one tag per event)
│   ├── Google Ads Conversion (per conversion action)
│   └── Meta Pixel (if running Meta ads)
├── Triggers
│   ├── All Pages
│   ├── DOM Ready
│   ├── Data Layer Event — [event_name]
│   └── Custom Element Click — [selector]
└── Variables
    ├── Data Layer Variables (dlv — for each dL key)
    ├── Constant — GA4 Measurement ID
    └── JavaScript Variables (computed values)
```

### Tag Patterns for SaaS

**Pattern 1: Data Layer Push (most reliable)**
 
Your app pushes to dataLayer → GTM listens.

```javascript
// In your app code (on event):
window.dataLayer = window.dataLayer || [];
window.dataLayer.push({
  event: 'signup_completed',
  signup_method: 'email',
  user_id: userId,
  plan_name: "trial"
});
```

```
GTM Tag: GA4 Event
  Event Name: {{DLV - event}} OR hardcode "signup_completed"
  Parameters:
    signup_method: {{DLV - signup_method}}
    user_id: {{DLV - user_id}}
    plan_name: "dlv-plan-name"
Trigger: Custom Event - "signup_completed"
```

**Pattern 2: CSS Selector Click**

For events triggered by UI elements without app-level hooks.

```
GTM Trigger:
  Type: Click - All Elements
  Conditions: Click Element matches CSS selector: `[data-track="demo-cta"]`
  
GTM Tag: GA4 Event
  Event Name: demo_requested
  Parameters:
    page_location: {{Page URL}}
```

See [references/gtm-patterns.md](references/gtm-patterns.md) for full configuration templates.

---

## Conversion Tracking: Platform-Specific

### Google Ads

1. Create conversion action in Google Ads → Tools → Conversions
2. Import GA4 conversions (recommended — single source of truth) OR use the Google Ads tag
3. Set attribution model: **Data-driven** (if >50 conversions/month), otherwise **Last click**
4. Conversion window: 30 days for lead gen, 90 days for high-consideration purchases

### Meta (Facebook/Instagram) Pixel

1. Install Meta Pixel base code via GTM
2. Standard events: `PageView`, `Lead`, `CompleteRegistration`, `Purchase`
3. Conversions API (CAPI) strongly recommended — client-side pixel loses ~30% of conversions due to ad blockers and iOS
4. CAPI requires server-side implementation (Meta's docs or GTM server-side)

---

## Cross-Platform Tracking

### UTM Strategy

Enforce strict UTM conventions or your channel data becomes noise.

| Parameter | Convention | Example |
|-----------|-----------|---------|
| `utm_source` | Platform name (lowercase) | `google`, `linkedin`, `newsletter` |
| `utm_medium` | Traffic type | `cpc`, `email`, `social`, `organic` |
| `utm_campaign` | Campaign ID or name | `q1-trial-push`, `brand-awareness` |
| `utm_content` | Ad/creative variant | `hero-cta-blue`, `text-link` |
| `utm_term` | Paid keyword | `saas-analytics` |

**Rule:** Never tag organic or direct traffic with UTMs. UTMs override GA4's automatic source/medium attribution.

### Attribution Windows

| Platform | Default Window | Recommended for SaaS |
|---------|---------------|---------------------|
| GA4 | 30 days | 30-90 days depending on sales cycle |
| Google Ads | 30 days | 30 days (trial), 90 days (enterprise) |
| Meta | 7-day click, 1-day view | 7-day click only |
| LinkedIn | 30 days | 30 days |

### Cross-Domain Tracking

For funnels that cross domains (e.g., `acme.com` → `app.acme.com`):

1. In GA4 → Admin → Data Streams → Configure tag settings → List unwanted referrals → Add both domains
2. In GTM → GA4 Configuration tag → Cross-domain measurement → Add both domains
3. Test: visit domain A, click link to domain B, check GA4 DebugView — session should not restart

---

## Data Quality

### Deduplication

**Events firing twice?** Common causes:

1. **Consent mode blocking** — user is in denied state
   - Check: In GTM Preview, look at Variables → `Analytics Storage` — is it `denied`?
   - Fix: Test with consent granted, or implement Advanced Consent Mode

2. **Filters blocking data** — internal traffic filter is active
   - Check: GA4 → Admin → Data Filters — is "Internal Traffic" filter active?
   - Fix: Disable filter temporarily, test, then re-enable and exclude your IP correctly

3. **Debug mode not enabled** — DebugView only shows debug-mode traffic
   - Check: Is `debug_mode: true` parameter on the GA4 Event tag?
   - Fix: Add it, or use the GA4 Debugger Chrome extension

4. **Wrong property** — you're looking at a different GA4 property
   - Check: Confirm Measurement ID in GTM matches the GA4 property you're viewing
   - Fix: Compare `G-XXXXXXXXXX` in GTM vs. GA4 Data Stream settings

5. **Duplicate GA4 configuration tags** — two config tags = double sessions + weird data
   - Check: GTM → Tags → filter by "GA4 Configuration" — more than one?
   - Fix: Delete duplicates, keep one with All Pages trigger

---

### Issue: Event not firing in GTM Preview at all

**Diagnosis path:**

**Step 1:** Check the trigger
- Is the trigger for this tag listed under the action in GTM Preview?
- If not: the trigger didn't fire

**Step 2:** Check trigger conditions
- Open the trigger in GTM
- Reproduce the exact scenario step by step
- In GTM Preview, check Variables at the moment the action happened
- Do the variable values match your trigger conditions?

**Step 3:** dataLayer issue (for Custom Event triggers)
- In GTM Preview → select the relevant event in left panel → Variables tab
- Scroll to find `event` — what's the value?
- If event name doesn't match trigger exactly: it won't fire (case-sensitive, exact match)

**Step 4:** Timing issue
- If using "Page View" trigger and element doesn't exist yet: switch to "DOM Ready" or "Window Loaded"
- If SPA: route changes may not trigger "Page View" — use History Change instead

---

### Issue: Parameters showing as (not set) or undefined in GA4

**Step 1:** Verify parameter is in the network request
- DevTools → Network → find GA4 collect request → Payload
- Search for the parameter name (e.g., `plan_name`)
- If not there: GTM variable isn't resolving correctly

**Step 2:** Check the GTM variable
- GTM Preview → find the event → Variables tab
- Find the variable for this parameter (e.g., `DLV - plan_name`)
- What's its value? If `undefined`: the dataLayer push didn't include this key, or key name is wrong

**Step 3:** Check dataLayer push in your app code
- DevTools → Console → type: `dataLayer.filter(e => e.event === 'your_event_name')`
- Inspect the object — is the parameter key present and spelled correctly?

**Step 4:** Check GA4 custom dimension registration
- Some parameters require a registered custom dimension in GA4 to appear in reports
- GA4 → Admin → Custom Definitions → Custom Dimensions
- If parameter isn't registered here: it'll exist in raw data but won't show in Explore reports

---

### Issue: Duplicate events (event fires 2x per action)

**Find the duplicates:**
- GTM Preview → find the action → how many tags with the same name fired?
- DevTools → Network → filter by `collect` → count hits for the action

**Common causes:**

1. **Enhanced Measurement + manual GTM tag**
   - e.g., Enhanced Measurement tracks outbound clicks, GTM also has an outbound click tag
   - Fix: disable the Enhanced Measurement setting OR remove the GTM tag

2. **Two GTM Configuration tags**
   - Each sends its own hits
   - Fix: delete one, keep one

3. **SPA router fires pageview + History Change trigger also fires**
   - Fix: disable Enhanced Measurement pageview, use only History Change tag

4. **Event fires on multiple triggers that both match**
   - Fix: make triggers more specific — add exclusion conditions

---

### Issue: Sessions/users look wrong (too high or too low)

**Too many sessions:**
- Multiple GA4 Configuration tags
- History Change trigger firing + Enhanced Measurement pageview on SPA
- Client ID not persisting (cookie being blocked or cleared)

**Too few sessions / users:**
- Consent blocking analytics for non-consenting users (expected under strict consent mode)
- Bot filtering too aggressive
- GA4 tags firing on wrong pages only

**Sessions reset unexpectedly (user shows as new on every page):**
- Cross-domain tracking not configured
- Cookie domain mismatch
- GTM cookie settings incorrect

---

### Issue: Conversions not matching between GA4 and Google Ads

**Check 1: Attribution window mismatch**
- GA4 default: 30-day last click
- Google Ads: check conversion action settings for window
- These legitimately produce different numbers

**Check 2: Conversion event names**
- In Google Ads → Tools → Conversions → imported from GA4
- Does the linked event name exactly match the GA4 event?

**Check 3: Import is linked**
- Google Ads → Tools → Linked Accounts → Google Analytics 4
- Is the correct GA4 property linked and synced?
- Sync can take 24-48 hours after changes

**Check 4: Enhanced Conversions**
- If GA4 uses a user_id or email parameter, Enhanced Conversions can improve matching
- Google Ads → Conversions → Enhanced Conversions for Web → Enable

---

## Debug Checklist Template

Use this for any new tracking issue:
```
[ ] Confirmed exact event name and parameters expected
[ ] Verified app code is pushing to dataLayer (console: dataLayer)
[ ] GTM Preview: trigger fires at correct moment
[ ] GTM Preview: parameters resolve to correct values (not undefined)
[ ] Network: GA4 collect request appears with correct payload
[ ] GA4 DebugView: event appears within 30 seconds
[ ] GA4 DebugView: parameters present and correct
[ ] GA4 Reports: event appears (24-48h delay for standard reports)
[ ] Consent check: tested with analytics consent granted
[ ] Filter check: internal traffic filter not blocking test traffic
```
