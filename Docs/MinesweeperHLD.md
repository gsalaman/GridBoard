# Glenn's Minesweeper Thoughts
## Requirements
* 8x8 grid with 10 mines
* Board starts out with all squares hidden
* User does "quick press" to flag a square
* User does "long press" to reveal a square
* Game ends with loss if user reveals a mine
* Game ends with win if user has flagged all mines with no extraneous flags

## Data
We'll use two 8x8 arrays to drive the game:
* `grid[][]` will sow where the mines are.  Each cell contains:
  * `'M'` for a mine
  * if no mine, it'll have a number for how many mines surround that pice.  0 is allowed.
* `board[][]` keeps track of what the user as seen.  Each cell can be:
  * `'U'` for unknown
  * `'F'` for user-flagged
  * `'R'` for revealed

## Main Flow
* Initialize Game
  * Populate grid and board
* Main loop:  while game is still going
  * get a press
  * if it's a short press (reveal), flag that square and check for win
  * if it's a long press and it's a mine, show loss
  * if it's a long press and it's not a mine, show that square

## Input processing
Our existing "read" interface from `get_buttons.py` returns a tuple with x,y,and Press type...either `"P"` for a press or `"R"` for release.

To detect long vs short presses, we'll need to keep track of "state" for each button:  is it currently pressed?  The algo is as follows:
* When we get a press, store a timestamp for when that press started
* When we get a release, see how long that button has been down.  
  * If it's short (less than 2s?), count it as a short press.  
  * If it's long, count it as long.
  * Don't forget to set the button state back to "not pressed"

We could also add a little logic to show a "select" icon on press to give the user feedback.
