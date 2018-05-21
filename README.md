# ChessGame
my biggest challenge was getting a system to check for diagonals to work
it wasn't very easy to just check with a regular thing, because the position changes and it has to work every time
the way that I ended up fixing that problem was by making a couple functions that assigned numbers to each row and column
then adding up the rows and columns
this leads to a square that looks like this


__1__2__3__4__5__6__7__8
 
1_2__3__4__5__6__7__8__9

2_3__4__5__6__7__8__9__10

3_4__5__6__7__8__9__10_11

4_5__6__7__8__9__10_11_12

5_6__7__8__9__10_11_12_13

6_7__8__9__10_11_12_13_14

7_8__9__10_11_12_13_14_15

8_9__10_11_12_13_14_15_16

as you can see all the diagonals going one direction add to the same number
then i just made a method that checked whether the current position of the piece added to the same number 
as the position of the place where they wanted to move
then after checking that, I flipped the x numbers (1=8, 2=7, etc.) and checked again
that was my solution to finding if a diagonal move was legal or not
