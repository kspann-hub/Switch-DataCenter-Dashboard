PROJECT_TYPE = "data_center"
BRAND_NAME = "CriticalArc"
BRAND_COLOR = "#39B54A"

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