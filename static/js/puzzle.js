document.addEventListener("DOMContentLoaded", () => {
  const puzzleBoard = document.getElementById("puzzle-board");
  const shuffleButton = document.getElementById("shuffle-button");
  const solveButton = document.getElementById("solve-button");

  function renderBoard(state) {
    puzzleBoard.innerHTML = "";
    state.split("").forEach((tile) => {
      const tileElement = document.createElement("div");
      tileElement.className = "tile";
      if (tile === " ") {
        tileElement.classList.add("empty");
      } else {
        tileElement.textContent = tile;
        tileElement.addEventListener("click", () => moveTile(tile));
      }
      puzzleBoard.appendChild(tileElement);
    });
  }

  function shuffleBoard() {
    fetch("/shuffle")
      .then((response) => response.json())
      .then((data) => renderBoard(data.state));
  }

  function moveTile(tile) {
    const state = Array.from(puzzleBoard.children)
      .map((tile) => tile.textContent || " ")
      .join("");
    fetch(`/move?state=${state}&tile=${tile}`)
      .then((response) => response.json())
      .then((data) => renderBoard(data.state));
  }

  function solveBoard() {
    const state = Array.from(puzzleBoard.children)
      .map((tile) => tile.textContent || " ")
      .join("");
    fetch(`/solve?state=${state}`)
      .then((response) => response.json())
      .then((data) => {
        if (data.solution) {
          let idx = 0;
          const interval = setInterval(() => {
            if (idx >= data.solution.length) {
              clearInterval(interval);
            } else {
              renderBoard(data.solution[idx]);
              idx++;
            }
          }, 500);
        } else {
          alert("No solution found");
        }
      });
  }

  shuffleButton.addEventListener("click", shuffleBoard);
  solveButton.addEventListener("click", solveBoard);

  shuffleBoard();
});
