# Bar Chart Logs

Bar Chart Logs is a Python project that analyzes server log data and creates a bar chart of the most visited endpoints. The project takes raw log data, counts how many times each endpoint appears, and visualizes the top endpoints.

## Purpose

The purpose of this project is to practice working with log data, counting repeated values, and turning raw information into a readable chart. This project helped me understand how server logs can be analyzed to find useful traffic patterns.

## Features

* Reads server log data
* Counts how often each endpoint appears
* Identifies the most visited endpoints
* Displays the top endpoints in a bar chart
* Uses Python to process and visualize the data

## Tech Stack

* Python
* Flask
* Jupyter Notebook
* Matplotlib

## Project Files

```text
bar-chart-logs/
├── analytics.py
├── barchart.ipynb
└── README.md
```

## What I Learned

While building this project, I practiced reading and processing data, using Python dictionaries or counters to track repeated values, and creating a bar chart to make the results easier to understand. I also gained experience using Flask for a basic API route and Jupyter Notebook for testing and visualizing the data.

## Future Improvements

* Allow users to upload their own log files
* Add filtering by endpoint or request type
* Add more chart options
* Improve error handling
* Organize the code into separate helper functions
* Eventually turn it into a full web application

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Unknown903-dev/bar-chart-logs.git
```

2. Open the project folder:

```bash
cd bar-chart-logs
```

3. Install the required packages:

```bash
pip install flask requests matplotlib
```

4. Run the Python file:

```bash
python analytics.py
```

5. Open the notebook to view or edit the chart:

```text
barchart.ipynb
```

