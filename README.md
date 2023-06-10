# BattleShips project (Portfolio 3)

A game of Battleships wherr you enter coordinates to hit the opponents ships.

## How to play
- On Initialization, the board is generated randomly. Ships are placed unknown to the user.
<br>
<br>
<img src="https://imgtr.ee/images/2023/06/10/KNMWJ.png"  width="100" height="100">
<br>
<br>
- We are presented with quantity of shots left and a prompt to input coordinates in both y and x axis.
<br>
<br>
<img src="https://imgtr.ee/images/2023/06/10/KN7Gz.png"  width="100" height="100">
<br>
<br>
- Input validation is responded with when user enters coordinates out of the scope of the grid, enters the same guess twice and when user doesnt use numbers for input requests.
<br>
<br>
<img src="https://imgtr.ee/images/2023/06/10/KLXe2.png"  width="150" height="100">
<img src="https://imgtr.ee/images/2023/06/10/KLHQA.png"  width="120" height="100">
<img src="https://imgtr.ee/images/2023/06/10/KLzU7.png"  width="150" height="100">
<br>
<br>

## About This Project
I made this project with 4 functions that generate a board of 5 randomly positioned enemy ships of which only occupy one space. The user is provided with 10 shots to locate all 5 ships. The majority of this is contained in a while loop within the play_game() function which dictates various outcomes through if statements depending on user input and info updated in variables via the while loop.

### Built with
This project was structured with Python.

### Bugs
- Minor updates like adjusting the information logged to the user were all the fixes that needed to be done so far.

#### Bugs remaining
- No bugs are in the project currently.

## Testing

- Screened project by running through PEP8online validator
- Input invalid information, string values instead of numbers, same coordinates twice, numbers out of grid scope.
- Tested in my loacal terminal and Code Institutes Heroku terminal

## Validator testing

- PEP8: No errors were returned from PEP8online

## Deployment

The site was deployed using Code Institutes mock terminal in Heroku.

- Steps for deployment:
    - Fork or clone this repository
    - Create a new Heroku app
    - Set the buildbacks to "Python" and "NodeJS" in that order
    - Link the Heroku app to the repository
    - Click on **Deploy**

## Credits
- Code Institute for the Heroku terminal