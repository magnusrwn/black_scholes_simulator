# Black-Scholes Simulator

A web-based simulator for the Black-Scholes model, implemented in Python with a frontend built using HTML and JavaScript. This project enables users to visualize and experiment with option pricing using the Black-Scholes formula.

## Features

- **Interactive option pricing calculator** using the Black-Scholes model
- **Visualizations** for option price and Greeks over time or varying parameters
- **User-friendly web interface** for entering parameters like stock price, strike price, volatility, interest rate, and time to maturity
- **Python backend** for calculations, with HTML/JavaScript frontend for interactivity

## Getting Started

### Prerequisites

- Python 3.x
- (Optional) pip for installing dependencies

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/magnusrwn/black_scholes_simulator.git
   cd black_scholes_simulator
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies (add requirements.txt if present):

   ```bash
   pip install -r requirements.txt
   ```

### Running the Simulator

If there is a Python script to launch a web server (e.g. `app.py` or `main.py`), run:

```bash
python app.py
```

Then open your browser and navigate to `http://localhost:5000` (or the specified port... specified in terminal on run of 'run.py').

### Usage

1. Enter the parameters for the option (stock price, strike price, volatility, interest rate, time to maturity).
2. Click "Calculate" to see the option price and Greeks.
3. Use interactive graphs to explore how changes in parameters affect pricing.

## Project Structure

- `*.py` — Python backend code for Black-Scholes calculations and web server
- `*.html` — Frontend UI templates
- `*.js` — Frontend scripts for interactivity and visualization


*This README was generated as a starting point. Feel free to customize it with more details about your project, scripts, and usage examples!*

## About the code...
All code, bar the tailwind CSS, was hand written/ non ai. This is purely becasue; A) Frontend tends to be tedious, and I did not need anything insane. B) I am learning. This is a learning project, so all code (bar the frontend -- which I am capable of doing) was understood. All code is as clean sa possible, and i assume decently modular and easy to understand, however improvements and critiques would be greatly appriciated!

This took (approx) 2-3 days of a few hours of work, and is the first finished decent project that I am both happy, and interested with.

Throughout the proscess of developing this, I have learned to greater understand building full-stack apps, the Basics of the FastAPI framework, plotting (with plotly), the maths behind the black scholes model, and more...
