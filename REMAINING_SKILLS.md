# Porting Summary - Claude-Skills → Nanobot-Superpowers

## Already Ported (149 total skills in nanobot-superpowers)

### Core Superpowers (13)
brainstorming, systematic-debugging, verification-before-completion, test-driven-development,
writing-plans, writing-skills, executing-plans, finishing-a-development-branch,
using-superpowers, receiving-code-review, requesting-code-review, instagram-poster, equity-report

### Engineering Skills (12)
nanobot-architect, nanobot-senior-frontend, nanobot-senior-backend, nanobot-senior-fullstack,
nanobot-senior-qa, nanobot-senior-ml-engineer, nanobot-senior-data-scientist,
nanobot-senior-data-engineer, nanobot-senior-computer-vision, nanobot-aws-solution-architect, nanobot-azure-cloud-architect, nanobot-gcp-cloud-architect

### Cloud & DevOps (8)
nanobot-devops, nanobot-senior-secops, nanobot-senior-security, nanobot-cloud-security,
nanobot-ai-security, nanobot-incident-commander, nanobot-ai-security, nanobot-incident-response,
nanobot-red-team, nanobot-security-pen-testing, nanobot-dependency-auditor

### AI/ML Skills (6)
nanobot-prompt-engineer, nanobot-self-improving-agent, nanobot-tdd-guide,
nanobot-tech-stack-evaluator, nanobot-stripe-integration-expert, nanobot-context-engine

### Agentic Skills (6)
nanobot-agent-designer, nanobot-agent-protocol, nanobot-agent-workflow-designer,
nanobot-agenthub, nanobot-decision-logger, nanobot-epic-design

### Security & Testing (4)
nanobot-incident-response, nanobot-red-team, nanobot-security-pen-testing, nanobot-dependency-auditor

### Marketing Skills (37)
nanobot-ad-creative, nanobot-brand-guidelines, nanobot-campaign-analytics,
nanobot-seo-audit, nanobot-ai-seo, nanobot-analytics-tracking,
nanobot-app-store-optimization, nanobot-churn-prevention, nanobot-cold-email,
nanobot-competitor-alternatives, nanobot-content-production, nanobot-content-strategy,
nanobot-copywriting, nanobot-email-sequence, nanobot-marketing-ops,
nanobot-marketing-psychology, nanobot-paid-ads, nanobot-programmatic-seo,
nanobot-social-media-manager, nanobot-x-twitter-growth, nanobot-marketing-strategy-pmm,
nanobot-content-creator, nanobot-content-humanizer, nanobot-copy-editing,
nanobot-form-cro, nanobot-free-tool-strategy, nanobot-launch-strategy,
nanobot-marketing-context, nanobot-marketing-demand-acquisition,
nanobot-marketing-ideas, nanobot-onboarding-cro, nanobot-page-cro,
nanobot-paywall-upgrade-cro, nanobot-popup-cro, nanobot-pricing-strategy,
nanobot-prompt-engineer-toolkit, nanobot-referral-program, nanobot-schema-markup,
nanobot-signup-flow-cro, nanobot-site-architecture, nanobot-social-content,
nanobot-social-media-analyzer

### Product Skills (8)
nanobot-agile-product-owner, nanobot-product-strategist, nanobot-ux-researcher-designer,
nanobot-product-analytics, nanobot-product-discovery, nanobot-competitive-teardown,
nanobot-experiment-designer, nanobot-roadmap-communicator

### Business Skills (3)
nanobot-customer-success-manager, nanobot-revenue-operations, nanobot-sales-engineer

### Finance Skills (10)
nanobot-financial-analyst, nanobot-saas-metrics-coach, nanobot-financial-orchestrator,
nanobot-financial-ratios, nanobot-data-normalizer, nanobot-bankruptcy-scorer,
nanobot-working-capital-analyst, nanobot-audit-interpreter, nanobot-off-balance-scanner,
nanobot-financial-research-report

### Project Management Skills (6)
nanobot-senior-pm, nanobot-scrum-master, nanobot-jira-expert,
nanobot-confluence-expert, nanobot-atlassian-admin, nanobot-atlassian-templates

### C-Level Advisory (24)
nanobot-ceo-advisor, nanobot-cfo-advisor, nanobot-cto-advisor, nanobot-coo-advisor,
nanobot-cmo-advisor, nanobot-ciso-advisor, nanobot-chief-of-staff, nanobot-board-meeting,
nanobot-board-deck-builder, nanobot-strategic-alignment, nanobot-company-os, nanobot-culture-architect,
nanobot-cpo-advisor, nanobot-cro-advisor, nanobot-cho-advisor, nanobot-cisos-onboard,
nanobot-founder-coach, nanobot-intl-expansion, nanobot-change-management, nanobot-scenario-war-room,
nanobot-org-health-diagnostic, nanobot-internal-narrative, nanobot-ma-playbook, nanobot-competitive-intel

### RA/QM Team (7)
nanobot-mdr-745-specialist, nanobot-iso13485-qms, nanobot-fda-consultant,
nanobot-iso27001-info-sec, nanobot-gdpr-dsgvo, nanobot-cpa-officer, nanobot-risk-management

### More Engineering (12)
nanobot-ci-cd-pipeline-builder, nanobot-mcp-server-builder, nanobot-database-designer,
nanobot-rag-architect, nanobot-observability-designer, nanobot-performance-profiler,
nanobot-monorepo-navigator, nanobot-release-manager, nanobot-runbook-generator,
nanobot-git-worktree-manager, nanobot-env-secrets-manager, nanobot-codebase-onboarding

### Orchestration (1)
nanobot-orchestration

---

## Genuinely Remaining (Not Yet Ported)

These are source skills in `claude-skills` that don't have a `nanobot-*` equivalent:

### Product Team (unique skills not covered by nanobot-product-*)
- `adversarial-reviewer` → `nanobot-adversarial-reviewer`
- `ux-researcher-designer` → already ported as `nanobot-ux-researcher-designer` ✓
- `competitive-teardown` → already ported as `nanobot-competitive-teardown` ✓
- `experiment-designer` → already ported as `nanobot-experiment-designer` ✓
- `product-analytics` → already ported as `nanobot-product-analytics` ✓
- `product-discovery` → already ported as `nanobot-product-discovery` ✓
- `product-strategist` → already ported as `nanobot-product-strategist` ✓
- `product-manager-toolkit` → `nanobot-product-manager-toolkit`
- `roadmap-communicator` → already ported as `nanobot-roadmap-communicator` ✓

### Business Growth (unique skills)
- `contract-and-proposal-writer` → `nanobot-contract-and-proposal-writer`
- `meeting-analyzer` → `nanobot-meeting-analyzer`

### Engineering Team (unique skills not covered by nanobot-senior-*)
- `api-design-reviewer` → already ported as `nanobot-api-design-reviewer` ✓
- `api-test-suite-builder` → `nanobot-api-test-suite-builder`
- `app-store-optimization` → already ported ✓
- `atlassian-admin` → already ported ✓
- `atlassian-templates` → already ported ✓
- `browser-automation` → `nanobot-browser-automation`
- `browserstack` → `nanobot-browserstack`
- `challenge` → `nanobot-challenge`
- `command-guide` → `nanobot-command-guide`
- `coverage` → `nanobot-coverage`
- `database-schema-designer` → `nanobot-database-schema-designer`
- `dependency-auditor` → already ported ✓
- `email-template-builder` → `nanobot-email-template-builder`
- `extract` → `nanobot-extract`
- `generate` → `nanobot-generate`
- `google-workspace` → `nanobot-google-workspace`
- `interview-system-designer` → `nanobot-interview-system-designer`
- `isms-audit-expert` → `nanobot-isms-audit-expert`
- `jira-expert` → already ported ✓
- `karpathy-check` → `nanobot-karpathy-check`
- `landing-page-generator` → `nanobot-landing-page-generator`
- `ms365-tenant-manager` → already ported ✓
- `persona` → `nanobot-persona`
- `plugin-audit` → `nanobot-plugin-audit`
- `postmortem` → `nanobot-postmortem`
- `pr-review-expert` → `nanobot-pr-review-expert`
- `product-manager` → already ported ✓
- `project-health` → `nanobot-project-health`
- `promote` → `nanobot-promote`
- `resume` → `nanobot-resume`
- `retro` → `nanobot-retro`
- `revenue-operations` → already ported ✓
- `rice` → `nanobot-rice`
- `scrum-master` → already ported ✓
- `secrets-vault-manager` → already ported ✓
- `senior-pm` → already ported ✓
- `solo-founder` → `nanobot-solo-founder`
- `spec-driven-workflow` → `nanobot-spec-driven-workflow`
- `spec-to-repo` → `nanobot-spec-to-repo`
- `sprint-health` → `nanobot-sprint-health`
- `sprint-plan` → `nanobot-sprint-plan`
- `sql-database-assistant` → `nanobot-sql-database-assistant`
- `startup-cto` → `nanobot-startup-cto`
- `stress-test` → `nanobot-stress-test`
- `team-communications` → `nanobot-team-communications`
- `tech-debt` → `nanobot-tech-debt`
- `tech-debt-tracker` → `nanobot-tech-debt-tracker`
- `testrail` → `nanobot-testrail`
- `threat-detection` → already ported ✓
- `ui-design-system` → `nanobot-ui-design-system`
- `user-story` → `nanobot-user-story`
- `wiki-ingest` → `nanobot-wiki-ingest`
- `wiki-init` → `nanobot-wiki-init`
- `wiki-lint` → `nanobot-wiki-lint`
- `wiki-log` → `nanobot-wiki-log`
- `wiki-query` → `nanobot-wiki-query`

### Marketing (unique skills not covered)
- `marketing-skills` → already ported (37 skills) ✓
- Most marketing skills already ported

---

## Recommendation

**The main remaining skills worth porting are:**
1. `nanobot-adversarial-reviewer` (unique)
2. `nanobot-api-test-suite-builder`
3. `nanobot-browser-automation`
4. `nanobot-browserstack`
5. `nanobot-challenge`
6. `nanobot-command-guide`
7. `nanobot-contract-and-proposal-writer`
8. `nanobot-coverage`
9. `nanobot-database-schema-designer`
10. `nanobot-email-template-builder`
11. `nanobot-extract`
12. `nanobot-generate`
13. `nanobot-google-workspace`
14. `nanobot-interview-system-designer`
15. `nanobot-karpathy-check`
16. `nanobot-landing-page-generator`
17. `nanobot-meeting-analyzer`
18. `nanobot-persona`
19. `nanobot-plugin-audit`
20. `nanobot-postmortem`
21. `nanobot-pr-review-expert`
22. `nanobot-product-manager-toolkit`
23. `nanobot-project-health`
24. `nanobot-promote`
25. `nanobot-resume`
26. `nanobot-retro`
27. `nanobot-rice`
28. `nanobot-solo-founder`
29. `nanobot-spec-driven-workflow`
30. `nanobot-spec-to-repo`
31. `nanobot-sprint-health`
32. `nanobot-sprint-plan`
33. `nanobot-sql-database-assitant`
34. `nanobot-stress-test`
35. `nanobot-tech-debt`
36. `nanobot-tech-debt-tracker`
37. `nanobot-testrail`
38. `nanobot-ui-design-system`
39. `nanobot-user-story`
40. `nanobot-wiki-*` (5 skills)

**However**, many of these are:
- **Editor/IDE helper skills** (likely not needed for nanobot)
- **Overlapping** with already ported `nanobot-senior-*` skills
- **Templates/tools** (not actual skills)

**Suggested next action:** Port only the unique, high-value skills that don't overlap with existing ported skills.
