"""
This script retimes an asciinema cast file to speed up sections with animated spinner.
"""
import json
import sys
import re

def retime_cast(file_path, speed_factor):
    spinner_frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

    def strip_ansi(data):
        """Removes ANSI escape codes from a string."""
        return re.sub(r'\x1b\[([0-9;]*[mGKHJ])', '', data)

    def normalize_output(data, frames):
        """Removes spinner frames and ANSI codes for comparison."""
        data = strip_ansi(data)
        for frame in frames:
            data = data.replace(frame, '')
        return data

    with open(file_path, 'r') as f:
        header = json.loads(f.readline())
        events = [json.loads(line) for line in f if line.strip()]

    print(json.dumps(header))

    last_original_ts = 0.0
    last_new_ts = 0.0

    for i, event in enumerate(events):
        original_ts = event[0]
        original_delay = original_ts - last_original_ts
        new_delay = original_delay
        speed_up = False

        if event[1] == 'o':
            current_data = event[2]
            current_has_spinner = any(frame in current_data for frame in spinner_frames)

            if current_has_spinner:
                # Search backwards for the last event that was an output with a spinner
                j = i - 1
                while j >= 0:
                    if events[j][1] == 'o':
                        prev_data = events[j][2]
                        if any(frame in prev_data for frame in spinner_frames):
                            normalized_current = normalize_output(current_data, spinner_frames)
                            normalized_prev = normalize_output(prev_data, spinner_frames)
                            if normalized_current == normalized_prev:
                                speed_up = True
                            break  # Found the last relevant frame
                    j -= 1
        
        if speed_up:
            new_delay = original_delay / speed_factor
        
        new_ts = last_new_ts + new_delay
        event[0] = new_ts
        
        last_original_ts = original_ts
        last_new_ts = new_ts

        print(json.dumps(event))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python retime.py <file.cast> <speed_factor>", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        speed_factor = float(sys.argv[2])
        if speed_factor <= 0:
            raise ValueError("Speed factor must be a positive number.")
    except ValueError as e:
        print(f"Error: Invalid speed factor. {e}", file=sys.stderr)
        sys.exit(1)

    retime_cast(file_path, speed_factor)