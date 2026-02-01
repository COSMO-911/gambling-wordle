# gambling-wordle
If u win the wordle game (where u have to guess 5 letter words based on hints) your bet amount doubles , else you lose that money


**PROJECT STRUCTURE**
- the __main__ file has loggin and signin feature; before playing you have to log in / sign in using your name and password which gets stored in a binary file 'user_detail.dat' .
- the 'gambling_wordle.py' file has the whole game logic.
- 'random-word.txt' file contains many different 5 letter enlish word , the programs picks one random word from this .txt file in order for you to play wordle and guess the choosen word.



**ABOUT WORDLE -**
Wordle is a logic-based word puzzle where your goal is to identify a secret five-letter word within a set number of attempts.
After each guess, the game provides feedback through three colored signals:
-  green indicates a letter is correct and in the right position,
-  yellow means the letter is in the word but currently in the wrong spot,
-  gray or black means the letter does not appear in the word at all.
To play effectively, you must use these clues to narrow down possibilities, eliminating incorrect letters and repositioning correct ones until the exact word is revealed.



**ABOUT THE GAME -**
 -  After you log in or sign in. You'll get $10k for starting the game 
 -  You bet an amount (say 100)
 -  Now you'll play the Wordle game
 -  If you win, you recover your bet plus winnings (e.g., bet $100, total balance becomes $10,100)
 -  If you lose, your bet amount gets subtracted from your balance (balance now = $ 9900 , bet amout got subtracted)
 -  You can play the game till u run out of money or you simply choose to quit 
 -  After quitting, all progress will be lost; however, you will receive $10k again when you log back in.
 



