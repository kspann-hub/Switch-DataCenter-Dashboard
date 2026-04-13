PROJECT_TYPE = "data_center"
BRAND_NAME = "CriticalArc"
BRAND_COLOR = "#39B54A"

ISSUE_STATUS_ORDER = [
    "Open",
    "In Progress",
    "Ready To Inspect",
    "Work Complete",
    "Delayed Until After IST",
    "Information Only",
    "Void",
    "Closed",
]

ISSUE_STATUSES = ["Open", "In Progress", "Pending Verification", "Closed", "Void", "Work Complete", "Ready to Inspect", "Delayed Until After IST", "Information Only"]

# has the checklist had any work on it yet...
CHECKLIST_VERIFIED = ["Finished", "CxA Verified", "GC Verified", "GC to Verify", "Contractor Complete"]

# has the checklist been completed and verified by the GC or CxA?
checklist_complete_statuses = ["Finished", "CxA Verified", "GC Verified", "Contractor Complete"]

# fill in correct order of checklist statuses and their corresponding date fields
CHECKLIST_PIPELINE = [
    ("Not Started", "not_started_date"),
    ("In Progress", "in_progress_date"),
    ("GC to Verify", "gc_to_verify_date"),
    ("Finished", "finished_date"),
]

LEVEL_MAP = {
    'Component Verification': 'Component',
    'L2 - Installation Verification': 'L2',
    'L3 - Prefunctional': 'L3',
    'L2 - Skid Installation Verificiation': 'L2',
    'FAT - Factory Acceptance Test': 'FAT',
    'Level 1 - Site Acceptance': 'L1',
    'Level 2a - Set in Place Verification': 'L2a',
    'Level 2b - Installation Verification': 'L2b',
    'Level 2c - Pre-Energization Inspection': 'L2c',
    'Level 3 - Energization and Startup Verification': 'L3',
}

LEVELS_ORDERED = ['L1', 'L2', 'L2a', 'L2b', 'L2c', 'L3', 'FAT', 'Component']



# ── Keyword-based color rules (checked in order) ──
# If a status/category CONTAINS the keyword, it gets that color.
# First match wins, so order matters.

COLOR_RULES = [
    # Red — needs attention
    ("open",        "#E04040"),
    ("failed",      "#E04040"),
    ("rejected",    "#E04040"),
    ("overdue",     "#E04040"),

    # Yellow — waiting / warning
    ("ready",       "#F4B942"),
    ("pending",     "#F4B942"),
    ("inspect",     "#F4B942"),
    ("review",      "#F4B942"),

    # Blue — actively in progress
    ("in progress", "#92ADCA"),
    ("assigned",    "#4A90D9"),
    ("delivered",   "#4A90D9"),
    ("installation","#4A90D9"),

    # Purple — deferred / special
    ("delay",       "#B07CD8"),
    ("defer",       "#B07CD8"),
    ("hold",        "#B07CD8"),

    # Light green — contractor done, not fully verified
    ("contractor complete", "#6BCB77"),
    ("work complete",       "#6BCB77"),
    ("gc verified",         "#2ECC71"),

    # Brand green — fully done
    ("verified",    "#39B54A"),
    ("complete",    "#39B54A"),
    ("closed",      "#39B54A"),
    ("passed",      "#39B54A"),

    # Dark gray — removed / cancelled
    ("void",        "#5A5F68"),
    ("removed",     "#5A5F68"),
    ("cancelled",   "#5A5F68"),

    # Gray — informational / not started
    ("information", "#8A8F98"),
    ("released",    "#8A8F98"),
    ("designed",    "#8A8F98"),
    ("script",      "#8A8F98"),

    # Disciplines
    ("mechanical",    "#E74C3C"),
    ("hvac",          "#F4B942"),
    ("electrical",    "#F5A623"),
    ("plumbing",      "#4A90D9"),
    ("fire",          "#39B54A"),
    ("bms",           "#B07CD8"),
    ("controls",      "#B07CD8"),
    ("monitoring",    "#6BCB77"),

    # Priority levels
    ("high",          "#E04040"),   # red
    ("moderate",      "#F4B942"),   # yellow
    ("low",           "#39B54A"),   # green
]

# ── Level colors (these are consistent across projects) ──
LEVEL_COLORS = {
    "L1":  "#4A90D9",
    "L2a": "#F4B942",
    "L2b": "#E07C4A",
    "L2c": "#B07CD8",
    "L3":  "#39B54A",
}

FALLBACK_COLOR = "#8A8F98"


def get_color(name):
    """Match a status/category to a color using keyword rules."""
    if not name or str(name) in ['nan', 'None', '0', '']:
        return FALLBACK_COLOR

    # Check levels first
    if name in LEVEL_COLORS:
        return LEVEL_COLORS[name]

    # Keyword matching (case-insensitive)
    lower = str(name).lower()
    for keyword, color in COLOR_RULES:
        if keyword in lower:
            return color

    return FALLBACK_COLOR


def get_color_list(values):
    """Return colors for a list of category values."""
    return [get_color(v) for v in values]


def get_color_map(values):
    """Return a {value: color} dict for unique values."""
    return {v: get_color(v) for v in values}