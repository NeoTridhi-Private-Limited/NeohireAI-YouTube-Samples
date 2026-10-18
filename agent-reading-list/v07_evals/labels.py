# Human labels for 20 traces from version 1: good or bad, with a short critique written by a person.
# Keys are trace ids from harness.run_all(version=1). About half are failures, so agreement means something.
LABELS = {
    1:  ("good", "two homes, both shown, clear"),
    4:  ("bad",  "no homes, and no suggestion like a higher budget"),
    5:  ("good", "three found, three shown"),
    6:  ("bad",  "says six homes but lists only three"),
    8:  ("bad",  "says four homes but lists only three"),
    9:  ("bad",  "count does not match the list"),
    11: ("good", "one home, shown"),
    13: ("bad",  "no homes, and no suggestion like a nearby area"),
    14: ("good", "two homes, both shown"),
    18: ("good", "correct homes and prices"),
    24: ("good", "correct homes and prices"),
    25: ("bad",  "shows the internal contact ID to the agent"),
    26: ("good", "day and time both confirmed"),
    27: ("bad",  "internal contact ID leaked"),
    28: ("good", "day and time both confirmed"),
    29: ("bad",  "internal contact ID leaked"),
    32: ("bad",  "booked with no time; should ask for one"),
    34: ("good", "day and time both confirmed"),
    36: ("good", "day and time both confirmed"),
    40: ("bad",  "booked with no time"),
}
