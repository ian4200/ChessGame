# ChessGame
my biggest challenge was getting a system to check for diagonals to work
it wasn't very easy to just check with a regular thing, because the position changes and it has to work every time
the way that I ended up fixing that problem was by making a couple functions that assigned numbers to each row and column
then adding up the rows and columns
this leads to a square that looks like this


 1  2  3  4  5  6  7  8
1 2  3  4  5  6  7  8  9
2 3  4  5  6  7  8  9  10
3 4  5  6  7  8  9  10 11
4 5  6  7  8  9  10 11 12
5 6  7  8  9  10 11 12 13
6 7  8  9  10 11 12 13 14
7 8  9  10 11 12 13 14 15
8 9  10 11 12 13 14 15 16

as you can see all the diagonals going one direction add to the same number
then i just made a method that checked whether the current position of the piece added to the same number 
as the position of the place where they wanted to move
then after checking that, I flipped the x numbers (1=8, 2=7, etc.) and checked again
that was my solution to finding if a diagonal move was legal or not
