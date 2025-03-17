# Taylor-Freeman.github.io

## Welcome!
Welcome to my senior project page! Here, I showcase my work using Pygame to build an interactive game. Explore the sections below to learn more about my journey.

## Why Pygame?
  Pygame is an easy way to begin making 2-dimensional games that are highly interactive with the user. With Pygame's simple interface, beginners in game production may start without an extensive understanding of graphics programming pretty quickly. Learning Pygame is made simple by its comprehensive tutorials, examples, and supportive community you can find on places like Reddit. There is also scalability for Pygame projects too as there is a range of simple methods and packages it provides to complex ideas with features supporting hardware acceleration, sprite batching, and efficient event loops. Pygames can optimize graphics and support a lot of libraries. 
## How I Built My Project
I first built the game's main logic, I used a list of first and last names to loop in around 500 players with their respective personalities and statistics. Next was the games where I had to run loops for 3 innings. These innings maintained the 3-out frame from a traditional baseball game. The hitter's hitting statistic is compared to the pitcher's statistic that are created when the program is initially run. If the hitter stat is higher then it results in a hit and if the pitcher stat is higher than the result is an out. Hit type is decided on a weighted dice roll where its weighted as 50, 35, 5, 10. The results were single, double, triple, and Homerun, respectively. Now that the game logic was essentially finished, it was time for the screen building. You will play in a 69-game season with playoffs after. You will play 6 games against in-conference opponents and 4 games against out-of-conference opponents. 

I had a nice welcome screen where you could start or exit the game. It then transitions to a team selection screen where 20 teams of random city locations and mascots are and you can choose your favorite one. After your team is selected, the calendar screen will be displayed. It was all your games displayed with options to look at your lineup and play your next game. The playoff format is similar to the MLB format where 1st and 2nd conference seeds from each conference will move onto playoffs and face off in a division series that is a best of 5. Winners move onto a championship series where it's a best of 7 and then the winners of that will move on to the World Series where it is also a best of 7. 
## Challenges & Errors
The information carrying across screens was my hardest task as I could not find a way to correctly call the hitting and pitching statistics that were stored in the dictionaries as values of the created players. I also could not achieve multiple screen live updates as on the calendar screen you would have your live record of wins and losses be displayed but no matter if I used wins and losses as a global variable I would update upon playing a game.  

## Try It Out
To play, download the code from GitHub and run it using Python:


```sh
python main.py
```

[View on GitHub](https://github.com/YOUR-USERNAME/YOUR-REPO)
