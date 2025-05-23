# Singapore Metro Stations

## Description
<pre>
This project simulates the Singapore MRT (Mass Rapid Transit) network using a custom-built graph data structure. It allows users to:

- Load and process real MRT station data from a CSV file.
- Build a graph where each station is a node.
- Find the shortest route (least number of stops) between two stations.
- Find the fastest route (minimum travel time, with weighted edges).
- Handle interchanges between lines with fixed transfer times.
</pre>

<pre>
All graph logic is implemented from scratch, without external libraries like `networkx`.

When prompted, type the name of your starting and destination MRT stations.

Example:
Enter starting station name: PIONEER MRT STATION
Enter destination station name: ANG MO KIO MRT STATION

## Features
Custom graph with edges, weights, BFS, and Dijkstra.
Randomized travel time (2–8 mins) for adjacent stations.
Fixed 5-min transfer time between lines at interchange stations.
Clear path output for shortest and fastest travel modes.
</pre>

## Requirements
- Python 3.x (no external libraries required)
- No external libraries required (only uses the standard library and `pandas`)

## How to run
python main.py


## To download the project from github:
<pre>
1. Shift + Right Click on the directory you want to 
save the project.
2. Select "Open command window in here".
3. git clone (https://github.com/joanadhiamandi/singapore_metro.git )
4. cd singapore_metro
</pre>

## To create the virtual enviroment:
<pre>
1. cd singapore_metro                #To go inside the project.
2. python -m venv venv                #To create the virtual enviroment.
3. venv\Scripts\Activate                #To start the virtual enviroment.
4. pip install -r requirements.txt      #To install all the necessary libraries. ore (pip install pandas), the only dependency needed
5. python main.py                     #To start the program.
</pre>