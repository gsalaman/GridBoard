# Glenn's ideas for the gamepad launcher
Use Jonah's base framework as a starting point.  Each application will have a class that "runs" that application.  
An app can be as simple as just showing a screen for a given period of time, or it can be a complex set of screens implementing a game with begin, end, and high-score pieces.

These classes should all implement a "run" function that the launcher will call.  Run will return a code that the launcher uses to pick the  next application.

## Example
As an example, consider the existing game-launcher as defined by the game design team.  We have the following screens and behaviors:
* We start with the "splash" screen.  This has exactly one exit (pushing the big button in the middle) which goes to the "game select" screen.  It's only return value will be "select".
* In the game select screen, we can exit in 4 ways:
  * User selects "Tic-Tac-Toe".  Screen returns "TTT".
  * User selects "Connect 4".  Screen returns "C4".
  * User selects "Minesweeper".  Screen returns "MS"
  * Screen timeouts (time TBD).  Screen returns "splash"

## Driver Code
Did a quick prototype with just the splash and select screen.
Check out the following snippet from the "glenn_launcher_ideas" branch of board_main,py.
```
splash = splashApp(matrix, total_rows, total_columns)
select = selectApp(matrix, total_rows, total_columns)
apps = {
  "splash": splash,
  "select": select
}

currentApp = splash 
```
This builds a dictionary of all of our apps, and sets the starting point to "splash".

The "big loop" then looks like this:
```
    while True:
      nextApp = currentApp.run()
      currentApp = apps[nextApp]
```

# Encapsulation notes
The thing I like about this design is that it reduces coupling between "board_main" and the apps that we are writing.  The only info that "board_main" needs to know are the app names and return codes (which are other app names).  It doesn't care about screens or timing or inputs from the apps in question.
  
