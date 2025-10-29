# five-lines

In this kata your task is to refactor the code for a small game. When finished it should be easy to add new tile types, or make the key draw as a circle, so we can easily distinguish it from the lock. 

The code already abides by the most common principles "Don't Repeat Yourself", "Keep It Simple, Stupid", and there are only very few magic literals. There are no poorly structured nor deeply nested `if`s.

This is *not* an easy exercise.

# About the Game
In the game, you are a red square and have to get the box (brown) to the lower right corner. Obstacles include falling stones (blue), walls (gray), and a lock (yellow, right) that can be unlocked with the key (yellow, left). You can push one stone or box at a time, and only if it is not falling. The flux (greenish) holds up boxes and stones but can be 'eaten' by the player. 

![Screenshot of the game](game.png)

# How to Build It
Assuming that you have the Typescript compiler installed: Open a terminal in this directory, then run `tsc`. There should now be a `index.js` file in this directory.

# How to Run It
To run the game you need to first build it, see above. Then simply open `index.html` in a browser. Use the arrows to move the player.

# Thank You!
If you like this kata please consider giving the repo a star. You might also consider purchasing a copy of my book where I show a simple way to tackle code like this: [Five Lines of Code](https://www.manning.com/books/five-lines-of-code), available through the Manning Early Access Program.

[![Five Lines of Code](frontpage.png)](https://www.manning.com/books/five-lines-of-code)

If you have feedback or comments on this repo don't hesitate to write me a message or send me a pull request. 

Thank you for checking it out.

----

Запуск:
python -m http.server 5173
http://localhost:5173/
http://localhost:5173/five-lines/


----

1. Tile в идеале может иметь только ссылку на Cell и Player (например принимать через параметры функций)

2. cell.down().isAir() способ определениея возможности падать

3. isAir() переименовать в isEmpty()

4. getBlockOnTopState - реализовать логическую операцию И 

5. premove - скорее всего не нужен, все это можно поместить в onEnterTile

6. cell должна хранить в себе координаты, координаты ячеек не меняются, только содержимое

7. this.map2D[y][x] заменить на приватное getCell(p: Position)

8. f(this.map2D[y][x], new Position(x,y - что бы такого не было Cell Должна возвращать Position а получать при инициализации

9. вернуть грядку как то по чему можно ходить

10. Разместить грядку под отодвигаемям камнем

11. Убрать класс Layer полностью

12. Ghb gj