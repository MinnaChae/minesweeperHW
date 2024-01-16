Aqueno Nirasmi Amalraj
Minna Chae
Sarah St. Albin 
TCSS 502 
Dungeon Adventure Game Final 


NOTE: Our Dungeon Adventure Game uses the factory design pattern. See our UML class diagram for details.



***



Name : Aqueno Nirasmi Amalraj 

Time: I have spent approximately 20 hours on this assignment.   

My part on this assignment was Room class its unit test, DungeonItems (HealingPotion, Pit, and four pillars) its unit test, UML diagram and Output Capture of Winning, Losing and Maze Gen. The challenging part on this assignment for me is figuring out the str method of Room class and I had an issue on calling the class directly with the constructor but it didn't work, and overcame the issue by using getter methods and setter methods to call the class. I had some doubts on the UML relationship between aggregation and composition Varik's explanation provided clarity on relationship between classes. 



***



Name : Minna Chae

Hours spent: 40-50 hours

I worked on Adventurer, Dungeon Adventure, Adventurer Unit Test, Dungeon Adventure Unit Test.

Short comings: Adventurer Class was easy and only took 1 day and I only created the print statements for Dungeon Adventure. Since I didn't fully understand how to structure the game, or what exactly went into each class, I waited for Dungeon to be workable to start diving into the Dungeon Adventure class. I believe I should have worked on Dungeon Adventure earlier to understand project better and provide help with different modules in Dungeon or create modules I needed in Dungeon earlier.

Other information/Extra Credit for game design: Dungeon Adventure had 4 levels of game play, easy, medium, hard, and player's choice. Player's choice allows the user to choose all of Adventurer's attributes and Dungeon size. User's choice also handles non-int values and doesn't allow negative values for Dungeon dimensions. Player's choice allows for negative attributes to make it harder for game play. If player chooses a 0 or negative values for health points, the player will automatically die.

For game play, a full image of the maze will display in the console. The maze map displays all attributes of the current room (doors, walls, item), --- for previously traveled rooms, and ^^^ for not yet traveled rooms. This allows the player to know where the player is in respect of the dungeon. There is also a print image of only the current room plus feedback on if the player had received any items or incurred any negative health points.

When the player reaches the end of the maze, the player can choose to leave the game or continue traversing through the maze.
The game will continue until the player has quit the game.

The secure menu option is \'93map\'94 and prints out the full map of the dungeon with all attributes. Map also prints the symbol \'93@\'93 at player's current location. This allows for the developer to know where the player is currently located on the map.

At the end of the game, there are 2 maps printed, one that has been traveled by the player and therefore does not display items picked up during the game. The second is the full original map with all original items.




***




Name: Sarah St. Albin

What I covered: My primary responsibility was the Dungeon class, as well as the DungeonItemsFactory once our team decided to incorporate the Factory design pattern into our project. I also wrote the applicable unit tests for my classes. 

Time spent: Between 40 and 50 hours

Shortcomings: I think our project would have benefited a lot from a GUI, but we ended up not having enough time to finish one. 

Other notes and reflections: I struggled and learned a lot during the course of this project! The unit tests for Dungeon were very hard for me, but I learned about ways to control randomness and other unpredictable behaviors that make consistent testing difficult. Writing the _create_maze and _traverse_the_maze (checking for possibility) algorithms for Dungeon was incredibly challenging, too. Figuring it out (finally) was very rewarding. 

Our team worked really hard to put into practice some of the concepts we learned in TCSS 502, especially in implementing a design method and prioritizing modular design (we did this with the Dungeon Items Factory, which hides the details of "dungeon items" object creation. We communicated daily, including impromptu remote meetings to talk through problems, and we tried to emulate what it will be like to work on a team for a company. We also used git and GitHub for versioning and keeping up to date with the latest version of our code. 
