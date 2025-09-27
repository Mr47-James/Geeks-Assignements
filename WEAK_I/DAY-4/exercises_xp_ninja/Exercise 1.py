import time
from typing import Iterable, Set, Tuple, Optional

Cell = Tuple[int, int] 


class GameOfLife:
    def __init__(
        self,
        width: Optional[int] = 20,
        height: Optional[int] = 10,
        initial_live: Optional[Iterable[Cell]] = None,
        fixed: bool = True,
        max_border: int = 10000,
    ):
    
        if fixed and (width is None or height is None):
            raise ValueError("Fixed mode requires width and height.")
        if not fixed:
            self.width = None
            self.height = None
        else:
            self.width = int(width)
            self.height = int(height)

        self.fixed = bool(fixed)
        self.max_border = int(max_border)
        self.live: Set[Cell] = set()
        if initial_live:
            for c in initial_live:
                self._add_cell(c)

    def _in_bounds(self, cell: Cell) -> bool:
        if self.fixed:
            x, y = cell
            return 0 <= x < self.width and 0 <= y < self.height
        else:
            return True

    def _add_cell(self, cell: Cell):
        if self._in_bounds(cell):
            self.live.add(cell)

    @staticmethod
    def _neighbors(cell: Cell):
        x, y = cell
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                yield (x + dx, y + dy)

    def step(self):

        new_live: Set[Cell] = set()
        candidates = set()

        for cell in self.live:
            candidates.add(cell)
            for n in self._neighbors(cell):
                candidates.add(n)

        for cell in candidates:
            if self.fixed and not self._in_bounds(cell):
              
                continue

            live_neighbors = sum((1 for n in self._neighbors(cell) if n in self.live and (self.fixed and self._in_bounds(n) or not self.fixed)))
            if cell in self.live:
       
                if live_neighbors == 2 or live_neighbors == 3:
                    new_live.add(cell)
            else:
         
                if live_neighbors == 3:
                    new_live.add(cell)

    
        if not self.fixed and new_live:
            xs = [c[0] for c in new_live]
            ys = [c[1] for c in new_live]
            span_x = max(xs) - min(xs) + 1
            span_y = max(ys) - min(ys) + 1
            if span_x > self.max_border or span_y > self.max_border:
                raise MemoryError("Bounding box exceeded max_border; simulation aborted for safety.")

        self.live = new_live

    def display(self, padding: int = 2) -> None:
     
        if not self.live:
            
            print("(empty world)")
            return

        if self.fixed:
            min_x, max_x = 0, self.width - 1
            min_y, max_y = 0, self.height - 1
        else:
            xs = [c[0] for c in self.live]
            ys = [c[1] for c in self.live]
            min_x, max_x = min(xs) - padding, max(xs) + padding
            min_y, max_y = min(ys) - padding, max(ys) + padding
            span_x = max_x - min_x + 1
            span_y = max_y - min_y + 1
            if span_x > self.max_border or span_y > self.max_border:
                raise MemoryError("Display area would exceed max_border; aborting display for safety.")

        for y in range(min_y, max_y + 1):
            row_chars = []
            for x in range(min_x, max_x + 1):
                if (x, y) in self.live:
                    row_chars.append("#")
                else:
                    row_chars.append(".")
            print("".join(row_chars))

    def run(
        self,
        max_generations: int = 200,
        pause: float = 0.2,
        verbose: bool = True,
        detect_repeats: bool = True,
    ) -> dict:
        
        history = set()
        gen = 0

        def snapshot():
           
            return frozenset(self.live)

        if verbose:
            print(f"Starting simulation. Mode: {'Fixed' if self.fixed else 'Expandable'}")
        while gen <= max_generations:
            if verbose:
                print(f"\nGeneration {gen}")
                self.display()
            snap = snapshot()
            if not self.live:
                if verbose:
                    print("\nAll cells are dead: simulation ended.")
                return {"result": "extinct", "generation": gen, "live_count": 0}
            if detect_repeats:
                if snap in history:
                    if verbose:
                        print("\nConfiguration repeated: reached steady state or oscillator. Simulation ended.")
                    return {"result": "repeat", "generation": gen, "live_count": len(self.live)}
                history.add(snap)

            if gen == max_generations:
                if verbose:
                    print("\nReached maximum generations: simulation ended.")
                return {"result": "max_generations", "generation": gen, "live_count": len(self.live)}

          
            self.step()
            gen += 1
            if pause > 0 and verbose:
                try:
                    time.sleep(pause)
                except KeyboardInterrupt:
                    if verbose:
                        print("\nInterrupted by user.")
                    return {"result": "interrupted", "generation": gen, "live_count": len(self.live)}


        return {"result": "stopped", "generation": gen, "live_count": len(self.live)}




def translate(pattern: Iterable[Cell], dx=0, dy=0):
    return [(x + dx, y + dy) for (x, y) in pattern]


BLOCK = [(1, 1), (1, 2), (2, 1), (2, 2)]
BLINKER = [(1, 0), (1, 1), (1, 2)]
GLIDER = [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]
R_PENTOMINO = [(1, 0), (2, 0), (0, 1), (1, 1), (1, 2)]




def demo():
    print("Game of Life demos\n===================\n")

    print("Demo 1: Block (still life) — fixed grid")
    game1 = GameOfLife(width=6, height=6, initial_live=BLOCK, fixed=True)
    res1 = game1.run(max_generations=10, pause=0.25)
    print("Result:", res1)
    print("\n" + "=" * 40 + "\n")
    time.sleep(0.5)

    print("Demo 2: Blinker (oscillator) — fixed grid")
    game2 = GameOfLife(width=7, height=7, initial_live=translate(BLINKER, dx=3, dy=2), fixed=True)
    res2 = game2.run(max_generations=10, pause=0.25)
    print("Result:", res2)
    print("\n" + "=" * 40 + "\n")
    time.sleep(0.5)

    print("Demo 3: Glider — expandable grid (bonus)")
    game3 = GameOfLife(width=None, height=None, initial_live=translate(GLIDER, dx=2, dy=2), fixed=False, max_border=200)
    res3 = game3.run(max_generations=30, pause=0.15)
    print("Result:", res3)
    print("\n" + "=" * 40 + "\n")
    time.sleep(0.5)

   
    print("Demo 4: R-pentomino — expandable grid (chaotic behavior)")
    game4 = GameOfLife(width=None, height=None, initial_live=translate(R_PENTOMINO, dx=20, dy=10), fixed=False, max_border=500)
    res4 = game4.run(max_generations=200, pause=0.05)
    print("Result:", res4)
    print("\nDemos finished.")


if __name__ == "__main__":
    demo()
