Guys i found this research of Sir  Brian J. Johnson and i was like Oh boy we have to do this 

# Mosquito Love to Death: Audio Tones for Attracting Mosquitoes

well apparently this is a thing that only males are attracted 😂🤣females need not waste their energy oh boy indeed a  classical problem 





🦟 Mosquito Frequency Experiment (Python)
This project plays audio tones at specific frequencies (e.g., 550–600 Hz) that are known to potentially attract female mosquitoes, particularly during their mating phase. The tones mimic the wingbeat frequencies of male mosquitoes.

📦 Setup Instructions
1. Clone the Repository (or save your .py file)

git clone <your-repo-url>
cd mosquito-tone-lab
2. Create and Activate Virtual Environment (Recommended)

python -m venv mosquito-env
source mosquito-env/bin/activate      # Linux/macOS
.\mosquito-env\Scripts\activate       # Windows
3. Install Dependencies

pip install sounddevice numpy


▶️ Usage
Run the Python script to test various mosquito-attracting tone patterns.


python mosquito_tone_experiments.py



🎵 Available Tone Tests
Test	Function	Description
T1	play_tone(550, 10)	Plays 550 Hz continuously for 10 sec
T2	play_tone(600, 10)	Plays 600 Hz continuously for 10 sec
T3	pulse_tone(550, 1, 1, 10)	1 sec ON / 1 sec OFF pulse pattern
T4	sweep_tone(500, 650, 10)	Gradually increases frequency from 500 to 650 Hz
T5	alternate_tones(550, 600, 2, 5)	Alternates between 550 Hz and 600 Hz for 2 sec each



⚠️ Safety & Limitations
Do NOT play at full volume in headphones. Use external speakers for better effect.

Results may vary by mosquito species and environment.

Mosquito attraction depends on factors like temperature, time of day, and presence of humans or standing water.



🧪 Experiment Ideas
Track mosquito activity using time-lapse video or logging app.

Add water + light source to increase attractiveness.

Log observations in a CSV (logging template included in code).



📁 File Structure (Minimal Version)
pgsql
Copy
Edit
mosquito-tone-lab/
│
├── mosquito_tone_experiments.py   # Main Python script
├── README.md                      # This file
└── requirements.txt               # Optional: freeze deps
To generate requirements.txt:


pip freeze > requirements.txt


💡 Future Plans (Optional Ideas)
Export tones to .wav

CLI/terminal menu to select test case

Matplotlib visual of frequency over time (for sweep)

Real-time mic input to capture mosquito buzz
