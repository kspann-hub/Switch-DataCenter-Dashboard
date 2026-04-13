# New Project Setup Guide

A step-by-step guide for discovering your project's data and configuring the dashboard to match.

---

## Step 1: Sync the Data

Before configuring anything, pull data from CxAlloy into SQLite:

```bash
python sync_job.py
```

Wait for it to finish (you'll see row counts and "Sync complete"). Then Ctrl+C to stop the scheduler.

---

## Step 2: Discover Your Data

Run these commands in the terminal to see what your project's data looks like. Copy the output — you'll use it to fill in `config.py` and `cleaning.py`.

### Issue Statuses

```bash
python -c "
import sqlite3, pandas as pd
conn = sqlite3.connect('dashboard_data.db')
print(pd.read_sql('SELECT DISTINCT status FROM [Issues]', conn))
"
```

**Where to edit:** `config.py` → `ISSUE_STATUSES`

---

### Checklist Statuses

```bash
python -c "
import sqlite3, pandas as pd
conn = sqlite3.connect('dashboard_data.db')
print(pd.read_sql('SELECT DISTINCT status FROM [Checklists]', conn))
"
```

**Where to edit:** `config.py` → three places:
- `checklist_complete_statuses` — statuses that mean "done" (used for completion percentages)
- `CHECKLIST_VERIFIED` — statuses that mean "work finished or in review" (used for equipment tab progress bars)
- These can be the same list if you don't need the distinction

---

### Checklist Types → Level Mapping

```bash
python -c "
import sqlite3, pandas as pd
conn = sqlite3.connect('dashboard_data.db')
print(pd.read_sql('SELECT DISTINCT type_name FROM [Checklists]', conn))
"
```

**Where to edit:** `config.py` → `LEVEL_MAP` and `LEVELS_ORDERED`

Each `type_name` from CxAlloy needs to be mapped to a short level label used in the dashboard. Example:

```python
LEVEL_MAP = {
    'L2 - Installation Verification': 'L2',
    'L3 - Prefunctional': 'L3',
    'FAT - Factory Acceptance Test': 'FAT',
    'Component Verification': 'Component',
    # Add every type_name from your output here
}

LEVELS_ORDERED = ['L2', 'L3', 'FAT', 'Component']
# The order they appear in the dashboard (left to right)
```

**Also edit:** `cleaning.py` → inside `clean_checklists()`, make sure the level derivation uses the config:

```python
if 'type_name' in df.columns:
    from config import LEVEL_MAP
    df['level'] = df['type_name'].map(LEVEL_MAP).fillna('Other')
```

---

### Checklist Pipeline Dates (Extended Status Fields)

```bash
python -c "
import sqlite3, pandas as pd, json
conn = sqlite3.connect('dashboard_data.db')
df = pd.read_sql('SELECT extended_status FROM [Checklists] LIMIT 5', conn)
for val in df['extended_status']:
    try:
        print(list(json.loads(val).keys()))
        break
    except: pass
"
```

**Where to edit:** `config.py` → `CHECKLIST_PIPELINE` — each stage is a tuple of (display name, date field name):

```python
CHECKLIST_PIPELINE = [
    ("Not Started", "not_started_date"),
    ("In Progress", "in_progress_date"),
    ("GC to Verify", "gc_to_verify_date"),
    ("Finished", "finished_date"),
]
```

**Also edit:** `cleaning.py` → inside `clean_checklists()`, the `flatten_extended_status` call must list the same date fields:

```python
df = flatten_extended_status(df, [
    'not_started_date', 'in_progress_date',
    'gc_to_verify_date', 'finished_date',
])
```

---

### Test Statuses

```bash
python -c "
import sqlite3, pandas as pd
conn = sqlite3.connect('dashboard_data.db')
print(pd.read_sql('SELECT DISTINCT status FROM [Tests]', conn))
"
```

**Where to edit:** `layout.py` — tests don't have a config entry, but the test tab hardcodes status checks like `tests['status'] == 'Passed'`. If your project uses different status names (e.g. "Complete" instead of "Passed"), update the comparisons in the Tab 3 section of `layout.py`.

Common things to check in layout.py Tab 3:
- `passed = (tests['status'] == 'Passed').sum()` — is "Passed" the right value?
- `failed = (tests['status'] == 'Failed').sum()` — is "Failed" the right value?
- `not_started = (tests['status'] == 'Not Started').sum()` — is "Not Started" the right value?

---

### Equipment Statuses

```bash
python -c "
import sqlite3, pandas as pd
conn = sqlite3.connect('dashboard_data.db')
print(pd.read_sql('SELECT DISTINCT status FROM [Equipment]', conn))
"
```

**Where to edit:** `layout.py` → Tab 4 (Equipment) — the KPI cards hardcode status checks like:

```python
delivered = (equipment['status'] == 'Delivered').sum()
installing = (equipment['status'] == 'Installation in Progress').sum()
```

Update these to match your project's equipment statuses.

---

### Equipment Attributes (Building Phase, Floor, etc.)

```bash
python -c "
import sqlite3, pandas as pd, json
conn = sqlite3.connect('dashboard_data.db')
df = pd.read_sql('SELECT attributes FROM [Equipment] LIMIT 5', conn)
for val in df['attributes']:
    try:
        attrs = json.loads(val)
        for a in attrs:
            print(f\"{a.get('name')}: {a.get('value', '')}\")
        print('---')
        break
    except: pass
"
```

**Where to edit:** `layout.py` → Tab 4 — the `_get_attr()` function extracts attributes by name. If your project uses different attribute names (e.g. "Phase" instead of "Building Phase"), update the strings in:

```python
equipment['building_phase'] = equipment['attributes'].apply(
    lambda x: _get_attr(x, 'Building Phase'))
equipment['floor_parsed'] = equipment['attributes'].apply(
    lambda x: _get_attr(x, 'Floor'))
```

---

## Step 3: Quick Reference — What to Edit Where

| What | File | Variable/Section |
|------|------|-----------------|
| Issue statuses | `config.py` | `ISSUE_STATUSES` |
| Checklist "done" statuses | `config.py` | `checklist_complete_statuses` |
| Checklist "verified" statuses | `config.py` | `CHECKLIST_VERIFIED` |
| Checklist type → level mapping | `config.py` | `LEVEL_MAP` |
| Level display order | `config.py` | `LEVELS_ORDERED` |
| Pipeline stages and date fields | `config.py` | `CHECKLIST_PIPELINE` |
| Level derivation code | `cleaning.py` | `clean_checklists()` |
| Pipeline date extraction | `cleaning.py` | `flatten_extended_status()` call |
| Test status comparisons | `layout.py` | Tab 3 section |
| Equipment status KPIs | `layout.py` | Tab 4 KPI section |
| Equipment attribute names | `layout.py` | Tab 4 `_get_attr()` calls |
| Project type and branding | `config.py` | `PROJECT_TYPE`, `BRAND_NAME`, `BRAND_COLOR` |

---

## Step 4: Verify

After making all edits:

```bash
streamlit run app.py
```

Check each tab:
- **Tab 1 (Issues)** — KPIs show correct counts, status chart labels match
- **Tab 2 (Checklists)** — Level donuts appear, completion percentages look right
- **Tab 3 (Tests)** — Pass/fail counts add up to total
- **Tab 4 (Equipment)** — KPI counts match, filters work

---

## Step 5: Commit and Deploy

```bash
git add -A
git commit -m "Configure for new project"
git push
```