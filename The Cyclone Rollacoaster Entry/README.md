# The Cyclone Rollercoaster Entry System

A theme park ride entry validation system that checks height and credit requirements.

## Description

This program simulates an entry system for "The Cyclone" rollercoaster, checking if visitors meet both the height requirement (137 cm) and have sufficient credits (10) to ride.

## How to Use

1. Run the program: `python main.py`
2. Enter your height in centimeters when prompted
3. Enter your available credits when prompted
4. The system will determine if you can ride or what requirements you're missing

## Requirements to Ride

- **Minimum Height**: 137 cm (safety requirement)
- **Cost**: 10 credits

## Possible Outcomes

1. **"Enjoy the ride!"** - You meet both requirements
2. **"You are not tall enough to ride."** - Height < 137 cm but credits ≥ 10
3. **"You don't have enough credits."** - Height ≥ 137 cm but credits < 10  
4. **"You haven't met either requirement."** - Both height < 137 cm and credits < 10

## Features

- Dual requirement validation
- Clear feedback messages
- Safety-first approach
- Theme park simulation
- Multiple condition checking

## Learning Concepts

- Conditional statements (if/elif/else)
- Logical operators (and)
- Multiple condition evaluation
- User input handling
- Boolean logic
- Real-world application simulation

## Safety Note

The height requirement represents real safety standards used in theme parks to ensure rider safety on high-speed attractions.

## How to Run

```bash
python main.py
```

## Example Usage

```
Enter height: 140
Enter credits: 15
Enjoy the ride!
```

## Requirements

- Python 3.6 or higher

## Educational Purpose

This program demonstrates:
- Complex conditional logic
- Safety validation systems
- Real-world application of programming
- Multiple criteria decision making
- User input processing

## Real-World Applications

- Theme park management systems
- Access control systems
- Eligibility verification
- Safety compliance checking
- Age and requirement validation

## Potential Enhancements

- Add age verification
- Implement credit purchase system
- Create ride queue management
- Add multiple rides with different requirements
- Include group booking validation
