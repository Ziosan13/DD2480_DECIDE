# DD2480 - DECIDE

The DECIDE program generates a boolean signal which determines whether an interceptor should be launched or not.

## Description

The DECIDE program uses 5 inputs: 
- NUMPOINTS (the number of planar data points on radar tracking), 
- POINTS (an array containing the coordinates of data points), 
- PARAMETERS (a dictionary holding various parameters used by the program - see list of parameters below), 
- LCM (a 15x15 logical connector matrix which determines boolean relationships between the various conditions needed to be fulfilled - it contains values among "NOTUSED", "ANDD" and "ORR")
- PUV (a preliminary unlocking vector - it contains boolean values determining if some conditions should hold back the launch of the interceptor). 
Using these, a boolean signal is generated and "YES" or "NO" is printed to the standard output based on the decision.

### List of parameters
The parameters in the PARAMETERS dictionary are as follow:
- LENGTH1 (float) : Length in LICs 0, 7, 12
- RADIUS1 (float) : Radius in LICs 1, 8, 13
- EPSILON (float) : Deviation from PI in LICs 2, 9
- AREA1 (float) : Area in LICs 3, 10, 14
- Q_PTS (int)  : No. of consecutive points in LIC 4
- QUADS (int) : No. of quadrants in LIC 4 
- DIST (double) : Distance in LIC 6
- N_PTS (int) : No. of consecutive pts. in LIC 6
- K_PTS (int) : No. of int. pts. in LICs 7, 12
- A_PTS (int) : No. of int. pts. in LICs 8, 13
- B_PTS (int) : No. of int. pts. in LICs 8, 13
- C_PTS (int) : No. of int. pts. in LIC 9
- D_PTS (int) : No. of int. pts. in LIC 9
- E_PTS (int) : intGPTS; double LENGTH2; double RADIUS2 ; double AREA2;
- F_PTS (int) :
- G_PTS (int) :
// Length in LICs 0, 7, 12
// Radius in LICs 1, 8, 13
// Deviation from PI in LICs 2, 9
// Area in LICs 3, 10, 14
// No. of consecutive points in LIC 4 // No. of quadrants in LIC 4
// Distance in LIC 6
// 
// No. of int. pts. in LICs
// No. of int. pts. in LICs
// No. of int. pts. in LICs
//  //  // No. of int. pts. in LICs
// No. of int. pts. in LICs
// No. of int. pts. in LIC 11 // Maximum length in LIC 12
// Maximum radius in LIC 13 // Maximum area in LIC 14

## Getting Started

### Dependencies

To install dependencies for the program, run (from the project folder):
```
pip install -r requirements.txt
```

### Documentation
To generate PDF documentation, run from the docs/ folder (after installing dependencies):
```
make latexpdf
```
or (for Windows)
```
.\make.bat latexpdf
```
To generate html files, replace latexpdf with html in the last commands.
Generated files are then available in docs/_build/ folder.

### Installing

To install the program, just clone the GitHub repository.

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Authors

* Eloi Dieme
* Hugo Malmberg
* Olivia Aronsson
* Lovisa Strange
* Yuta Ojima

## Version History

* 0.1
    * Initial Release

## Assessment of way of working

From looking at the checklist, we agree that our way of working currently fulfills the "In Place"-level. We think this because the tools that we are using, for example GitHub issues and pull requests, are working well and are helping the team work efficiently on what needs to be done. Also, all team members are involved in reviewing and improving each other's work, which is also helping the team work better. This is in line with what the requirements for this level states. To get to the next level, "Working well", we need to become more comfortable with working this way, as the requirements state that the way of working should come naturally and not require much effort from the team members. The way of working should also be adjusted as needed to support the work being done. By continuing to work in this way, we will become more confident in our way of working. By also continuing to evaluate how the work is going, we can reach the next state.  

## Statement of contributions

* Eloi Dieme: initialized Decide class; implemented LICs 3, 8 and 13 ; implemented documentation generation ; implemented LCM matrix; reviewed some pull requests; participated in writing README file and "Assess the way of working".

* Hugo Malmberg:
* Olivia Aronsson:
* Lovisa Strange:
* Yuta Ojima: