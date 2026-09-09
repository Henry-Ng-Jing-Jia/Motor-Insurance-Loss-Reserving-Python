# Motor-Insurance-Loss-Reserving-Python

## Project Summary
This project uses a motor insurance dataset to estimate the loss reserve of the latest development period. The dataset consists of 30,000 cases, each case has 6 stages of development. So, in total it is a 180,000-row dataset. 

## Actuarial Context
Property and casualty (P&C) loss reserving is the process of estimating and setting aside the pool of money an insurance company needs to pay for claims that have already occurred but have not yet been fully settled or paid, in short IBNR.

## Dataset Overview 
Each case consists of 6 stages: First Notification of Loss (FNOL), Assign Claim, Claim Decision, Set Reserve, Payment Sent, Close Claim. For each case, I check for nulls and validate the chronological dates. 

## Methodology & Data Pipeline
- Data Cleaning: I extracted the timestamps of FNOL and payment transaction.
- Finding the Development Lag: I calculated the duration in days and map them into monthly cohorts (dev_month 0, 1, 2).
- Mechanics behind the Reserving Estimation: I constructed a 37×3 matrix and applied volume weighted link ratio of $f_{1→2}$.

## Key Output
A table of the final 37×3 Monthly Cumulative Loss Triangle is generated and the projected ultimate loss figure for the latest undeveloped cohort April 2023 is $1336638.69.
 <img width="525" height="802" alt="image" src="https://github.com/user-attachments/assets/8c4a27b7-0b2c-46d8-96ea-3512a374900a" />


## Tech Stack
Python libraries used are pandas, openpyxl and tools used are Excel and Github

## How to Run
1. **Clone the repository:**
```bash
   git clone https://github.com/Henry-Ng-Jing-Jia/Motor-Insurance-Loss-Reserving-Python.git
   ```
