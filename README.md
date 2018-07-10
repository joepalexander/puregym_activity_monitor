# Puregym Activity Monitor

**TL;DR - A project to continuously monitor how many people are in your local puregym**

We all need to go to the gym, but no one likes to be there when there is no space to get anything done. Knowing how many people are currently in your local
gym is useful. 

Fortunately, [the puregym members dashboard](https://puregym.com/members) displays exactly this information. However, it is only a snapshot of the current activity in the gym. Wouldn't it be nice to map the activity over time? That would allow you to find the trends. What time of day is it quietest? What day of  the week is busiest? etc etc

These are all good questions that can lead to you finding the best times to go to the gym based on real data about your local puregym. To answer these questions you need the raw data. That is where this project comes in.

## Getting started

This project uses python 3 (I used python 3.6.6 at time of creation) with selenium (using headless chrome) to log into your members area and pull the gym activity.

The following steps will get you set up:

1. Clone this repo
  `git clone https://github.com/adiman9/puregym_activity_monitor.git`
2. Enter the directory
  `cd puregym_activity_monitor`  
3. Install the python dependencies
  `pip install -r requirements.txt`
5. Run the project 
  `python scraper.py`

## Optional: continuously run in the background

I prefer to use pm2 from npm to ensure that the project is constantly running and will restart after any crashes.

1. Install nodejs and npm if you don't already have them on your system.
2. `npm install -g pm2`
3. Inside the `puregym_activity_monitor` directory run `pm2 start scraper.py`
4. done

## Contributing

This is a project I threw together pretty quickly, but I would be more than happy if anyone else wanted to clean things up or add features. All PRs welcomed :)
