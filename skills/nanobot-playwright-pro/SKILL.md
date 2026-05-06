# Nanobot Playwright Pro#

Advanced browser automation with Playwright for nanobot - testing, scraping, screenshot capture, and web interaction workflows.

## Use when#

- Automating browser tasks (form filling, navigation, data extraction)
- Creating end-to-end tests for web applications
- Capturing screenshots, generating PDFs, or printing pages
- Scraping dynamic content from JavaScript-heavy sites
- Testing responsive designs across multiple viewports
- Integrating browser automation into nanobot superpowers workflows#

## Core principle#

Browser automation should be reliable, maintainable, and mimic human behavior. nanobot helps you write Playwright scripts that are robust (wait for elements, handle errors), readable (clear selectors, comments), and respectful (rate limiting, user-agent rotation)—but the testing strategy and coverage decisions remain with the team.

## The Process#

### 1. Initialize Playwright#

Set up Playwright in your project:

```bash
# Initialize Playwright
python scripts/pw_init.py . --browser chromium,firefox,webkit#

# Output:
# ✓ Chromium installed (version 120.0.6099.109)
# ✓ Firefox installed (version 121.0)
# ✓ WebKit installed (version 17.4)
# ✓ Created playwright.config.js
# ✓ Created example tests in tests/#
# Verify installation
python scripts/pw_init.py . --verify
```

### 2. Generate Tests#

Create Playwright tests from specifications:

```bash
# Generate test from user story
python scripts/test_generator.py --story "User can log in with valid credentials" \
  --output tests/login.spec.js#

# Output:
# ✓ Generated test: tests/login.spec.js
# ✓ Includes:
#   - Navigate to login page
#   - Fill email and password
#   - Click submit button
#   - Assert redirect to dashboard
#   - Assert welcome message visible#
# Generate test with fixtures
python scripts/test_generator.py --story "User can update profile" \
  --fixtures fixtures/user.json \
  --output tests/profile.spec.js#
# Generate visual regression test
python scripts/test_generator.py --url https://example.com \
  --visual-regression \
  --output tests/visual.spec.js
```

### 3. Run Tests#

Execute tests across configured browsers:

```bash
# Run all tests
python scripts/test_runner.py .#

# Output:
# Running 12 tests across 3 browsers
# ✓ chromium: 12/12 passed (45s)
# ✓ firefox: 12/12 passed (52s)
# ✓ webkit: 11/12 passed (48s)
#   ✗ profile.spec.js: Update avatar test failed
#     Expected image to match, but 15% difference found#
# Run specific test
python scripts/test_runner.py tests/login.spec.js#

# Run with debugging
python scripts/test_runner.py . --debug#

# Run in headed mode (see the browser)
python scripts/test_runner.py . --headed
```

### 4. Fix Failures#

Diagnose and fix test failures:

```bash
# Analyze test failures
python scripts/test_fixer.py ./test_results/ --analyze#

# Output:
# === Test Failure Analysis ===
# Total tests: 12
# Passed: 11
# Failed: 1
#
# Failure: profile.spec.js - Update avatar
#   Error: Image comparison failed (15% diff)
#   Root cause: Avatar upload changes layout slightly
#   Suggestion: Update baseline image or increase threshold to 20%
#
# Auto-fix (where safe)
python scripts/test_fixer.py ./test_results/ --auto-fix#
# Generate new baseline
python scripts/test_fixer.py ./test_results/ --update-baseline
```

### 5. Generate Reports#

Create test reports and coverage analysis:

```bash
# Generate HTML report
python scripts/report_generator.py ./test_results/ --format html --output report.html#

# Output includes:
# - Test results by browser
# - Failure screenshots
# - Execution traces
# - Performance metrics (load time, interaction delay)#
# Generate coverage report
python scripts/report_generator.py . --coverage#

# Output:
# === Test Coverage Report ===
# Pages covered: 8/12 (67%)
# User flows covered: 5/8 (63%)
# Missing coverage:
#   - Admin dashboard
#   - Payment flow
#   - User settings#
# Export to CI/CD
python scripts/report_generator.py ./test_results/ --format junit --output junit.xml
```

## Tools Included#

### PW Init#
Initializes Playwright with browser downloads and configuration.

### Test Generator#
Creates Playwright test files from user stories or URLs.

### Test Runner#
Executes tests across Chromium, Firefox, and WebKit with debugging support.

### Test Fixer#
Analyzes failures and suggests fixes or auto-fixes safe cases.

### Report Generator#
Creates HTML reports, JUnit XML, and coverage analysis.

## Red Flags#

- **No waits** (page.goto without waitForLoadState) → Add explicit waits for reliability
- **Flaky tests** (>10% retry rate) → Investigate timing issues, add stable selectors
- **Hardcoded timeouts** (waitForTimeout(5000)) → Use explicit waits for elements
- **No screenshot on failure** → Always capture screenshot + DOM snapshot on failure
- **Testing internal details** (implementation-specific selectors) → Test user-visible behavior
- **No rate limiting** → Add delays between actions to mimic human behavior
- **Missing viewport tests** → Test responsive design at 375px, 768px, 1024px+
- **No cleanup** → Always reset state between tests (logout, clear cookies)#

## Test Patterns#

### Pattern 1: Reliable Navigation#
```javascript
// ✓ Good: Explicit waits
await page.goto('https://example.com/login');
await page.waitForLoadState('networkidle');
await page.waitForSelector('[data-testid="login-form"]');

// ✗ Bad: No waits
await page.goto('https://example.com/login');
await page.fill('#email', 'user@example.com'); // Might fail if page not loaded
```

### Pattern 2: Stable Selectors#
```javascript
// ✓ Good: data-testid attributes
await page.click('[data-testid="submit-button"]');

// ✓ Good: Accessible selectors
await page.fill('[aria-label="Email address"]', email);

// ✗ Bad: Brittle CSS selectors
await page.click('.btn-primary.submit-btn:nth-child(2)'); // Breaks on CSS changes
```

### Pattern 3: Visual Regression#
```javascript
// ✓ Good: Visual comparison with threshold
const screenshot = await page.screenshot();
expect(screenshot).toMatchSnapshot('login-page.png', { threshold: 0.2 });

// Update baseline when UI intentionally changes
// npm run test -- --update-snapshots
```

## Responsive Testing#

Test across common viewports:

```bash
# Run tests at mobile viewport
python scripts/test_runner.py . --viewport 375,667#

# Run tests at tablet viewport
python scripts/test_runner.py . --viewport 768,1024#

# Run tests at desktop viewport
python scripts/test_runner.py . --viewport 1920,1080#

# Test all viewports automatically
python scripts/test_runner.py . --all-viewports
```

## Common nanobot Commands#

```bash
# Setup
python scripts/pw_init.py . --browser chromium,firefox,webkit
python scripts/pw_init.py . --verify

# Test generation
python scripts/test_generator.py --story "User logs in" --output tests/login.spec.js
python scripts/test_generator.py --url https://example.com --visual-regression

# Test execution
python scripts/test_runner.py .                    # All tests
python scripts/test_runner.py tests/login.spec.js  # Single test
python scripts/test_runner.py . --headed            # See the browser
python scripts/test_runner.py . --debug             # Step through

# Fix failures
python scripts/test_fixer.py ./results/ --analyze
python scripts/test_fixer.py ./results/ --auto-fix

# Reports
python scripts/report_generator.py ./results/ --format html
python scripts/report_generator.py . --coverage
```

## Integration with nanobot Superpowers#

To use Playwright automation in your nanobot project:

1. **Add browser automation** to your agent's tool set
2. **Create test specs** for critical user flows
3. **Run in CI/CD** with the test runner
4. **Capture screenshots** for visual verification#

```javascript
// Example: Using nanobot with Playwright
const { chromium } = require('playwright');

async function automateWithNanobot(task) {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  // Navigate as nanobot would
  await page.goto(task.url);
  await page.waitForLoadState('networkidle');
  
  // Execute nanobot's planned actions
  for (const action of task.actions) {
    await page.waitForSelector(action.selector);
    await page.click(action.selector);
    await page.waitForTimeout(500); // Human-like delay
  }
  
  // Capture result
  const screenshot = await page.screenshot();
  await browser.close();
  return screenshot;
}
```

## References#

Load these files from the SKILL's `references/` directory for detailed information:

| File | Contains | When to Load |
|------|----------|--------------|
| `references/playwright_patterns.md` | Best practices, selector strategies, wait patterns | "unreliable tests", "flaky tests" |
| `references/visual_regression.md` | Snapshot testing, threshold configuration | "visual diff", "layout changed" |
| `references/ci_integration.md` | GitHub Actions, CircleCI, Jenkins setup | "run in pipeline", "CI/CD integration" |
| `references/debugging.md` | Trace viewer, screenshot comparison, common errors | "test failed", "why is this flaky" |
