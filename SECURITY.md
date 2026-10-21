# Security Policy

## Supported Versions

Only the latest commit on `main` is supported. Fixes are not backported.

## Reporting a Vulnerability

Please don't open a public issue. Report it privately through the [Report a vulnerability](https://github.com/iSayZes/BDO-PAZ-Browser/security/advisories/new) form on the Security tab. Only the reporter and I can see it. If you can't use the form, message me on Discord (`sayzes`) instead.

Include:

- What the problem is and what an attacker could do with it
- Steps or a file that reproduces it
- The commit you tested on

I'll reply in the report thread, and credit you in the advisory when the fix is published unless you'd rather stay anonymous.

## Scope

The browser reads local game files and serves previews from a local server bound to `127.0.0.1` on a random port with a per-session token. Things worth reporting:

- A crafted `.paz`, `.meta` or other game file that runs code, writes outside the chosen output folder, or reads files it shouldn't
- The preview server being reachable from another machine, or answering without its token
- Script injection through file names or parsed text shown in the UI

Out of scope: crashes or wrong output on a malformed file with no security impact (open a [bug report](../../issues/new?template=bug-report.yml) instead), and anything about the game client or its servers.
