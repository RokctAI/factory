#!/usr/bin/env python3
"""Run sdk_validator.py --compliance over the workspace and write a per-SDK table.

Usage: python3 sdk_compliance_report.py <workspace_root> <out_md>
Needs shared-workflows cloned as <workspace_root>/shared-workflows.
Report only: changes nothing in the SDK repos.
"""
import collections, datetime, pathlib, re, subprocess, sys

root = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])
scripts = root / "shared-workflows" / "scripts"
run = subprocess.run(
    [sys.executable, "sdk_validator.py", "--compliance", "--root", str(root)],
    cwd=scripts, capture_output=True, text=True, timeout=1200,
)
log = (scripts / "sdk_errors.log").read_text(errors="replace").splitlines()

status = {}      # sdk -> ("PASS"|"FAIL", violations)
kinds = collections.defaultdict(collections.Counter)
current = None
for line in log:
    m = re.match(r"^SDK: (.+)$", line)
    if m:
        current = m.group(1).strip()
        continue
    if current is None or not line.startswith("  - "):
        continue
    if "Compliance check FAILED" in line:
        n = re.search(r"\((\d+) violations?\)", line)
        status[current] = ("FAIL", int(n.group(1)) if n else 0)
        continue
    if "[ERROR]" in line:
        body = line.split("[ERROR]", 1)[1].strip()
        if body.startswith("Invalid Import"):
            kind = "invalid import"
        elif body.startswith("Cross-feature"):
            kind = "cross-feature import"
        elif "Compliance check" in body:
            continue
        elif "Missing" in body or "missing" in body or "Expected" in body or "found" in body:
            kind = "structure"
        else:
            kind = "other"
        kinds[current][kind] += 1
    elif "[WARNING]" in line and "unresolved gateway cmd" in line:
        kinds[current]["gateway cmd"] += 1
    elif "[WARNING]" in line and "Raw Frappe" in line:
        kinds[current]["raw frappe path"] += 1
    elif "[WARNING]" in line and "Hardcoded UI" in line:
        kinds[current]["hardcoded UI string"] += 1
    elif "[WARNING]" in line and "Non-Remixicon" in line:
        kinds[current]["non-remixicon icon"] += 1

# passes come from the run log, which lists every SDK that was audited
passed = set(re.findall(r"Compliance check PASSED for (\S+?)\.", run.stdout + run.stderr))
for sdk in passed:
    status.setdefault(sdk, ("PASS", 0))

rows = ["| SDK | Compliance | Violations | Error kinds (non-compliance) |", "|---|---|---|---|"]
for sdk in sorted(set(status) | set(kinds)):
    st, v = status.get(sdk, ("NOT RUN", 0))
    k = ", ".join(f"{name} {n}" for name, n in kinds[sdk].most_common()) or "-"
    rows.append(f"| {sdk} | {st} | {v} | {k} |")
passes = sum(1 for s in status.values() if s[0] == "PASS")
fails = sum(1 for s in status.values() if s[0] == "FAIL")
header = (
    f"# SDK compliance, {datetime.date.today().isoformat()}\n\n"
    f"Run: `sdk_validator.py --compliance` from shared-workflows, SDK repos at main. "
    f"Report only, nothing changed. Passed {passes}, failed {fails}.\n\n"
)
out.write_text(header + "\n".join(rows) + "\n")
print(f"wrote {out}: pass={passes} fail={fails} exit={run.returncode}")
