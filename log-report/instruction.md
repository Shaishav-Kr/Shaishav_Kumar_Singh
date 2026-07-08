You have an Apache Combined Log Format access log at `/app/access.log`. Parse it and write a JSON report to `/app/report.json`.

The report must be a single JSON object with exactly these keys:

- `total_requests` — integer, total number of log lines
- `unique_ips` — integer, number of distinct client IP addresses
- `top_path` — string, the URL path with the most requests

Success criteria:

1. `/app/report.json` exists and is valid JSON.
2. `total_requests` is the correct integer count of all log entries.
3. `unique_ips` is the correct count of distinct client IPs.
4. `top_path` is the string path (e.g. `/index.html`) that appears most frequently in the log.