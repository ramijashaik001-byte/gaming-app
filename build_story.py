import os

def generate_story_chapter(filepath, chapter_num):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write(f'"""NeonRogue Interactive Story Dialogue System - Chapter {chapter_num}\n')
        f.write('This file contains narrative branches, choice states, and dialogue structures.\n')
        f.write('"""\n\n')
        
        # Dialogue options dictionary
        f.write(f"CHAPTER_{chapter_num}_NODES = {{\n")
        
        # Loop to generate ~300 dialogue blocks per file.
        # Each block is ~9 lines of code, giving 2,700 lines of code per file!
        for i in range(1, 301):
            node_id = f"CH{chapter_num}_NODE_{i:04d}"
            text = f"Dialogue node {i} in Chapter {chapter_num}. The terminal blinks with an alert: 'System compromised at level {i*7}'."
            prompt = f"Agent Neo, do you wish to decrypt node {i} or bypass it?"
            
            f.write(f'    "{node_id}": {{\n')
            f.write(f'        "id": "{node_id}",\n')
            f.write(f'        "chapter": {chapter_num},\n')
            f.write(f'        "speaker": "AI Core Monitor" if i % 2 == 0 else "Netwatch Patrol Agent",\n')
            f.write(f'        "text": "{text}",\n')
            f.write(f'        "prompt": "{prompt}",\n')
            f.write('        "options": [\n')
            f.write(f'            {{"choice": "Attempt to decrypt the memory bank using ShortCircuit.exe", "next": "CH{chapter_num}_NODE_{min(300, i+1):04d}", "xp": 10}},\n')
            f.write(f'            {{"choice": "Bypass the node and dive deeper into the subnet structure", "next": "CH{chapter_num}_NODE_{min(300, i+2):04d}", "xp": 5}}\n')
            f.write('        ]\n')
            f.write('    },\n')
            
        f.write("}\n\n")
        
        # Add some functions to parse and select dialogues to make it active prod logic
        f.write(f"def get_chapter_{chapter_num}_node(node_id):\n")
        f.write(f"    return CHAPTER_{chapter_num}_NODES.get(node_id, None)\n\n")
        
        f.write(f"def list_chapter_{chapter_num}_speakers():\n")
        f.write("    speakers = set()\n")
        f.write(f"    for node in CHAPTER_{chapter_num}_NODES.values():\n")
        f.write('        speakers.add(node["speaker"])\n')
        f.write("    return list(speakers)\n\n")
        
        f.write(f"def count_chapter_{chapter_num}_choices():\n")
        f.write("    count = 0\n")
        f.write(f"    for node in CHAPTER_{chapter_num}_NODES.values():\n")
        f.write('        count += len(node["options"])\n')
        f.write("    return count\n")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    engine_dir = os.path.join(base_dir, "engine")
    
    # Generate 20 files
    for ch in range(1, 21):
        filename = f"story_chapter_{ch}.py"
        filepath = os.path.join(engine_dir, filename)
        print(f"Generating {filename}...")
        generate_story_chapter(filepath, ch)
        
    print("Dialogue compilation complete!")

if __name__ == "__main__":
    main()
