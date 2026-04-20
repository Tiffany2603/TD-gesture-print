# Dingfuzhuang Private Physical Examination Center

An interactive installation that uses motion capture and real-time 
visual feedback to simulate a satirical "health checkup" — 
exploring how contemporary youth express stress and anxiety 
through humor and absurdity.

## About

Inspired by the "Mad Literature" phenomenon on Chinese social media, 
this installation invites visitors to undergo a fictional medical 
examination. Participants fill out a symptom checklist, stand before 
a screen for a full-body Kinect scan, receive a personalized 
"diagnosis report," and print it out to take home.

The piece uses medical aesthetics, ASCII art, and real-time body 
tracking to create an immersive, participatory experience that 
validates the emotional states of young people under social pressure.

## Built With

- **TouchDesigner** — interactive visuals, Kinect data processing, 
  UI flow
- **Python** — printer integration via folder monitoring (watchdog)
- **Microsoft Kinect** — body capture, motion recognition, 
  gesture-based interaction

## Hardware Requirements

- Microsoft Kinect sensor
- Display screen
- Printer (for report output)
- Bright white exhibition space

## Software Requirements

- TouchDesigner 099 or above
- Python 3.x
- watchdog library: `pip install watchdog`

## Getting Started

1. Connect the Kinect sensor and printer
2. Open the `.toe` file in TouchDesigner
3. Run `print image.py` to start the print monitoring script
4. Visitor stands in front of the screen and raises their right hand
   - **Grab gesture** = click/select
5. Follow the on-screen flow to complete the scan
6. The printer automatically outputs the diagnosis report

## Project Structure

├── mainProject.toe                 # TouchDesigner main project file
├── print image.py        # Python print control script  
├── images/               # Symptom image assets
└── README.md

## How to Contribute

This project demonstrates a workflow for connecting TouchDesigner 
with physical output devices. Contributions welcome:

- Adapting the Kinect tracking for different body sizes or 
  environments
- Improving the Python printer script for other printer models
- Translating the symptom content for non-Chinese audiences
- Documenting alternative setups without Kinect

## Author

Yuan Ziyi  
Communication University of China, Digital Media Arts 2021  
Advisors: Yang Xiaojun, Wang Limin  
Collaborators: Wei Quntao (technical), Li Lingjing (visual design)

## License

MIT License — see [LICENSE](LICENSE) for details.
