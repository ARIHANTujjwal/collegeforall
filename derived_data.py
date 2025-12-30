from utils import load_json_to_dict, save_dict_to_json, safe_int, STATE_MAP
import os
import argparse
import json

cwd = os.getcwd()

# SCHOOLS = f"{cwd}/data/schools.json"

def derive_data(filename, min_math=None, max_math=None, min_eng=None, max_eng=None, state=None):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    schools = load_json_to_dict(filename)
    filtered_results = []

    for school, sdata in schools.items():
        # 1. Extraction with Null-Safety
        mscore = safe_int(sdata.get("sat_math"))
        wscore = safe_int(sdata.get("sat_writing"))
        rscore = safe_int(sdata.get("sat_critical_reading"))
        
        # Determine English Score (Max of Writing/Reading)
        escore = max(wscore, rscore)
        
        # Clean State Data
        school_state = sdata.get("state", "").strip().upper()

        # 2. Filtering
        if min_math is not None and mscore < min_math:
            continue
        if max_math is not None and mscore > max_math:
            continue
        if min_eng is not None and escore < min_eng:
            continue
        if max_eng is not None and escore > max_eng:
            continue
        if state and state.upper() != school_state:
            continue

        # 3. Collect Match
        filtered_results.append({
            "name": school,
            "math": mscore,
            "english": escore,
            "state": school_state
        })

    # 4. Multi-Level Sorting Logic:
    # Primary: Math (Descending) -> -x['math']
    # Secondary: English (Descending) -> -x['english']
    # Tertiary: School Name (Ascending) -> x['name']
    sorted_results = sorted(
        filtered_results, 
        key=lambda x: (-x['math'], -x['english'], x['name'])
    )

    # 5. Output
    print(f"\n{'School Name':<55} | {'Math':<5} | {'English':<7} | {'State Code':<9} | {'State'}")
    print("-" * 108)

    if not sorted_results:
        print("No schools found matching those criteria.")
    else:
        for s in sorted_results:
            math_display = s['math'] if s['math'] > 0 else "N/A"
            eng_display = s['english'] if s['english'] > 0 else "N/A"
            
            state_name = STATE_MAP.get(s['state'], "")
            if not state_name:
              state_name = s['state']
            
            print(f"{s['name'][:55]:<55} | {math_display:<5} | {eng_display:<7} |  {s['state']:<9} | {state_name}")

# Entry Point

def main():
    parser = argparse.ArgumentParser(description="Filter/Sort USA Colleges by SAT Scores.")
    
    parser.add_argument("--file", type=str, required=True, help="Path to schools.json")
    parser.add_argument("--min_math", type=int, help="Minimum SAT Math Score")
    parser.add_argument("--max_math", type=int, help="Maximum SAT Math Score")
    parser.add_argument("--min_eng", type=int, help="Minimum SAT English Score")
    parser.add_argument("--max_eng", type=int, help="Maximum SAT English Score")
    parser.add_argument("--state", type=str, help="Two-letter state (e.g., CA)")

    args = parser.parse_args()

    derive_data(args.file, args.min_math, args.max_math, args.min_eng, args.max_eng, args.state)

if __name__ == "__main__":
  # uv run  derived_data.py --file src/collegedata/derived_data.py --min_math 750 --max_math 800
  main()
