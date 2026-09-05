# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest `main` | ✅ |
| Older commits | ❌ |

## Scope

This repository contains:
- **`tracker.html`** — a static single-page app served via GitHub Pages
- **Jupyter notebooks** (`.ipynb`) — solution notebooks, C#/Python/Go/Rust
- **GitHub Actions workflows** — CI, deployment, and release automation

## Reporting a Vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Please report security issues privately via [GitHub's private vulnerability reporting](https://github.com/sanjay-bhat/ProgrammingConcepts/security/advisories/new).

Include:
- A clear description of the vulnerability
- Steps to reproduce (or a proof-of-concept)
- Impact assessment (what an attacker could do)
- Any suggested mitigations

You will receive a response within **7 days**. If the issue is confirmed, a fix will be released as soon as practical.

## Security Measures in Place

### tracker.html (client-side app)
| Measure | Implementation |
|---------|----------------|
| Content Security Policy | `<meta http-equiv="Content-Security-Policy">` restricts script/style/connect sources |
| Subresource Integrity | All 6 CDN scripts carry `integrity=` SHA-384 hashes |
| Referrer Policy | `strict-origin-when-cross-origin` — no full URL leaked to external sites |
| XSS hardening | All user-controlled strings (playlist names) are HTML-escaped before DOM insertion |
| Clickjacking protection | `frame-ancestors 'none'` in CSP |
| Upgrade insecure requests | `upgrade-insecure-requests` in CSP |
| External link safety | `rel="noopener noreferrer"` on all `target="_blank"` links |

### GitHub Actions
| Measure | Implementation |
|---------|----------------|
| Principle of least privilege | Each workflow declares only the permissions it needs |
| Secret scanning | Gitleaks runs on every PR and push |
| Dependency updates | Dependabot monitors GitHub Actions weekly |
| SRI validation in CI | CI step confirms all CDN scripts have `integrity=` attributes |
| No secrets in code | All sensitive values use `${{ secrets.* }}` references |

## Known Limitations

- `'unsafe-inline'` is required in the script-src CSP directive because the tracker embeds ~2000 lines of JS inline. Moving to an external file (enabling a strict CSP hash or nonce) is a future improvement.
- The notebook viewer fetches content from `raw.githubusercontent.com` over HTTPS. Fetched content is rendered via `marked.js` (markdown → HTML); rendered output is set as `innerHTML` of a sandboxed content div. This is an accepted risk for a personal tool.
