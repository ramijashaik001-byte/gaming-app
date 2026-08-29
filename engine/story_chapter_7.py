# -*- coding: utf-8 -*-
"""NeonRogue Interactive Story Dialogue System - Chapter 7
This file contains narrative branches, choice states, and dialogue structures.
"""

CHAPTER_7_NODES = {
    "CH7_NODE_0001": {
        "id": "CH7_NODE_0001",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 1 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 7'.",
        "prompt": "Agent Neo, do you wish to decrypt node 1 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0002", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0003", "xp": 5}
        ]
    },
    "CH7_NODE_0002": {
        "id": "CH7_NODE_0002",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 2 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 14'.",
        "prompt": "Agent Neo, do you wish to decrypt node 2 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0003", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0004", "xp": 5}
        ]
    },
    "CH7_NODE_0003": {
        "id": "CH7_NODE_0003",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 3 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 21'.",
        "prompt": "Agent Neo, do you wish to decrypt node 3 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0004", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0005", "xp": 5}
        ]
    },
    "CH7_NODE_0004": {
        "id": "CH7_NODE_0004",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 4 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 28'.",
        "prompt": "Agent Neo, do you wish to decrypt node 4 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0005", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0006", "xp": 5}
        ]
    },
    "CH7_NODE_0005": {
        "id": "CH7_NODE_0005",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 5 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 35'.",
        "prompt": "Agent Neo, do you wish to decrypt node 5 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0006", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0007", "xp": 5}
        ]
    },
    "CH7_NODE_0006": {
        "id": "CH7_NODE_0006",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 6 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 42'.",
        "prompt": "Agent Neo, do you wish to decrypt node 6 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0007", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0008", "xp": 5}
        ]
    },
    "CH7_NODE_0007": {
        "id": "CH7_NODE_0007",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 7 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 49'.",
        "prompt": "Agent Neo, do you wish to decrypt node 7 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0008", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0009", "xp": 5}
        ]
    },
    "CH7_NODE_0008": {
        "id": "CH7_NODE_0008",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 8 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 56'.",
        "prompt": "Agent Neo, do you wish to decrypt node 8 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0009", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0010", "xp": 5}
        ]
    },
    "CH7_NODE_0009": {
        "id": "CH7_NODE_0009",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 9 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 63'.",
        "prompt": "Agent Neo, do you wish to decrypt node 9 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0010", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0011", "xp": 5}
        ]
    },
    "CH7_NODE_0010": {
        "id": "CH7_NODE_0010",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 10 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 70'.",
        "prompt": "Agent Neo, do you wish to decrypt node 10 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0011", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0012", "xp": 5}
        ]
    },
    "CH7_NODE_0011": {
        "id": "CH7_NODE_0011",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 11 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 77'.",
        "prompt": "Agent Neo, do you wish to decrypt node 11 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0012", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0013", "xp": 5}
        ]
    },
    "CH7_NODE_0012": {
        "id": "CH7_NODE_0012",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 12 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 84'.",
        "prompt": "Agent Neo, do you wish to decrypt node 12 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0013", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0014", "xp": 5}
        ]
    },
    "CH7_NODE_0013": {
        "id": "CH7_NODE_0013",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 13 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 91'.",
        "prompt": "Agent Neo, do you wish to decrypt node 13 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0014", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0015", "xp": 5}
        ]
    },
    "CH7_NODE_0014": {
        "id": "CH7_NODE_0014",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 14 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 98'.",
        "prompt": "Agent Neo, do you wish to decrypt node 14 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0015", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0016", "xp": 5}
        ]
    },
    "CH7_NODE_0015": {
        "id": "CH7_NODE_0015",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 15 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 105'.",
        "prompt": "Agent Neo, do you wish to decrypt node 15 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0016", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0017", "xp": 5}
        ]
    },
    "CH7_NODE_0016": {
        "id": "CH7_NODE_0016",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 16 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 112'.",
        "prompt": "Agent Neo, do you wish to decrypt node 16 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0017", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0018", "xp": 5}
        ]
    },
    "CH7_NODE_0017": {
        "id": "CH7_NODE_0017",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 17 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 119'.",
        "prompt": "Agent Neo, do you wish to decrypt node 17 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0018", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0019", "xp": 5}
        ]
    },
    "CH7_NODE_0018": {
        "id": "CH7_NODE_0018",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 18 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 126'.",
        "prompt": "Agent Neo, do you wish to decrypt node 18 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0019", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0020", "xp": 5}
        ]
    },
    "CH7_NODE_0019": {
        "id": "CH7_NODE_0019",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 19 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 133'.",
        "prompt": "Agent Neo, do you wish to decrypt node 19 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0020", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0021", "xp": 5}
        ]
    },
    "CH7_NODE_0020": {
        "id": "CH7_NODE_0020",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 20 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 140'.",
        "prompt": "Agent Neo, do you wish to decrypt node 20 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0021", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0022", "xp": 5}
        ]
    },
    "CH7_NODE_0021": {
        "id": "CH7_NODE_0021",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 21 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 147'.",
        "prompt": "Agent Neo, do you wish to decrypt node 21 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0022", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0023", "xp": 5}
        ]
    },
    "CH7_NODE_0022": {
        "id": "CH7_NODE_0022",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 22 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 154'.",
        "prompt": "Agent Neo, do you wish to decrypt node 22 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0023", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0024", "xp": 5}
        ]
    },
    "CH7_NODE_0023": {
        "id": "CH7_NODE_0023",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 23 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 161'.",
        "prompt": "Agent Neo, do you wish to decrypt node 23 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0024", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0025", "xp": 5}
        ]
    },
    "CH7_NODE_0024": {
        "id": "CH7_NODE_0024",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 24 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 168'.",
        "prompt": "Agent Neo, do you wish to decrypt node 24 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0025", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0026", "xp": 5}
        ]
    },
    "CH7_NODE_0025": {
        "id": "CH7_NODE_0025",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 25 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 175'.",
        "prompt": "Agent Neo, do you wish to decrypt node 25 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0026", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0027", "xp": 5}
        ]
    },
    "CH7_NODE_0026": {
        "id": "CH7_NODE_0026",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 26 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 182'.",
        "prompt": "Agent Neo, do you wish to decrypt node 26 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0027", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0028", "xp": 5}
        ]
    },
    "CH7_NODE_0027": {
        "id": "CH7_NODE_0027",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 27 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 189'.",
        "prompt": "Agent Neo, do you wish to decrypt node 27 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0028", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0029", "xp": 5}
        ]
    },
    "CH7_NODE_0028": {
        "id": "CH7_NODE_0028",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 28 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 196'.",
        "prompt": "Agent Neo, do you wish to decrypt node 28 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0029", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0030", "xp": 5}
        ]
    },
    "CH7_NODE_0029": {
        "id": "CH7_NODE_0029",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 29 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 203'.",
        "prompt": "Agent Neo, do you wish to decrypt node 29 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0030", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0031", "xp": 5}
        ]
    },
    "CH7_NODE_0030": {
        "id": "CH7_NODE_0030",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 30 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 210'.",
        "prompt": "Agent Neo, do you wish to decrypt node 30 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0031", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0032", "xp": 5}
        ]
    },
    "CH7_NODE_0031": {
        "id": "CH7_NODE_0031",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 31 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 217'.",
        "prompt": "Agent Neo, do you wish to decrypt node 31 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0032", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0033", "xp": 5}
        ]
    },
    "CH7_NODE_0032": {
        "id": "CH7_NODE_0032",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 32 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 224'.",
        "prompt": "Agent Neo, do you wish to decrypt node 32 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0033", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0034", "xp": 5}
        ]
    },
    "CH7_NODE_0033": {
        "id": "CH7_NODE_0033",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 33 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 231'.",
        "prompt": "Agent Neo, do you wish to decrypt node 33 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0034", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0035", "xp": 5}
        ]
    },
    "CH7_NODE_0034": {
        "id": "CH7_NODE_0034",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 34 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 238'.",
        "prompt": "Agent Neo, do you wish to decrypt node 34 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0035", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0036", "xp": 5}
        ]
    },
    "CH7_NODE_0035": {
        "id": "CH7_NODE_0035",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 35 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 245'.",
        "prompt": "Agent Neo, do you wish to decrypt node 35 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0036", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0037", "xp": 5}
        ]
    },
    "CH7_NODE_0036": {
        "id": "CH7_NODE_0036",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 36 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 252'.",
        "prompt": "Agent Neo, do you wish to decrypt node 36 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0037", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0038", "xp": 5}
        ]
    },
    "CH7_NODE_0037": {
        "id": "CH7_NODE_0037",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 37 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 259'.",
        "prompt": "Agent Neo, do you wish to decrypt node 37 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0038", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0039", "xp": 5}
        ]
    },
    "CH7_NODE_0038": {
        "id": "CH7_NODE_0038",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 38 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 266'.",
        "prompt": "Agent Neo, do you wish to decrypt node 38 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0039", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0040", "xp": 5}
        ]
    },
    "CH7_NODE_0039": {
        "id": "CH7_NODE_0039",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 39 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 273'.",
        "prompt": "Agent Neo, do you wish to decrypt node 39 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0040", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0041", "xp": 5}
        ]
    },
    "CH7_NODE_0040": {
        "id": "CH7_NODE_0040",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 40 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 280'.",
        "prompt": "Agent Neo, do you wish to decrypt node 40 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0041", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0042", "xp": 5}
        ]
    },
    "CH7_NODE_0041": {
        "id": "CH7_NODE_0041",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 41 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 287'.",
        "prompt": "Agent Neo, do you wish to decrypt node 41 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0042", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0043", "xp": 5}
        ]
    },
    "CH7_NODE_0042": {
        "id": "CH7_NODE_0042",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 42 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 294'.",
        "prompt": "Agent Neo, do you wish to decrypt node 42 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0043", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0044", "xp": 5}
        ]
    },
    "CH7_NODE_0043": {
        "id": "CH7_NODE_0043",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 43 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 301'.",
        "prompt": "Agent Neo, do you wish to decrypt node 43 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0044", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0045", "xp": 5}
        ]
    },
    "CH7_NODE_0044": {
        "id": "CH7_NODE_0044",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 44 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 308'.",
        "prompt": "Agent Neo, do you wish to decrypt node 44 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0045", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0046", "xp": 5}
        ]
    },
    "CH7_NODE_0045": {
        "id": "CH7_NODE_0045",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 45 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 315'.",
        "prompt": "Agent Neo, do you wish to decrypt node 45 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0046", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0047", "xp": 5}
        ]
    },
    "CH7_NODE_0046": {
        "id": "CH7_NODE_0046",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 46 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 322'.",
        "prompt": "Agent Neo, do you wish to decrypt node 46 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0047", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0048", "xp": 5}
        ]
    },
    "CH7_NODE_0047": {
        "id": "CH7_NODE_0047",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 47 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 329'.",
        "prompt": "Agent Neo, do you wish to decrypt node 47 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0048", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0049", "xp": 5}
        ]
    },
    "CH7_NODE_0048": {
        "id": "CH7_NODE_0048",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 48 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 336'.",
        "prompt": "Agent Neo, do you wish to decrypt node 48 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0049", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0050", "xp": 5}
        ]
    },
    "CH7_NODE_0049": {
        "id": "CH7_NODE_0049",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 49 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 343'.",
        "prompt": "Agent Neo, do you wish to decrypt node 49 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0050", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0051", "xp": 5}
        ]
    },
    "CH7_NODE_0050": {
        "id": "CH7_NODE_0050",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 50 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 350'.",
        "prompt": "Agent Neo, do you wish to decrypt node 50 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0051", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0052", "xp": 5}
        ]
    },
    "CH7_NODE_0051": {
        "id": "CH7_NODE_0051",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 51 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 357'.",
        "prompt": "Agent Neo, do you wish to decrypt node 51 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0052", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0053", "xp": 5}
        ]
    },
    "CH7_NODE_0052": {
        "id": "CH7_NODE_0052",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 52 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 364'.",
        "prompt": "Agent Neo, do you wish to decrypt node 52 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0053", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0054", "xp": 5}
        ]
    },
    "CH7_NODE_0053": {
        "id": "CH7_NODE_0053",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 53 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 371'.",
        "prompt": "Agent Neo, do you wish to decrypt node 53 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0054", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0055", "xp": 5}
        ]
    },
    "CH7_NODE_0054": {
        "id": "CH7_NODE_0054",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 54 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 378'.",
        "prompt": "Agent Neo, do you wish to decrypt node 54 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0055", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0056", "xp": 5}
        ]
    },
    "CH7_NODE_0055": {
        "id": "CH7_NODE_0055",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 55 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 385'.",
        "prompt": "Agent Neo, do you wish to decrypt node 55 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0056", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0057", "xp": 5}
        ]
    },
    "CH7_NODE_0056": {
        "id": "CH7_NODE_0056",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 56 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 392'.",
        "prompt": "Agent Neo, do you wish to decrypt node 56 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0057", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0058", "xp": 5}
        ]
    },
    "CH7_NODE_0057": {
        "id": "CH7_NODE_0057",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 57 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 399'.",
        "prompt": "Agent Neo, do you wish to decrypt node 57 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0058", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0059", "xp": 5}
        ]
    },
    "CH7_NODE_0058": {
        "id": "CH7_NODE_0058",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 58 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 406'.",
        "prompt": "Agent Neo, do you wish to decrypt node 58 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0059", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0060", "xp": 5}
        ]
    },
    "CH7_NODE_0059": {
        "id": "CH7_NODE_0059",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 59 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 413'.",
        "prompt": "Agent Neo, do you wish to decrypt node 59 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0060", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0061", "xp": 5}
        ]
    },
    "CH7_NODE_0060": {
        "id": "CH7_NODE_0060",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 60 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 420'.",
        "prompt": "Agent Neo, do you wish to decrypt node 60 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0061", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0062", "xp": 5}
        ]
    },
    "CH7_NODE_0061": {
        "id": "CH7_NODE_0061",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 61 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 427'.",
        "prompt": "Agent Neo, do you wish to decrypt node 61 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0062", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0063", "xp": 5}
        ]
    },
    "CH7_NODE_0062": {
        "id": "CH7_NODE_0062",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 62 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 434'.",
        "prompt": "Agent Neo, do you wish to decrypt node 62 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0063", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0064", "xp": 5}
        ]
    },
    "CH7_NODE_0063": {
        "id": "CH7_NODE_0063",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 63 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 441'.",
        "prompt": "Agent Neo, do you wish to decrypt node 63 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0064", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0065", "xp": 5}
        ]
    },
    "CH7_NODE_0064": {
        "id": "CH7_NODE_0064",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 64 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 448'.",
        "prompt": "Agent Neo, do you wish to decrypt node 64 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0065", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0066", "xp": 5}
        ]
    },
    "CH7_NODE_0065": {
        "id": "CH7_NODE_0065",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 65 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 455'.",
        "prompt": "Agent Neo, do you wish to decrypt node 65 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0066", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0067", "xp": 5}
        ]
    },
    "CH7_NODE_0066": {
        "id": "CH7_NODE_0066",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 66 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 462'.",
        "prompt": "Agent Neo, do you wish to decrypt node 66 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0067", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0068", "xp": 5}
        ]
    },
    "CH7_NODE_0067": {
        "id": "CH7_NODE_0067",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 67 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 469'.",
        "prompt": "Agent Neo, do you wish to decrypt node 67 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0068", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0069", "xp": 5}
        ]
    },
    "CH7_NODE_0068": {
        "id": "CH7_NODE_0068",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 68 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 476'.",
        "prompt": "Agent Neo, do you wish to decrypt node 68 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0069", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0070", "xp": 5}
        ]
    },
    "CH7_NODE_0069": {
        "id": "CH7_NODE_0069",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 69 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 483'.",
        "prompt": "Agent Neo, do you wish to decrypt node 69 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0070", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0071", "xp": 5}
        ]
    },
    "CH7_NODE_0070": {
        "id": "CH7_NODE_0070",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 70 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 490'.",
        "prompt": "Agent Neo, do you wish to decrypt node 70 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0071", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0072", "xp": 5}
        ]
    },
    "CH7_NODE_0071": {
        "id": "CH7_NODE_0071",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 71 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 497'.",
        "prompt": "Agent Neo, do you wish to decrypt node 71 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0072", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0073", "xp": 5}
        ]
    },
    "CH7_NODE_0072": {
        "id": "CH7_NODE_0072",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 72 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 504'.",
        "prompt": "Agent Neo, do you wish to decrypt node 72 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0073", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0074", "xp": 5}
        ]
    },
    "CH7_NODE_0073": {
        "id": "CH7_NODE_0073",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 73 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 511'.",
        "prompt": "Agent Neo, do you wish to decrypt node 73 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0074", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0075", "xp": 5}
        ]
    },
    "CH7_NODE_0074": {
        "id": "CH7_NODE_0074",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 74 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 518'.",
        "prompt": "Agent Neo, do you wish to decrypt node 74 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0075", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0076", "xp": 5}
        ]
    },
    "CH7_NODE_0075": {
        "id": "CH7_NODE_0075",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 75 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 525'.",
        "prompt": "Agent Neo, do you wish to decrypt node 75 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0076", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0077", "xp": 5}
        ]
    },
    "CH7_NODE_0076": {
        "id": "CH7_NODE_0076",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 76 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 532'.",
        "prompt": "Agent Neo, do you wish to decrypt node 76 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0077", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0078", "xp": 5}
        ]
    },
    "CH7_NODE_0077": {
        "id": "CH7_NODE_0077",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 77 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 539'.",
        "prompt": "Agent Neo, do you wish to decrypt node 77 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0078", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0079", "xp": 5}
        ]
    },
    "CH7_NODE_0078": {
        "id": "CH7_NODE_0078",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 78 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 546'.",
        "prompt": "Agent Neo, do you wish to decrypt node 78 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0079", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0080", "xp": 5}
        ]
    },
    "CH7_NODE_0079": {
        "id": "CH7_NODE_0079",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 79 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 553'.",
        "prompt": "Agent Neo, do you wish to decrypt node 79 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0080", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0081", "xp": 5}
        ]
    },
    "CH7_NODE_0080": {
        "id": "CH7_NODE_0080",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 80 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 560'.",
        "prompt": "Agent Neo, do you wish to decrypt node 80 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0081", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0082", "xp": 5}
        ]
    },
    "CH7_NODE_0081": {
        "id": "CH7_NODE_0081",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 81 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 567'.",
        "prompt": "Agent Neo, do you wish to decrypt node 81 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0082", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0083", "xp": 5}
        ]
    },
    "CH7_NODE_0082": {
        "id": "CH7_NODE_0082",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 82 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 574'.",
        "prompt": "Agent Neo, do you wish to decrypt node 82 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0083", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0084", "xp": 5}
        ]
    },
    "CH7_NODE_0083": {
        "id": "CH7_NODE_0083",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 83 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 581'.",
        "prompt": "Agent Neo, do you wish to decrypt node 83 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0084", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0085", "xp": 5}
        ]
    },
    "CH7_NODE_0084": {
        "id": "CH7_NODE_0084",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 84 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 588'.",
        "prompt": "Agent Neo, do you wish to decrypt node 84 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0085", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0086", "xp": 5}
        ]
    },
    "CH7_NODE_0085": {
        "id": "CH7_NODE_0085",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 85 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 595'.",
        "prompt": "Agent Neo, do you wish to decrypt node 85 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0086", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0087", "xp": 5}
        ]
    },
    "CH7_NODE_0086": {
        "id": "CH7_NODE_0086",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 86 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 602'.",
        "prompt": "Agent Neo, do you wish to decrypt node 86 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0087", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0088", "xp": 5}
        ]
    },
    "CH7_NODE_0087": {
        "id": "CH7_NODE_0087",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 87 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 609'.",
        "prompt": "Agent Neo, do you wish to decrypt node 87 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0088", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0089", "xp": 5}
        ]
    },
    "CH7_NODE_0088": {
        "id": "CH7_NODE_0088",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 88 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 616'.",
        "prompt": "Agent Neo, do you wish to decrypt node 88 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0089", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0090", "xp": 5}
        ]
    },
    "CH7_NODE_0089": {
        "id": "CH7_NODE_0089",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 89 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 623'.",
        "prompt": "Agent Neo, do you wish to decrypt node 89 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0090", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0091", "xp": 5}
        ]
    },
    "CH7_NODE_0090": {
        "id": "CH7_NODE_0090",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 90 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 630'.",
        "prompt": "Agent Neo, do you wish to decrypt node 90 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0091", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0092", "xp": 5}
        ]
    },
    "CH7_NODE_0091": {
        "id": "CH7_NODE_0091",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 91 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 637'.",
        "prompt": "Agent Neo, do you wish to decrypt node 91 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0092", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0093", "xp": 5}
        ]
    },
    "CH7_NODE_0092": {
        "id": "CH7_NODE_0092",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 92 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 644'.",
        "prompt": "Agent Neo, do you wish to decrypt node 92 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0093", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0094", "xp": 5}
        ]
    },
    "CH7_NODE_0093": {
        "id": "CH7_NODE_0093",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 93 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 651'.",
        "prompt": "Agent Neo, do you wish to decrypt node 93 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0094", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0095", "xp": 5}
        ]
    },
    "CH7_NODE_0094": {
        "id": "CH7_NODE_0094",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 94 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 658'.",
        "prompt": "Agent Neo, do you wish to decrypt node 94 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0095", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0096", "xp": 5}
        ]
    },
    "CH7_NODE_0095": {
        "id": "CH7_NODE_0095",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 95 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 665'.",
        "prompt": "Agent Neo, do you wish to decrypt node 95 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0096", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0097", "xp": 5}
        ]
    },
    "CH7_NODE_0096": {
        "id": "CH7_NODE_0096",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 96 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 672'.",
        "prompt": "Agent Neo, do you wish to decrypt node 96 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0097", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0098", "xp": 5}
        ]
    },
    "CH7_NODE_0097": {
        "id": "CH7_NODE_0097",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 97 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 679'.",
        "prompt": "Agent Neo, do you wish to decrypt node 97 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0098", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0099", "xp": 5}
        ]
    },
    "CH7_NODE_0098": {
        "id": "CH7_NODE_0098",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 98 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 686'.",
        "prompt": "Agent Neo, do you wish to decrypt node 98 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0099", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0100", "xp": 5}
        ]
    },
    "CH7_NODE_0099": {
        "id": "CH7_NODE_0099",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 99 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 693'.",
        "prompt": "Agent Neo, do you wish to decrypt node 99 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0100", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0101", "xp": 5}
        ]
    },
    "CH7_NODE_0100": {
        "id": "CH7_NODE_0100",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 100 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 700'.",
        "prompt": "Agent Neo, do you wish to decrypt node 100 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0101", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0102", "xp": 5}
        ]
    },
    "CH7_NODE_0101": {
        "id": "CH7_NODE_0101",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 101 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 707'.",
        "prompt": "Agent Neo, do you wish to decrypt node 101 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0102", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0103", "xp": 5}
        ]
    },
    "CH7_NODE_0102": {
        "id": "CH7_NODE_0102",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 102 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 714'.",
        "prompt": "Agent Neo, do you wish to decrypt node 102 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0103", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0104", "xp": 5}
        ]
    },
    "CH7_NODE_0103": {
        "id": "CH7_NODE_0103",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 103 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 721'.",
        "prompt": "Agent Neo, do you wish to decrypt node 103 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0104", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0105", "xp": 5}
        ]
    },
    "CH7_NODE_0104": {
        "id": "CH7_NODE_0104",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 104 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 728'.",
        "prompt": "Agent Neo, do you wish to decrypt node 104 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0105", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0106", "xp": 5}
        ]
    },
    "CH7_NODE_0105": {
        "id": "CH7_NODE_0105",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 105 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 735'.",
        "prompt": "Agent Neo, do you wish to decrypt node 105 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0106", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0107", "xp": 5}
        ]
    },
    "CH7_NODE_0106": {
        "id": "CH7_NODE_0106",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 106 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 742'.",
        "prompt": "Agent Neo, do you wish to decrypt node 106 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0107", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0108", "xp": 5}
        ]
    },
    "CH7_NODE_0107": {
        "id": "CH7_NODE_0107",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 107 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 749'.",
        "prompt": "Agent Neo, do you wish to decrypt node 107 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0108", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0109", "xp": 5}
        ]
    },
    "CH7_NODE_0108": {
        "id": "CH7_NODE_0108",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 108 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 756'.",
        "prompt": "Agent Neo, do you wish to decrypt node 108 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0109", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0110", "xp": 5}
        ]
    },
    "CH7_NODE_0109": {
        "id": "CH7_NODE_0109",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 109 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 763'.",
        "prompt": "Agent Neo, do you wish to decrypt node 109 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0110", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0111", "xp": 5}
        ]
    },
    "CH7_NODE_0110": {
        "id": "CH7_NODE_0110",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 110 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 770'.",
        "prompt": "Agent Neo, do you wish to decrypt node 110 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0111", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0112", "xp": 5}
        ]
    },
    "CH7_NODE_0111": {
        "id": "CH7_NODE_0111",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 111 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 777'.",
        "prompt": "Agent Neo, do you wish to decrypt node 111 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0112", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0113", "xp": 5}
        ]
    },
    "CH7_NODE_0112": {
        "id": "CH7_NODE_0112",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 112 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 784'.",
        "prompt": "Agent Neo, do you wish to decrypt node 112 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0113", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0114", "xp": 5}
        ]
    },
    "CH7_NODE_0113": {
        "id": "CH7_NODE_0113",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 113 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 791'.",
        "prompt": "Agent Neo, do you wish to decrypt node 113 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0114", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0115", "xp": 5}
        ]
    },
    "CH7_NODE_0114": {
        "id": "CH7_NODE_0114",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 114 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 798'.",
        "prompt": "Agent Neo, do you wish to decrypt node 114 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0115", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0116", "xp": 5}
        ]
    },
    "CH7_NODE_0115": {
        "id": "CH7_NODE_0115",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 115 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 805'.",
        "prompt": "Agent Neo, do you wish to decrypt node 115 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0116", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0117", "xp": 5}
        ]
    },
    "CH7_NODE_0116": {
        "id": "CH7_NODE_0116",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 116 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 812'.",
        "prompt": "Agent Neo, do you wish to decrypt node 116 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0117", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0118", "xp": 5}
        ]
    },
    "CH7_NODE_0117": {
        "id": "CH7_NODE_0117",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 117 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 819'.",
        "prompt": "Agent Neo, do you wish to decrypt node 117 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0118", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0119", "xp": 5}
        ]
    },
    "CH7_NODE_0118": {
        "id": "CH7_NODE_0118",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 118 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 826'.",
        "prompt": "Agent Neo, do you wish to decrypt node 118 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0119", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0120", "xp": 5}
        ]
    },
    "CH7_NODE_0119": {
        "id": "CH7_NODE_0119",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 119 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 833'.",
        "prompt": "Agent Neo, do you wish to decrypt node 119 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0120", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0121", "xp": 5}
        ]
    },
    "CH7_NODE_0120": {
        "id": "CH7_NODE_0120",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 120 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 840'.",
        "prompt": "Agent Neo, do you wish to decrypt node 120 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0121", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0122", "xp": 5}
        ]
    },
    "CH7_NODE_0121": {
        "id": "CH7_NODE_0121",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 121 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 847'.",
        "prompt": "Agent Neo, do you wish to decrypt node 121 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0122", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0123", "xp": 5}
        ]
    },
    "CH7_NODE_0122": {
        "id": "CH7_NODE_0122",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 122 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 854'.",
        "prompt": "Agent Neo, do you wish to decrypt node 122 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0123", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0124", "xp": 5}
        ]
    },
    "CH7_NODE_0123": {
        "id": "CH7_NODE_0123",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 123 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 861'.",
        "prompt": "Agent Neo, do you wish to decrypt node 123 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0124", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0125", "xp": 5}
        ]
    },
    "CH7_NODE_0124": {
        "id": "CH7_NODE_0124",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 124 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 868'.",
        "prompt": "Agent Neo, do you wish to decrypt node 124 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0125", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0126", "xp": 5}
        ]
    },
    "CH7_NODE_0125": {
        "id": "CH7_NODE_0125",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 125 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 875'.",
        "prompt": "Agent Neo, do you wish to decrypt node 125 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0126", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0127", "xp": 5}
        ]
    },
    "CH7_NODE_0126": {
        "id": "CH7_NODE_0126",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 126 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 882'.",
        "prompt": "Agent Neo, do you wish to decrypt node 126 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0127", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0128", "xp": 5}
        ]
    },
    "CH7_NODE_0127": {
        "id": "CH7_NODE_0127",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 127 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 889'.",
        "prompt": "Agent Neo, do you wish to decrypt node 127 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0128", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0129", "xp": 5}
        ]
    },
    "CH7_NODE_0128": {
        "id": "CH7_NODE_0128",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 128 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 896'.",
        "prompt": "Agent Neo, do you wish to decrypt node 128 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0129", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0130", "xp": 5}
        ]
    },
    "CH7_NODE_0129": {
        "id": "CH7_NODE_0129",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 129 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 903'.",
        "prompt": "Agent Neo, do you wish to decrypt node 129 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0130", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0131", "xp": 5}
        ]
    },
    "CH7_NODE_0130": {
        "id": "CH7_NODE_0130",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 130 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 910'.",
        "prompt": "Agent Neo, do you wish to decrypt node 130 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0131", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0132", "xp": 5}
        ]
    },
    "CH7_NODE_0131": {
        "id": "CH7_NODE_0131",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 131 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 917'.",
        "prompt": "Agent Neo, do you wish to decrypt node 131 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0132", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0133", "xp": 5}
        ]
    },
    "CH7_NODE_0132": {
        "id": "CH7_NODE_0132",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 132 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 924'.",
        "prompt": "Agent Neo, do you wish to decrypt node 132 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0133", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0134", "xp": 5}
        ]
    },
    "CH7_NODE_0133": {
        "id": "CH7_NODE_0133",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 133 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 931'.",
        "prompt": "Agent Neo, do you wish to decrypt node 133 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0134", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0135", "xp": 5}
        ]
    },
    "CH7_NODE_0134": {
        "id": "CH7_NODE_0134",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 134 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 938'.",
        "prompt": "Agent Neo, do you wish to decrypt node 134 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0135", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0136", "xp": 5}
        ]
    },
    "CH7_NODE_0135": {
        "id": "CH7_NODE_0135",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 135 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 945'.",
        "prompt": "Agent Neo, do you wish to decrypt node 135 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0136", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0137", "xp": 5}
        ]
    },
    "CH7_NODE_0136": {
        "id": "CH7_NODE_0136",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 136 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 952'.",
        "prompt": "Agent Neo, do you wish to decrypt node 136 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0137", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0138", "xp": 5}
        ]
    },
    "CH7_NODE_0137": {
        "id": "CH7_NODE_0137",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 137 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 959'.",
        "prompt": "Agent Neo, do you wish to decrypt node 137 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0138", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0139", "xp": 5}
        ]
    },
    "CH7_NODE_0138": {
        "id": "CH7_NODE_0138",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 138 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 966'.",
        "prompt": "Agent Neo, do you wish to decrypt node 138 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0139", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0140", "xp": 5}
        ]
    },
    "CH7_NODE_0139": {
        "id": "CH7_NODE_0139",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 139 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 973'.",
        "prompt": "Agent Neo, do you wish to decrypt node 139 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0140", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0141", "xp": 5}
        ]
    },
    "CH7_NODE_0140": {
        "id": "CH7_NODE_0140",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 140 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 980'.",
        "prompt": "Agent Neo, do you wish to decrypt node 140 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0141", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0142", "xp": 5}
        ]
    },
    "CH7_NODE_0141": {
        "id": "CH7_NODE_0141",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 141 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 987'.",
        "prompt": "Agent Neo, do you wish to decrypt node 141 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0142", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0143", "xp": 5}
        ]
    },
    "CH7_NODE_0142": {
        "id": "CH7_NODE_0142",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 142 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 994'.",
        "prompt": "Agent Neo, do you wish to decrypt node 142 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0143", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0144", "xp": 5}
        ]
    },
    "CH7_NODE_0143": {
        "id": "CH7_NODE_0143",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 143 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1001'.",
        "prompt": "Agent Neo, do you wish to decrypt node 143 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0144", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0145", "xp": 5}
        ]
    },
    "CH7_NODE_0144": {
        "id": "CH7_NODE_0144",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 144 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1008'.",
        "prompt": "Agent Neo, do you wish to decrypt node 144 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0145", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0146", "xp": 5}
        ]
    },
    "CH7_NODE_0145": {
        "id": "CH7_NODE_0145",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 145 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1015'.",
        "prompt": "Agent Neo, do you wish to decrypt node 145 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0146", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0147", "xp": 5}
        ]
    },
    "CH7_NODE_0146": {
        "id": "CH7_NODE_0146",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 146 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1022'.",
        "prompt": "Agent Neo, do you wish to decrypt node 146 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0147", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0148", "xp": 5}
        ]
    },
    "CH7_NODE_0147": {
        "id": "CH7_NODE_0147",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 147 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1029'.",
        "prompt": "Agent Neo, do you wish to decrypt node 147 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0148", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0149", "xp": 5}
        ]
    },
    "CH7_NODE_0148": {
        "id": "CH7_NODE_0148",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 148 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1036'.",
        "prompt": "Agent Neo, do you wish to decrypt node 148 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0149", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0150", "xp": 5}
        ]
    },
    "CH7_NODE_0149": {
        "id": "CH7_NODE_0149",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 149 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1043'.",
        "prompt": "Agent Neo, do you wish to decrypt node 149 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0150", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0151", "xp": 5}
        ]
    },
    "CH7_NODE_0150": {
        "id": "CH7_NODE_0150",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 150 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1050'.",
        "prompt": "Agent Neo, do you wish to decrypt node 150 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0151", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0152", "xp": 5}
        ]
    },
    "CH7_NODE_0151": {
        "id": "CH7_NODE_0151",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 151 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1057'.",
        "prompt": "Agent Neo, do you wish to decrypt node 151 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0152", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0153", "xp": 5}
        ]
    },
    "CH7_NODE_0152": {
        "id": "CH7_NODE_0152",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 152 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1064'.",
        "prompt": "Agent Neo, do you wish to decrypt node 152 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0153", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0154", "xp": 5}
        ]
    },
    "CH7_NODE_0153": {
        "id": "CH7_NODE_0153",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 153 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1071'.",
        "prompt": "Agent Neo, do you wish to decrypt node 153 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0154", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0155", "xp": 5}
        ]
    },
    "CH7_NODE_0154": {
        "id": "CH7_NODE_0154",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 154 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1078'.",
        "prompt": "Agent Neo, do you wish to decrypt node 154 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0155", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0156", "xp": 5}
        ]
    },
    "CH7_NODE_0155": {
        "id": "CH7_NODE_0155",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 155 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1085'.",
        "prompt": "Agent Neo, do you wish to decrypt node 155 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0156", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0157", "xp": 5}
        ]
    },
    "CH7_NODE_0156": {
        "id": "CH7_NODE_0156",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 156 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1092'.",
        "prompt": "Agent Neo, do you wish to decrypt node 156 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0157", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0158", "xp": 5}
        ]
    },
    "CH7_NODE_0157": {
        "id": "CH7_NODE_0157",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 157 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1099'.",
        "prompt": "Agent Neo, do you wish to decrypt node 157 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0158", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0159", "xp": 5}
        ]
    },
    "CH7_NODE_0158": {
        "id": "CH7_NODE_0158",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 158 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1106'.",
        "prompt": "Agent Neo, do you wish to decrypt node 158 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0159", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0160", "xp": 5}
        ]
    },
    "CH7_NODE_0159": {
        "id": "CH7_NODE_0159",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 159 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1113'.",
        "prompt": "Agent Neo, do you wish to decrypt node 159 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0160", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0161", "xp": 5}
        ]
    },
    "CH7_NODE_0160": {
        "id": "CH7_NODE_0160",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 160 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1120'.",
        "prompt": "Agent Neo, do you wish to decrypt node 160 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0161", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0162", "xp": 5}
        ]
    },
    "CH7_NODE_0161": {
        "id": "CH7_NODE_0161",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 161 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1127'.",
        "prompt": "Agent Neo, do you wish to decrypt node 161 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0162", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0163", "xp": 5}
        ]
    },
    "CH7_NODE_0162": {
        "id": "CH7_NODE_0162",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 162 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1134'.",
        "prompt": "Agent Neo, do you wish to decrypt node 162 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0163", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0164", "xp": 5}
        ]
    },
    "CH7_NODE_0163": {
        "id": "CH7_NODE_0163",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 163 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1141'.",
        "prompt": "Agent Neo, do you wish to decrypt node 163 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0164", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0165", "xp": 5}
        ]
    },
    "CH7_NODE_0164": {
        "id": "CH7_NODE_0164",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 164 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1148'.",
        "prompt": "Agent Neo, do you wish to decrypt node 164 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0165", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0166", "xp": 5}
        ]
    },
    "CH7_NODE_0165": {
        "id": "CH7_NODE_0165",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 165 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1155'.",
        "prompt": "Agent Neo, do you wish to decrypt node 165 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0166", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0167", "xp": 5}
        ]
    },
    "CH7_NODE_0166": {
        "id": "CH7_NODE_0166",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 166 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1162'.",
        "prompt": "Agent Neo, do you wish to decrypt node 166 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0167", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0168", "xp": 5}
        ]
    },
    "CH7_NODE_0167": {
        "id": "CH7_NODE_0167",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 167 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1169'.",
        "prompt": "Agent Neo, do you wish to decrypt node 167 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0168", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0169", "xp": 5}
        ]
    },
    "CH7_NODE_0168": {
        "id": "CH7_NODE_0168",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 168 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1176'.",
        "prompt": "Agent Neo, do you wish to decrypt node 168 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0169", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0170", "xp": 5}
        ]
    },
    "CH7_NODE_0169": {
        "id": "CH7_NODE_0169",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 169 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1183'.",
        "prompt": "Agent Neo, do you wish to decrypt node 169 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0170", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0171", "xp": 5}
        ]
    },
    "CH7_NODE_0170": {
        "id": "CH7_NODE_0170",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 170 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1190'.",
        "prompt": "Agent Neo, do you wish to decrypt node 170 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0171", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0172", "xp": 5}
        ]
    },
    "CH7_NODE_0171": {
        "id": "CH7_NODE_0171",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 171 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1197'.",
        "prompt": "Agent Neo, do you wish to decrypt node 171 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0172", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0173", "xp": 5}
        ]
    },
    "CH7_NODE_0172": {
        "id": "CH7_NODE_0172",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 172 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1204'.",
        "prompt": "Agent Neo, do you wish to decrypt node 172 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0173", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0174", "xp": 5}
        ]
    },
    "CH7_NODE_0173": {
        "id": "CH7_NODE_0173",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 173 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1211'.",
        "prompt": "Agent Neo, do you wish to decrypt node 173 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0174", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0175", "xp": 5}
        ]
    },
    "CH7_NODE_0174": {
        "id": "CH7_NODE_0174",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 174 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1218'.",
        "prompt": "Agent Neo, do you wish to decrypt node 174 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0175", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0176", "xp": 5}
        ]
    },
    "CH7_NODE_0175": {
        "id": "CH7_NODE_0175",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 175 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1225'.",
        "prompt": "Agent Neo, do you wish to decrypt node 175 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0176", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0177", "xp": 5}
        ]
    },
    "CH7_NODE_0176": {
        "id": "CH7_NODE_0176",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 176 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1232'.",
        "prompt": "Agent Neo, do you wish to decrypt node 176 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0177", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0178", "xp": 5}
        ]
    },
    "CH7_NODE_0177": {
        "id": "CH7_NODE_0177",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 177 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1239'.",
        "prompt": "Agent Neo, do you wish to decrypt node 177 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0178", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0179", "xp": 5}
        ]
    },
    "CH7_NODE_0178": {
        "id": "CH7_NODE_0178",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 178 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1246'.",
        "prompt": "Agent Neo, do you wish to decrypt node 178 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0179", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0180", "xp": 5}
        ]
    },
    "CH7_NODE_0179": {
        "id": "CH7_NODE_0179",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 179 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1253'.",
        "prompt": "Agent Neo, do you wish to decrypt node 179 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0180", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0181", "xp": 5}
        ]
    },
    "CH7_NODE_0180": {
        "id": "CH7_NODE_0180",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 180 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1260'.",
        "prompt": "Agent Neo, do you wish to decrypt node 180 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0181", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0182", "xp": 5}
        ]
    },
    "CH7_NODE_0181": {
        "id": "CH7_NODE_0181",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 181 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1267'.",
        "prompt": "Agent Neo, do you wish to decrypt node 181 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0182", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0183", "xp": 5}
        ]
    },
    "CH7_NODE_0182": {
        "id": "CH7_NODE_0182",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 182 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1274'.",
        "prompt": "Agent Neo, do you wish to decrypt node 182 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0183", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0184", "xp": 5}
        ]
    },
    "CH7_NODE_0183": {
        "id": "CH7_NODE_0183",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 183 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1281'.",
        "prompt": "Agent Neo, do you wish to decrypt node 183 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0184", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0185", "xp": 5}
        ]
    },
    "CH7_NODE_0184": {
        "id": "CH7_NODE_0184",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 184 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1288'.",
        "prompt": "Agent Neo, do you wish to decrypt node 184 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0185", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0186", "xp": 5}
        ]
    },
    "CH7_NODE_0185": {
        "id": "CH7_NODE_0185",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 185 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1295'.",
        "prompt": "Agent Neo, do you wish to decrypt node 185 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0186", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0187", "xp": 5}
        ]
    },
    "CH7_NODE_0186": {
        "id": "CH7_NODE_0186",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 186 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1302'.",
        "prompt": "Agent Neo, do you wish to decrypt node 186 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0187", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0188", "xp": 5}
        ]
    },
    "CH7_NODE_0187": {
        "id": "CH7_NODE_0187",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 187 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1309'.",
        "prompt": "Agent Neo, do you wish to decrypt node 187 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0188", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0189", "xp": 5}
        ]
    },
    "CH7_NODE_0188": {
        "id": "CH7_NODE_0188",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 188 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1316'.",
        "prompt": "Agent Neo, do you wish to decrypt node 188 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0189", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0190", "xp": 5}
        ]
    },
    "CH7_NODE_0189": {
        "id": "CH7_NODE_0189",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 189 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1323'.",
        "prompt": "Agent Neo, do you wish to decrypt node 189 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0190", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0191", "xp": 5}
        ]
    },
    "CH7_NODE_0190": {
        "id": "CH7_NODE_0190",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 190 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1330'.",
        "prompt": "Agent Neo, do you wish to decrypt node 190 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0191", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0192", "xp": 5}
        ]
    },
    "CH7_NODE_0191": {
        "id": "CH7_NODE_0191",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 191 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1337'.",
        "prompt": "Agent Neo, do you wish to decrypt node 191 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0192", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0193", "xp": 5}
        ]
    },
    "CH7_NODE_0192": {
        "id": "CH7_NODE_0192",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 192 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1344'.",
        "prompt": "Agent Neo, do you wish to decrypt node 192 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0193", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0194", "xp": 5}
        ]
    },
    "CH7_NODE_0193": {
        "id": "CH7_NODE_0193",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 193 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1351'.",
        "prompt": "Agent Neo, do you wish to decrypt node 193 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0194", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0195", "xp": 5}
        ]
    },
    "CH7_NODE_0194": {
        "id": "CH7_NODE_0194",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 194 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1358'.",
        "prompt": "Agent Neo, do you wish to decrypt node 194 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0195", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0196", "xp": 5}
        ]
    },
    "CH7_NODE_0195": {
        "id": "CH7_NODE_0195",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 195 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1365'.",
        "prompt": "Agent Neo, do you wish to decrypt node 195 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0196", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0197", "xp": 5}
        ]
    },
    "CH7_NODE_0196": {
        "id": "CH7_NODE_0196",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 196 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1372'.",
        "prompt": "Agent Neo, do you wish to decrypt node 196 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0197", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0198", "xp": 5}
        ]
    },
    "CH7_NODE_0197": {
        "id": "CH7_NODE_0197",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 197 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1379'.",
        "prompt": "Agent Neo, do you wish to decrypt node 197 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0198", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0199", "xp": 5}
        ]
    },
    "CH7_NODE_0198": {
        "id": "CH7_NODE_0198",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 198 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1386'.",
        "prompt": "Agent Neo, do you wish to decrypt node 198 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0199", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0200", "xp": 5}
        ]
    },
    "CH7_NODE_0199": {
        "id": "CH7_NODE_0199",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 199 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1393'.",
        "prompt": "Agent Neo, do you wish to decrypt node 199 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0200", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0201", "xp": 5}
        ]
    },
    "CH7_NODE_0200": {
        "id": "CH7_NODE_0200",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 200 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1400'.",
        "prompt": "Agent Neo, do you wish to decrypt node 200 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0201", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0202", "xp": 5}
        ]
    },
    "CH7_NODE_0201": {
        "id": "CH7_NODE_0201",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 201 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1407'.",
        "prompt": "Agent Neo, do you wish to decrypt node 201 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0202", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0203", "xp": 5}
        ]
    },
    "CH7_NODE_0202": {
        "id": "CH7_NODE_0202",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 202 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1414'.",
        "prompt": "Agent Neo, do you wish to decrypt node 202 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0203", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0204", "xp": 5}
        ]
    },
    "CH7_NODE_0203": {
        "id": "CH7_NODE_0203",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 203 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1421'.",
        "prompt": "Agent Neo, do you wish to decrypt node 203 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0204", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0205", "xp": 5}
        ]
    },
    "CH7_NODE_0204": {
        "id": "CH7_NODE_0204",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 204 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1428'.",
        "prompt": "Agent Neo, do you wish to decrypt node 204 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0205", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0206", "xp": 5}
        ]
    },
    "CH7_NODE_0205": {
        "id": "CH7_NODE_0205",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 205 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1435'.",
        "prompt": "Agent Neo, do you wish to decrypt node 205 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0206", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0207", "xp": 5}
        ]
    },
    "CH7_NODE_0206": {
        "id": "CH7_NODE_0206",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 206 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1442'.",
        "prompt": "Agent Neo, do you wish to decrypt node 206 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0207", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0208", "xp": 5}
        ]
    },
    "CH7_NODE_0207": {
        "id": "CH7_NODE_0207",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 207 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1449'.",
        "prompt": "Agent Neo, do you wish to decrypt node 207 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0208", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0209", "xp": 5}
        ]
    },
    "CH7_NODE_0208": {
        "id": "CH7_NODE_0208",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 208 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1456'.",
        "prompt": "Agent Neo, do you wish to decrypt node 208 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0209", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0210", "xp": 5}
        ]
    },
    "CH7_NODE_0209": {
        "id": "CH7_NODE_0209",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 209 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1463'.",
        "prompt": "Agent Neo, do you wish to decrypt node 209 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0210", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0211", "xp": 5}
        ]
    },
    "CH7_NODE_0210": {
        "id": "CH7_NODE_0210",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 210 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1470'.",
        "prompt": "Agent Neo, do you wish to decrypt node 210 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0211", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0212", "xp": 5}
        ]
    },
    "CH7_NODE_0211": {
        "id": "CH7_NODE_0211",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 211 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1477'.",
        "prompt": "Agent Neo, do you wish to decrypt node 211 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0212", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0213", "xp": 5}
        ]
    },
    "CH7_NODE_0212": {
        "id": "CH7_NODE_0212",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 212 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1484'.",
        "prompt": "Agent Neo, do you wish to decrypt node 212 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0213", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0214", "xp": 5}
        ]
    },
    "CH7_NODE_0213": {
        "id": "CH7_NODE_0213",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 213 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1491'.",
        "prompt": "Agent Neo, do you wish to decrypt node 213 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0214", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0215", "xp": 5}
        ]
    },
    "CH7_NODE_0214": {
        "id": "CH7_NODE_0214",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 214 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1498'.",
        "prompt": "Agent Neo, do you wish to decrypt node 214 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0215", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0216", "xp": 5}
        ]
    },
    "CH7_NODE_0215": {
        "id": "CH7_NODE_0215",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 215 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1505'.",
        "prompt": "Agent Neo, do you wish to decrypt node 215 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0216", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0217", "xp": 5}
        ]
    },
    "CH7_NODE_0216": {
        "id": "CH7_NODE_0216",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 216 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1512'.",
        "prompt": "Agent Neo, do you wish to decrypt node 216 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0217", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0218", "xp": 5}
        ]
    },
    "CH7_NODE_0217": {
        "id": "CH7_NODE_0217",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 217 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1519'.",
        "prompt": "Agent Neo, do you wish to decrypt node 217 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0218", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0219", "xp": 5}
        ]
    },
    "CH7_NODE_0218": {
        "id": "CH7_NODE_0218",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 218 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1526'.",
        "prompt": "Agent Neo, do you wish to decrypt node 218 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0219", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0220", "xp": 5}
        ]
    },
    "CH7_NODE_0219": {
        "id": "CH7_NODE_0219",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 219 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1533'.",
        "prompt": "Agent Neo, do you wish to decrypt node 219 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0220", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0221", "xp": 5}
        ]
    },
    "CH7_NODE_0220": {
        "id": "CH7_NODE_0220",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 220 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1540'.",
        "prompt": "Agent Neo, do you wish to decrypt node 220 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0221", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0222", "xp": 5}
        ]
    },
    "CH7_NODE_0221": {
        "id": "CH7_NODE_0221",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 221 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1547'.",
        "prompt": "Agent Neo, do you wish to decrypt node 221 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0222", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0223", "xp": 5}
        ]
    },
    "CH7_NODE_0222": {
        "id": "CH7_NODE_0222",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 222 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1554'.",
        "prompt": "Agent Neo, do you wish to decrypt node 222 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0223", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0224", "xp": 5}
        ]
    },
    "CH7_NODE_0223": {
        "id": "CH7_NODE_0223",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 223 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1561'.",
        "prompt": "Agent Neo, do you wish to decrypt node 223 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0224", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0225", "xp": 5}
        ]
    },
    "CH7_NODE_0224": {
        "id": "CH7_NODE_0224",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 224 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1568'.",
        "prompt": "Agent Neo, do you wish to decrypt node 224 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0225", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0226", "xp": 5}
        ]
    },
    "CH7_NODE_0225": {
        "id": "CH7_NODE_0225",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 225 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1575'.",
        "prompt": "Agent Neo, do you wish to decrypt node 225 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0226", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0227", "xp": 5}
        ]
    },
    "CH7_NODE_0226": {
        "id": "CH7_NODE_0226",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 226 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1582'.",
        "prompt": "Agent Neo, do you wish to decrypt node 226 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0227", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0228", "xp": 5}
        ]
    },
    "CH7_NODE_0227": {
        "id": "CH7_NODE_0227",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 227 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1589'.",
        "prompt": "Agent Neo, do you wish to decrypt node 227 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0228", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0229", "xp": 5}
        ]
    },
    "CH7_NODE_0228": {
        "id": "CH7_NODE_0228",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 228 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1596'.",
        "prompt": "Agent Neo, do you wish to decrypt node 228 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0229", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0230", "xp": 5}
        ]
    },
    "CH7_NODE_0229": {
        "id": "CH7_NODE_0229",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 229 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1603'.",
        "prompt": "Agent Neo, do you wish to decrypt node 229 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0230", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0231", "xp": 5}
        ]
    },
    "CH7_NODE_0230": {
        "id": "CH7_NODE_0230",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 230 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1610'.",
        "prompt": "Agent Neo, do you wish to decrypt node 230 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0231", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0232", "xp": 5}
        ]
    },
    "CH7_NODE_0231": {
        "id": "CH7_NODE_0231",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 231 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1617'.",
        "prompt": "Agent Neo, do you wish to decrypt node 231 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0232", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0233", "xp": 5}
        ]
    },
    "CH7_NODE_0232": {
        "id": "CH7_NODE_0232",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 232 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1624'.",
        "prompt": "Agent Neo, do you wish to decrypt node 232 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0233", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0234", "xp": 5}
        ]
    },
    "CH7_NODE_0233": {
        "id": "CH7_NODE_0233",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 233 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1631'.",
        "prompt": "Agent Neo, do you wish to decrypt node 233 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0234", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0235", "xp": 5}
        ]
    },
    "CH7_NODE_0234": {
        "id": "CH7_NODE_0234",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 234 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1638'.",
        "prompt": "Agent Neo, do you wish to decrypt node 234 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0235", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0236", "xp": 5}
        ]
    },
    "CH7_NODE_0235": {
        "id": "CH7_NODE_0235",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 235 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1645'.",
        "prompt": "Agent Neo, do you wish to decrypt node 235 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0236", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0237", "xp": 5}
        ]
    },
    "CH7_NODE_0236": {
        "id": "CH7_NODE_0236",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 236 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1652'.",
        "prompt": "Agent Neo, do you wish to decrypt node 236 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0237", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0238", "xp": 5}
        ]
    },
    "CH7_NODE_0237": {
        "id": "CH7_NODE_0237",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 237 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1659'.",
        "prompt": "Agent Neo, do you wish to decrypt node 237 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0238", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0239", "xp": 5}
        ]
    },
    "CH7_NODE_0238": {
        "id": "CH7_NODE_0238",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 238 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1666'.",
        "prompt": "Agent Neo, do you wish to decrypt node 238 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0239", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0240", "xp": 5}
        ]
    },
    "CH7_NODE_0239": {
        "id": "CH7_NODE_0239",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 239 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1673'.",
        "prompt": "Agent Neo, do you wish to decrypt node 239 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0240", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0241", "xp": 5}
        ]
    },
    "CH7_NODE_0240": {
        "id": "CH7_NODE_0240",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 240 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1680'.",
        "prompt": "Agent Neo, do you wish to decrypt node 240 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0241", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0242", "xp": 5}
        ]
    },
    "CH7_NODE_0241": {
        "id": "CH7_NODE_0241",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 241 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1687'.",
        "prompt": "Agent Neo, do you wish to decrypt node 241 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0242", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0243", "xp": 5}
        ]
    },
    "CH7_NODE_0242": {
        "id": "CH7_NODE_0242",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 242 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1694'.",
        "prompt": "Agent Neo, do you wish to decrypt node 242 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0243", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0244", "xp": 5}
        ]
    },
    "CH7_NODE_0243": {
        "id": "CH7_NODE_0243",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 243 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1701'.",
        "prompt": "Agent Neo, do you wish to decrypt node 243 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0244", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0245", "xp": 5}
        ]
    },
    "CH7_NODE_0244": {
        "id": "CH7_NODE_0244",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 244 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1708'.",
        "prompt": "Agent Neo, do you wish to decrypt node 244 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0245", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0246", "xp": 5}
        ]
    },
    "CH7_NODE_0245": {
        "id": "CH7_NODE_0245",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 245 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1715'.",
        "prompt": "Agent Neo, do you wish to decrypt node 245 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0246", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0247", "xp": 5}
        ]
    },
    "CH7_NODE_0246": {
        "id": "CH7_NODE_0246",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 246 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1722'.",
        "prompt": "Agent Neo, do you wish to decrypt node 246 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0247", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0248", "xp": 5}
        ]
    },
    "CH7_NODE_0247": {
        "id": "CH7_NODE_0247",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 247 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1729'.",
        "prompt": "Agent Neo, do you wish to decrypt node 247 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0248", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0249", "xp": 5}
        ]
    },
    "CH7_NODE_0248": {
        "id": "CH7_NODE_0248",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 248 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1736'.",
        "prompt": "Agent Neo, do you wish to decrypt node 248 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0249", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0250", "xp": 5}
        ]
    },
    "CH7_NODE_0249": {
        "id": "CH7_NODE_0249",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 249 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1743'.",
        "prompt": "Agent Neo, do you wish to decrypt node 249 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0250", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0251", "xp": 5}
        ]
    },
    "CH7_NODE_0250": {
        "id": "CH7_NODE_0250",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 250 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1750'.",
        "prompt": "Agent Neo, do you wish to decrypt node 250 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0251", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0252", "xp": 5}
        ]
    },
    "CH7_NODE_0251": {
        "id": "CH7_NODE_0251",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 251 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1757'.",
        "prompt": "Agent Neo, do you wish to decrypt node 251 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0252", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0253", "xp": 5}
        ]
    },
    "CH7_NODE_0252": {
        "id": "CH7_NODE_0252",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 252 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1764'.",
        "prompt": "Agent Neo, do you wish to decrypt node 252 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0253", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0254", "xp": 5}
        ]
    },
    "CH7_NODE_0253": {
        "id": "CH7_NODE_0253",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 253 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1771'.",
        "prompt": "Agent Neo, do you wish to decrypt node 253 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0254", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0255", "xp": 5}
        ]
    },
    "CH7_NODE_0254": {
        "id": "CH7_NODE_0254",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 254 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1778'.",
        "prompt": "Agent Neo, do you wish to decrypt node 254 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0255", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0256", "xp": 5}
        ]
    },
    "CH7_NODE_0255": {
        "id": "CH7_NODE_0255",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 255 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1785'.",
        "prompt": "Agent Neo, do you wish to decrypt node 255 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0256", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0257", "xp": 5}
        ]
    },
    "CH7_NODE_0256": {
        "id": "CH7_NODE_0256",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 256 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1792'.",
        "prompt": "Agent Neo, do you wish to decrypt node 256 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0257", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0258", "xp": 5}
        ]
    },
    "CH7_NODE_0257": {
        "id": "CH7_NODE_0257",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 257 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1799'.",
        "prompt": "Agent Neo, do you wish to decrypt node 257 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0258", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0259", "xp": 5}
        ]
    },
    "CH7_NODE_0258": {
        "id": "CH7_NODE_0258",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 258 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1806'.",
        "prompt": "Agent Neo, do you wish to decrypt node 258 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0259", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0260", "xp": 5}
        ]
    },
    "CH7_NODE_0259": {
        "id": "CH7_NODE_0259",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 259 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1813'.",
        "prompt": "Agent Neo, do you wish to decrypt node 259 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0260", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0261", "xp": 5}
        ]
    },
    "CH7_NODE_0260": {
        "id": "CH7_NODE_0260",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 260 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1820'.",
        "prompt": "Agent Neo, do you wish to decrypt node 260 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0261", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0262", "xp": 5}
        ]
    },
    "CH7_NODE_0261": {
        "id": "CH7_NODE_0261",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 261 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1827'.",
        "prompt": "Agent Neo, do you wish to decrypt node 261 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0262", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0263", "xp": 5}
        ]
    },
    "CH7_NODE_0262": {
        "id": "CH7_NODE_0262",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 262 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1834'.",
        "prompt": "Agent Neo, do you wish to decrypt node 262 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0263", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0264", "xp": 5}
        ]
    },
    "CH7_NODE_0263": {
        "id": "CH7_NODE_0263",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 263 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1841'.",
        "prompt": "Agent Neo, do you wish to decrypt node 263 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0264", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0265", "xp": 5}
        ]
    },
    "CH7_NODE_0264": {
        "id": "CH7_NODE_0264",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 264 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1848'.",
        "prompt": "Agent Neo, do you wish to decrypt node 264 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0265", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0266", "xp": 5}
        ]
    },
    "CH7_NODE_0265": {
        "id": "CH7_NODE_0265",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 265 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1855'.",
        "prompt": "Agent Neo, do you wish to decrypt node 265 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0266", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0267", "xp": 5}
        ]
    },
    "CH7_NODE_0266": {
        "id": "CH7_NODE_0266",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 266 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1862'.",
        "prompt": "Agent Neo, do you wish to decrypt node 266 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0267", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0268", "xp": 5}
        ]
    },
    "CH7_NODE_0267": {
        "id": "CH7_NODE_0267",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 267 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1869'.",
        "prompt": "Agent Neo, do you wish to decrypt node 267 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0268", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0269", "xp": 5}
        ]
    },
    "CH7_NODE_0268": {
        "id": "CH7_NODE_0268",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 268 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1876'.",
        "prompt": "Agent Neo, do you wish to decrypt node 268 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0269", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0270", "xp": 5}
        ]
    },
    "CH7_NODE_0269": {
        "id": "CH7_NODE_0269",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 269 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1883'.",
        "prompt": "Agent Neo, do you wish to decrypt node 269 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0270", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0271", "xp": 5}
        ]
    },
    "CH7_NODE_0270": {
        "id": "CH7_NODE_0270",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 270 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1890'.",
        "prompt": "Agent Neo, do you wish to decrypt node 270 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0271", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0272", "xp": 5}
        ]
    },
    "CH7_NODE_0271": {
        "id": "CH7_NODE_0271",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 271 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1897'.",
        "prompt": "Agent Neo, do you wish to decrypt node 271 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0272", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0273", "xp": 5}
        ]
    },
    "CH7_NODE_0272": {
        "id": "CH7_NODE_0272",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 272 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1904'.",
        "prompt": "Agent Neo, do you wish to decrypt node 272 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0273", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0274", "xp": 5}
        ]
    },
    "CH7_NODE_0273": {
        "id": "CH7_NODE_0273",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 273 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1911'.",
        "prompt": "Agent Neo, do you wish to decrypt node 273 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0274", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0275", "xp": 5}
        ]
    },
    "CH7_NODE_0274": {
        "id": "CH7_NODE_0274",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 274 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1918'.",
        "prompt": "Agent Neo, do you wish to decrypt node 274 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0275", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0276", "xp": 5}
        ]
    },
    "CH7_NODE_0275": {
        "id": "CH7_NODE_0275",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 275 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1925'.",
        "prompt": "Agent Neo, do you wish to decrypt node 275 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0276", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0277", "xp": 5}
        ]
    },
    "CH7_NODE_0276": {
        "id": "CH7_NODE_0276",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 276 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1932'.",
        "prompt": "Agent Neo, do you wish to decrypt node 276 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0277", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0278", "xp": 5}
        ]
    },
    "CH7_NODE_0277": {
        "id": "CH7_NODE_0277",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 277 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1939'.",
        "prompt": "Agent Neo, do you wish to decrypt node 277 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0278", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0279", "xp": 5}
        ]
    },
    "CH7_NODE_0278": {
        "id": "CH7_NODE_0278",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 278 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1946'.",
        "prompt": "Agent Neo, do you wish to decrypt node 278 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0279", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0280", "xp": 5}
        ]
    },
    "CH7_NODE_0279": {
        "id": "CH7_NODE_0279",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 279 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1953'.",
        "prompt": "Agent Neo, do you wish to decrypt node 279 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0280", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0281", "xp": 5}
        ]
    },
    "CH7_NODE_0280": {
        "id": "CH7_NODE_0280",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 280 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1960'.",
        "prompt": "Agent Neo, do you wish to decrypt node 280 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0281", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0282", "xp": 5}
        ]
    },
    "CH7_NODE_0281": {
        "id": "CH7_NODE_0281",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 281 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1967'.",
        "prompt": "Agent Neo, do you wish to decrypt node 281 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0282", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0283", "xp": 5}
        ]
    },
    "CH7_NODE_0282": {
        "id": "CH7_NODE_0282",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 282 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1974'.",
        "prompt": "Agent Neo, do you wish to decrypt node 282 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0283", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0284", "xp": 5}
        ]
    },
    "CH7_NODE_0283": {
        "id": "CH7_NODE_0283",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 283 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1981'.",
        "prompt": "Agent Neo, do you wish to decrypt node 283 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0284", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0285", "xp": 5}
        ]
    },
    "CH7_NODE_0284": {
        "id": "CH7_NODE_0284",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 284 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1988'.",
        "prompt": "Agent Neo, do you wish to decrypt node 284 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0285", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0286", "xp": 5}
        ]
    },
    "CH7_NODE_0285": {
        "id": "CH7_NODE_0285",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 285 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 1995'.",
        "prompt": "Agent Neo, do you wish to decrypt node 285 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0286", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0287", "xp": 5}
        ]
    },
    "CH7_NODE_0286": {
        "id": "CH7_NODE_0286",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 286 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 2002'.",
        "prompt": "Agent Neo, do you wish to decrypt node 286 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0287", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0288", "xp": 5}
        ]
    },
    "CH7_NODE_0287": {
        "id": "CH7_NODE_0287",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 287 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 2009'.",
        "prompt": "Agent Neo, do you wish to decrypt node 287 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0288", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0289", "xp": 5}
        ]
    },
    "CH7_NODE_0288": {
        "id": "CH7_NODE_0288",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 288 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 2016'.",
        "prompt": "Agent Neo, do you wish to decrypt node 288 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0289", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0290", "xp": 5}
        ]
    },
    "CH7_NODE_0289": {
        "id": "CH7_NODE_0289",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 289 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 2023'.",
        "prompt": "Agent Neo, do you wish to decrypt node 289 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0290", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0291", "xp": 5}
        ]
    },
    "CH7_NODE_0290": {
        "id": "CH7_NODE_0290",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 290 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 2030'.",
        "prompt": "Agent Neo, do you wish to decrypt node 290 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0291", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0292", "xp": 5}
        ]
    },
    "CH7_NODE_0291": {
        "id": "CH7_NODE_0291",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 291 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 2037'.",
        "prompt": "Agent Neo, do you wish to decrypt node 291 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0292", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0293", "xp": 5}
        ]
    },
    "CH7_NODE_0292": {
        "id": "CH7_NODE_0292",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 292 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 2044'.",
        "prompt": "Agent Neo, do you wish to decrypt node 292 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0293", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0294", "xp": 5}
        ]
    },
    "CH7_NODE_0293": {
        "id": "CH7_NODE_0293",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 293 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 2051'.",
        "prompt": "Agent Neo, do you wish to decrypt node 293 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0294", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0295", "xp": 5}
        ]
    },
    "CH7_NODE_0294": {
        "id": "CH7_NODE_0294",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 294 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 2058'.",
        "prompt": "Agent Neo, do you wish to decrypt node 294 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0295", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0296", "xp": 5}
        ]
    },
    "CH7_NODE_0295": {
        "id": "CH7_NODE_0295",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 295 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 2065'.",
        "prompt": "Agent Neo, do you wish to decrypt node 295 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0296", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0297", "xp": 5}
        ]
    },
    "CH7_NODE_0296": {
        "id": "CH7_NODE_0296",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 296 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 2072'.",
        "prompt": "Agent Neo, do you wish to decrypt node 296 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0297", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0298", "xp": 5}
        ]
    },
    "CH7_NODE_0297": {
        "id": "CH7_NODE_0297",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 297 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 2079'.",
        "prompt": "Agent Neo, do you wish to decrypt node 297 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0298", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0299", "xp": 5}
        ]
    },
    "CH7_NODE_0298": {
        "id": "CH7_NODE_0298",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 298 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 2086'.",
        "prompt": "Agent Neo, do you wish to decrypt node 298 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0299", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0300", "xp": 5}
        ]
    },
    "CH7_NODE_0299": {
        "id": "CH7_NODE_0299",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 299 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 2093'.",
        "prompt": "Agent Neo, do you wish to decrypt node 299 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0300", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0300", "xp": 5}
        ]
    },
    "CH7_NODE_0300": {
        "id": "CH7_NODE_0300",
        "chapter": 7,
        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",
        "text": "Dialogue node 300 in Chapter 7. The terminal blinks with an alert: 'System compromised at level 2100'.",
        "prompt": "Agent Neo, do you wish to decrypt node 300 or bypass it?",
        "options": [
            {"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH7_NODE_0300", "xp": 10},
            {"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH7_NODE_0300", "xp": 5}
        ]
    },
}

def get_chapter_7_node(node_id):
    return CHAPTER_7_NODES.get(node_id, None)

def list_chapter_7_speakers():
    speakers = set()
    for node in CHAPTER_7_NODES.values():
        speakers.add(node["speaker"])
    return list(speakers)

def count_chapter_7_choices():
    count = 0
    for node in CHAPTER_7_NODES.values():
        count += len(node["options"])
    return count
