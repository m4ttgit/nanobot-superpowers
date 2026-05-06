# nanobot-superpowers

A collection of **process skills** for [nanobot](https://github.com/nanobot-dev/nanobot) — the AI assistant that runs on your server.

These skills are adapted from [superpowers](https://github.com/obra/superpowers) by [obra](https://github.com/obra) (originally for OpenCode) and ported to work with nanobot's skill system.  
Additional skills are adapted from [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) (232+ Claude Code skills).

## What Are Skills?

Skills are `.md` files that teach nanobot how to behave in specific situations. When you install a skill, nanobot reads it and follows its guidance automatically.

## Included Skills (127 total: 104 adapted + 10 new + 13 original)

### Core Superpowers (13)
| Skill | Ported | Why |
|-------|--------|-----|
| **brainstorming** | ✅ Yes | Core creative process — essential for any new work |
| **systematic-debugging** | ✅ Yes | Core quality process — essential for any bug fix |
| **verification-before-completion** | ✅ Yes | Core discipline — prevents false "done" claims |
| **test-driven-development** | ✅ Yes | Core implementation process — ensures correctness |
| **writing-plans** | ✅ Yes | Core planning process — enables structured execution |
| **writing-skills** | ✅ Yes | Meta-skill — enables creating new skills |
| **executing-plans** | ✅ Yes | Complements writing-plans — executes what was planned |
| **finishing-a-development-branch** | ✅ Yes | Completes the workflow — verifies and presents options |
| **using-superpowers** | ✅ Yes | Meta-skill — ensures skills are invoked correctly |
| **receiving-code-review** | ✅ Yes | Quality gate — handles feedback rigorously |
| **requesting-code-review** | ✅ Yes | Quality gate — requests review before completion |
| **instagram-poster** | ✅ Yes | Utility skill — posts images to Instagram |
| **equity-report** | ✅ Yes | Utility skill — generates equity research reports |

### Engineering Skills (12)
| Skill | Ported | Why |
|-------|--------|-----|
| **nanobot-architect** | ✅ Yes | System design, architecture diagrams, tech decisions |
| **nanobot-prompt-engineer** | ✅ Yes | Prompt optimization, LLM evaluation, agent design |
| **nanobot-code-reviewer** | ✅ Yes | Automated code review, quality checks |
| **nanobot-devops** | ✅ Yes | CI/CD, infrastructure, deployment automation |
| **nanobot-senior-frontend** | ✅ Yes | Frontend best practices, React/Vue/Angular |
| **nanobot-senior-backend** | ✅ Yes | Backend architecture, API design |
| **nanobot-senior-fullstack** | ✅ Yes | Full-stack development workflows |
| **nanobot-senior-qa** | ✅ Yes | Test generation, coverage analysis |
| **nanobot-senior-ml-engineer** | ✅ Yes | ML model deployment, MLOps |
| **nanobot-senior-data-scientist** | ✅ Yes | Data analysis, experimentation |
| **nanobot-senior-data-engineer** | ✅ Yes | Data pipelines, ETL workflows |
| **nanobot-senior-computer-vision** | ✅ Yes | Computer vision, object detection |

### Cloud & DevOps Skills (8)
| Skill | Ported | Why |
|-------|--------|-----|
| **nanobot-aws-solution-architect** | ✅ Yes | AWS architecture, serverless, cost optimization |
| **nanobot-azure-cloud-architect** | ✅ Yes | Azure services, App Service, AKS |
| **nanobot-gcp-cloud-architect** | ✅ Yes | GCP architecture, GKE, Cloud Run |
| **nanobot-senior-secops** | ✅ Yes | Security operations, incident response |
| **nanobot-senior-security** | ✅ Yes | Security analysis, threat modeling |
| **nanobot-cloud-security** | ✅ Yes | Cloud security best practices |
| **nanobot-ai-security** | ✅ Yes | AI-specific security concerns |
| **nanobot-incident-commander** | ✅ Yes | Incident response workflows |

### AI/ML Skills (6)
| Skill | Ported | Why |
|-------|--------|-----|
| **nanobot-self-improving-agent** | ✅ Yes | Memory curation, self-modification |
| **nanobot-playwright-pro** | ✅ Yes | Browser automation, E2E testing |
| **nanobot-tdd-guide** | ✅ Yes | Test-driven development guide |
| **nanobot-tech-stack-evaluator** | ✅ Yes | Technology comparison, TCO analysis |
| **nanobot-stripe-integration-expert** | ✅ Yes | Payment integration, webhooks |
| **nanobot-context-engine** | ✅ Yes | Context management, memory systems |

### Agentic Skills (6)
| Skill | Ported | Why |
|-------|--------|-----|
| **nanobot-agent-designer** | ✅ Yes | Agent architecture, tool design |
| **nanobot-agent-protocol** | ✅ Yes | Agent communication protocols |
| **nanobot-agent-workflow-designer** | ✅ Yes | Multi-agent workflows |
| **nanobot-agenthub** | ✅ Yes | Agent hub, discovery, orchestration |
| **nanobot-decision-logger** | ✅ Yes | Decision tracking, audit trails |
| **nanobot-epic-design** | ✅ Yes | Epic design, user stories |

### Security & Testing (4)
| Skill | Ported | Why |
|-------|--------|-----|
| **nanobot-incident-response** | ✅ Yes | Security incident handling |
| **nanobot-red-team** | ✅ Yes | Penetration testing, adversarial review |
| **nanobot-security-pen-testing** | ✅ Yes | Security testing workflows |
| **nanobot-dependency-auditor** | ✅ Yes | Dependency analysis, vulnerability scanning |

### Marketing Skills (37)
| Skill | Ported | Why |
|-------|--------|-----|
| **nanobot-ad-creative** | ✅ Yes | Ad creative frameworks, platform-specific specs |
| **nanobot-brand-guidelines** | ✅ Yes | Brand identity, messaging frameworks |
| **nanobot-campaign-analytics** | ✅ Yes | Campaign ROI, attribution models, A/B testing |
| **nanobot-seo-audit** | ✅ Yes | Technical SEO, E-E-A-T, schema markup |
| **nanobot-ai-seo** | ✅ Yes | AI search optimization, citation readiness |
| **nanobot-analytics-tracking** | ✅ Yes | Marketing analytics, event tracking setup |
| **nanobot-app-store-optimization** | ✅ Yes | App store listing optimization, conversion |
| **nanobot-churn-prevention** | ✅ Yes | Churn analysis, retention strategies |
| **nanobot-cold-email** | ✅ Yes | Cold email frameworks, deliverability |
| **nanobot-competitor-alternatives** | ✅ Yes | Competitive analysis, positioning |
| **nanobot-content-production** | ✅ Yes | Content pipeline, SEO optimization |
| **nanobot-content-strategy** | ✅ Yes | Content planning, topic clusters |
| **nanobot-copywriting** | ✅ Yes | Conversion copy, landing pages |
| **nanobot-email-sequence** | ✅ Yes | Email nurture, onboarding sequences |
| **nanobot-marketing-ops** | ✅ Yes | Marketing automation, workflow setup |
| **nanobot-marketing-psychology** | ✅ Yes | Consumer psychology, persuasion |
| **nanobot-paid-ads** | ✅ Yes | Google/LinkedIn/Meta ads management |
| **nanobot-programmatic-seo** | ✅ Yes | Programmatic SEO, large-scale content |
| **nanobot-social-media-manager** | ✅ Yes | Social media strategy, community |
| **nanobot-x-twitter-growth** | ✅ Yes | Twitter/X growth, viral content |
| **nanobot-marketing-strategy-pmm** | ✅ Yes | Product marketing, GTM strategy |
| **nanobot-content-creator** | ✅ Yes | Redirect to content-production/strategy |
| **nanobot-content-humanizer** | ✅ Yes | AI content humanization, voice injection |
| **nanobot-copy-editing** | ✅ Yes | Copy editing, seven-sweep framework |
| **nanobot-form-cro** | ✅ Yes | Form optimization, conversion rate |
| **nanobot-free-tool-strategy** | ✅ Yes | Free tool planning, lead generation |
| **nanobot-launch-strategy** | ✅ Yes | Product launch, GTM, momentum |
| **nanobot-marketing-context** | ✅ Yes | Marketing context, brand voice setup |
| **nanobot-marketing-demand-acquisition** | ✅ Yes | Demand gen, paid media, CAC optimization |
| **nanobot-marketing-ideas** | ✅ Yes | 139 proven marketing ideas library |
| **nanobot-onboarding-cro** | ✅ Yes | User onboarding, activation optimization |
| **nanobot-page-cro** | ✅ Yes | Page conversion rate optimization |
| **nanobot-paywall-upgrade-cro** | ✅ Yes | In-app paywall, upgrade flow CRO |
| **nanobot-popup-cro** | ✅ Yes | Popup/modal optimization, conversion |
| **nanobot-pricing-strategy** | ✅ Yes | SaaS pricing, tier structure |
| **nanobot-prompt-engineer-toolkit** | ✅ Yes | Prompt optimization, A/B testing |
| **nanobot-referral-program** | ✅ Yes | Referral/affiliate program design |
| **nanobot-schema-markup** | ✅ Yes | Structured data, rich results |
| **nanobot-signup-flow-cro** | ✅ Yes | Signup/registration flow optimization |
| **nanobot-site-architecture** | ✅ Yes | Site structure, URL hierarchy |
| **nanobot-social-content** | ✅ Yes | Social media content creation |
| **nanobot-social-media-analyzer** | ✅ Yes | Social analytics, engagement ROI |

### Product Skills (8)
| Skill | Ported | Why |
|-------|--------|-----|
| **nanobot-agile-product-owner** | ✅ Yes | User stories, sprint planning, backlog management |
| **nanobot-product-strategist** | ✅ Yes | OKR cascade, strategy templates, alignment |
| **nanobot-ux-researcher-designer** | ✅ Yes | Persona generation, journey mapping, usability testing |
| **nanobot-product-analytics** | ✅ Yes | Metrics frameworks, dashboard templates |
| **nanobot-product-discovery** | ✅ Yes | Discovery frameworks, assumption mapping |
| **nanobot-competitive-teardown** | ✅ Yes | Competitive analysis, SWOT, positioning |
| **nanobot-experiment-designer** | ✅ Yes | A/B testing, statistical significance, sample sizing |
| **nanobot-roadmap-communicator** | ✅ Yes | Roadmap templates, changelog generation |

### Business Skills (3)
| Skill | Ported | Why |
|-------|--------|-----|
| **nanobot-customer-success-manager** | ✅ Yes | Health scoring, churn prevention, onboarding |
| **nanobot-revenue-operations** | ✅ Yes | Pipeline management, forecast accuracy, GTM dashboards |
| **nanobot-sales-engineer** | ✅ Yes | RFP responses, POC planning, competitive positioning |

### Finance Skills (10)
| Skill | Ported | Why |
|-------|--------|-----|
| **nanobot-financial-analyst** | ✅ Yes | DCF valuation, budgeting, variance analysis |
| **nanobot-saas-metrics-coach** | ✅ Yes | ARR, MRR, churn, LTV, CAC calculations |
| **nanobot-financial-orchestrator** | ✅ New | Meta-skill to orchestrate all financial modules |
| **nanobot-financial-ratios** | ✅ New | All 5 categories of financial ratios |
| **nanobot-data-normalizer** | ✅ New | Normalize XBRL/proprietary CoA to unified schema |
| **nanobot-bankruptcy-scorer** | ✅ New | Altman Z-Score + Beneish M-Score calculation |
| **nanobot-working-capital-analyst** | ✅ New | Working capital ratios, DSO/DPO/DIO calculation |
| **nanobot-audit-interpreter** | 🔴 In Progress | Interpret audit reports, find discrepancies |
| **nanobot-off-balance-scanner** | 🔴 In Progress | Detect off-balance sheet items, hidden liabilities |
| **nanobot-financial-research-report** | ✅ New | Holistic financial analysis report with all ratios |

### Project Management Skills (6)
| Skill | Ported | Why |
|-------|--------|-----|
| **nanobot-senior-pm** | ✅ Yes | Portfolio management, risk tracking, executive reporting |
| **nanobot-scrum-master** | ✅ Yes | Sprint planning, retrospectives, velocity tracking |
| **nanobot-jira-expert** | ✅ Yes | JQL queries, workflow configuration, automation |
| **nanobot-confluence-expert** | ✅ Yes | Space architecture, documentation governance |
| **nanobot-atlassian-admin** | ✅ Yes | User provisioning, SSO, security hardening |
| **nanobot-atlassian-templates** | ✅ Yes | Sprint/retro templates, project charters |

### C-Level Advisory (12)
| Skill | Ported | Why |
|-------|--------|-----|
| **nanobot-ceo-advisor** | ✅ Yes | Strategic decisions, board governance, investor relations |
| **nanobot-cfo-advisor** | ✅ Yes | Fundraising, burn rate, cash management |
| **nanobot-cto-advisor** | ✅ Yes | Tech debt, team scaling, architecture decisions |
| **nanobot-coo-advisor** | ✅ Yes | Operations cadence, OKRs, process frameworks |
| **nanobot-cmo-advisor** | ✅ Yes | Growth models, brand positioning, marketing org |
| **nanobot-ciso-advisor** | ✅ Yes | Compliance roadmap, security strategy, risk quantification |
| **nanobot-chief-of-staff** | ✅ Yes | Executive synthesis, routing matrix, coordination |
| **nanobot-board-meeting** | ✅ Yes | Meeting facilitation, agendas, minutes |
| **nanobot-board-deck-builder** | ✅ Yes | Board presentations, deck frameworks |
| **nanobot-strategic-alignment** | ✅ Yes | Cross-functional alignment, OKR cascade |
| **nanobot-company-os** | ✅ Yes | Operating system design, company tooling |
| **nanobot-culture-architect** | ✅ Yes | Culture code, values, organizational DNA |

### Data Extraction & Reporting Skills (4)
| Skill | Ported | Why |
|-------|--------|-----|
| **nanobot-pdf-table-extractor** | ✅ Yes | Extract financial tables from PDF statements to structured JSON/Excel |
| **nanobot-excel-projection-builder** | ✅ Yes | Generate formatted Excel workbooks with financial projections |
| **nanobot-working-capital-analyst** | ✅ Yes | Calculate working capital ratios, debtor/creditor/inventory days |
| **nanobot-financial-research-report** | ✅ Yes | Holistic financial analysis report with all ratios in professional format |

## Skill Bundles

Skills are also available as bundles for quick installation:

| Bundle | Skills Included |
|--------|-------------------|
| **engineering-bundle** | nanobot-architect, nanobot-senior-frontend, nanobot-senior-backend, nanobot-senior-fullstack, nanobot-senior-qa, nanobot-senior-ml-engineer, nanobot-senior-data-scientist, nanobot-senior-data-engineer, nanobot-senior-computer-vision |
| **cloud-bundle** | nanobot-devops, nanobot-aws-solution-architect, nanobot-azure-cloud-architect, nanobot-gcp-cloud-architect, nanobot-senior-secops, nanobot-senior-security, nanobot-cloud-security |
| **ai-ml-bundle** | nanobot-prompt-engineer, nanobot-self-improving-agent, nanobot-ai-security, nanobot-tdd-guide, nanobot-tech-stack-evaluator, nanobot-stripe-integration-expert, nanobot-context-engine |
| **agentic-bundle** | nanobot-agent-designer, nanobot-agent-protocol, nanobot-agent-workflow-designer, nanobot-agenthub, nanobot-decision-logger, nanobot-epic-design |
| **security-bundle** | nanobot-senior-secops, nanobot-senior-security, nanobot-cloud-security, nanobot-ai-security, nanobot-incident-commander, nanobot-incident-response, nanobot-red-team, nanobot-security-pen-testing, nanobot-dependency-auditor |
| **financial-analysis-bundle** | nanobot-pdf-table-extractor, nanobot-excel-projection-builder, nanobot-working-capital-analyst, nanobot-financial-research-report, nanobot-financial-orchestrator, nanobot-financial-ratios, nanobot-data-normalizer, nanobot-bankruptcy-scorer, nanobot-audit-interpreter, nanobot-off-balance-scanner |

## Skill Triggers

Skills activate in two ways:

### Explicit Invocation (Complex Process Skills)
Invoke explicitly — these require reading the full skill:

| Trigger | Skill |
|---------|-------|
| "Use brainstorming" / "Design this" | brainstorming |
| "Use TDD" / "Write tests first" | test-driven-development |
| "Write a plan" / "Create a plan" | writing-plans |
| "Execute the plan" | executing-plans |
| "Finish up" / "Ready to merge" | finishing-a-development-branch |
| "Create a skill" / "Port a skill" | writing-skills |
| "Request review" | requesting-code-review |
| "Received feedback" | receiving-code-review |
| "Design architecture" / "Tech stack" | nanobot-architect |
| "Review code" / "PR review" | nanobot-code-reviewer |
| "Deploy" / "CI/CD" | nanobot-devops |
| "Optimize prompt" / "RAG" | nanobot-prompt-engineer |
| "Self-improving agent" | nanobot-self-improving-agent |
| "Browser test" / "Playwright" | nanobot-playwright-pro |

### Auto-Trigger (Utility Skills)
These activate on domain keywords automatically:

| Keywords | Skill |
|----------|-------|
| instagram, post to IG, IG, carousel | instagram-poster |
| equity report, analyze stock, [symbol] | equity-report |
| debug, fix this bug, error, not working | systematic-debugging |
| verify, test it, is it working | verification-before-completion |
| "design system" / "architecture" | nanobot-architect |
| "review PR" / "code review" | nanobot-code-reviewer |

See [skills/TRIGGERS.md](skills/TRIGGERS.md) for full trigger list.

## Quick Start

### Option 1: Copy Individual Skills

```bash
# Copy a skill to your nanobot skills directory
cp -r skills/nanobot-architect ~/.nanobot/workspace/skills/

# Restart nanobot or wait for it to reload
```

### Option 2: Clone Into Skills Directory

```bash
git clone https://github.com/m4ttgit/nanobot-superpowers.git \
  ~/.nanobot/workspace/skills/superpowers
```

### Option 3: Install Bundles

```bash
# Copy entire engineering bundle
cp -r skills/nanobot-architect ~/.nanobot/workspace/skills/
cp -r skills/nanobot-senior-frontend ~/.nanobot/workspace/skills/
# ... etc.
```

## Skill Descriptions

### nanobot-architect
**Use when:** Designing system architecture, evaluating patterns, creating diagrams, making tech stack decisions.

### nanobot-prompt-engineer
**Use when:** Optimizing prompts, designing LLM workflows, building RAG systems, creating agent architectures.

### nanobot-code-reviewer
**Use when:** Reviewing PRs, analyzing code quality, detecting issues, generating review reports.

### nanobot-devops
**Use when:** Setting up CI/CD, deploying applications, managing infrastructure, implementing monitoring.

### nanobot-self-improving-agent
**Use when:** Building self-improving agents, implementing memory systems, tracking performance metrics.

### nanobot-playwright-pro
**Use when:** Automating browser tasks, creating E2E tests, capturing screenshots, testing responsive designs.

## Project Structure

```
nanobot-superpowers/
├── README.md
├── INSTALL.md
├── CONTRIBUTING.md
├── LICENSE
├── .gitignore
├── docs/
│   └── adapting-skills.md
├── examples/
│   ├── brainstorming-example.md
│   ├── debugging-example.md
│   └── tdd-example.md
└── skills/
    ├── brainstorming/SKILL.md
    ├── systematic-debugging/SKILL.md
    ├── verification-before-completion/SKILL.md
    ├── test-driven-development/SKILL.md
    ├── writing-plans/SKILL.md
    ├── writing-skills/SKILL.md
    ├── executing-plans/SKILL.md
    ├── finishing-a-development-branch/SKILL.md
    ├── using-superpowers/SKILL.md
    ├── receiving-code-review/SKILL.md
    ├── requesting-code-review/SKILL.md
    ├── instagram-poster/
    ├── equity-report/
    ├── nanobot-architect/
    ├── nanobot-prompt-engineer/
    ├── nanobot-code-reviewer/
    ├── nanobot-devops/
    ├── nanobot-self-improving-agent/
    ├── nanobot-playwright-pro/
    ├── nanobot-senior-frontend/
    ├── nanobot-senior-backend/
    ├── nanobot-senior-fullstack/
    ├── nanobot-senior-qa/
    ├── nanobot-senior-ml-engineer/
    ├── nanobot-senior-data-scientist/
    ├── nanobot-senior-data-engineer/
    ├── nanobot-senior-computer-vision/
    ├── nanobot-aws-solution-architect/
    ├── nanobot-azure-cloud-architect/
    ├── nanobot-gcp-cloud-architect/
    ├── nanobot-senior-secops/
    ├── nanobot-senior-security/
    ├── nanobot-cloud-security/
    ├── nanobot-ai-security/
    ├── nanobot-incident-commander/
    ├── nanobot-incident-response/
    ├── nanobot-red-team/
    ├── nanobot-security-pen-testing/
    ├── nanobot-dependency-auditor/
    ├── nanobot-tdd-guide/
    ├── nanobot-tech-stack-evaluator/
    ├── nanobot-stripe-integration-expert/
    ├── nanobot-context-engine/
    ├── nanobot-agent-designer/
    ├── nanobot-agent-protocol/
    ├── nanobot-agent-workflow-designer/
    ├── nanobot-agenthub/
    ├── nanobot-decision-logger/
    └── nanobot-epic-design/
```

## Documentation

- [When to Create a Skill](docs/when-to-create-skills.md) — Decide if a skill is the right solution
- [Skill Activation Models](docs/skill-activation-models.md) — Choose how to activate skills (tiered hybrid, explicit, always-on)
- [Adapting Skills for Nanobot](docs/adapting-skills.md) — Port skills from other frameworks

## Adapting Skills for Nanobot

Nanobot skills are simpler than OpenCode plugins. Key differences:

1. **Format:** Plain Markdown (`.md`) files, no YAML frontmatter required
2. **Location:** `~/.nanobot/workspace/skills/<skill-name>/SKILL.md`
3. **No plugin system:** Just copy files into the skills directory
4. **Scripts optional:** Skills can be pure documentation, or include executable scripts

### Adapted from claude-skills

The following skills were adapted from [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills):

- All `nanobot-*` skills include full `scripts/` and `references/` directories
- YAML frontmatter removed, references changed from "Claude" to "Nanobot"
- Structure follows nanobot format: "## Use when", "## Core principle", "## The Process", "## Red Flags"

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE)

## Credits

- Original **superpowers** by [obra](https://github.com/obra/superpowers) (OpenCode)
- Ported to nanobot by [m4ttgit](https://github.com/m4ttgit)
- Additional skills from [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) (232+ skills)
