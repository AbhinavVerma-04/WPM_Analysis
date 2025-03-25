# Typing Speed Test  

A terminal-based typing speed test built with Python and `curses`, along with a Streamlit-powered dashboard for performance analysis.  

## Features  

### `typing_test.py`  
- Loads random text prompts from `text.txt`.  
- Tracks typing speed (WPM) in real-time.  
- Saves test results (username, timestamp, WPM, and time taken) in `typing_data.csv`.  
- Provides basic UI with error highlighting (green for correct, red for incorrect).  
- Allows users to retry the test.  

### `dashboard.py`  
- Loads past typing test results from `typing_data.csv`.  
- Displays user-specific performance trends with timestamps.  
- Visualizes typing speed progress using Matplotlib plots.  

## Installation  

### Prerequisites  
Ensure you have Python installed (version 3.7+ recommended).  

### Install Dependencies  
```bash
pip install streamlit pandas matplotlib
```

## Usage  

### Running the Typing Test  
```bash
python typing_test.py
```
- Follow the on-screen instructions to type the displayed text.  
- The test ends when you complete the text or press `ESC`.  
- Results are stored in `typing_data.csv`.  

### Viewing the Dashboard  
```bash
python -m streamlit run dashboard.py
```
- Opens a web-based dashboard for analyzing past test results.  
- Select a username to view their typing speed history.  

## File Structure  
```
📦 Typing-Speed-Test  
 ┣ 📜 typing_test.py    # Terminal-based typing test  
 ┣ 📜 dashboard.py      # Streamlit dashboard for data visualization  
 ┣ 📜 text.txt         # Text file containing typing test prompts  
 ┣ 📜 typing_data.csv  # Stores past typing test results  
 ┣ 📜 README.md        # Project documentation  
```

## Future Improvements  
- Add accuracy tracking.  
- Implement difficulty levels.  
- Enhance UI for better user experience.  
