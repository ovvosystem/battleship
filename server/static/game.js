socketio = io();

const playerBoard = document.getElementById("player-board");
const opponentBoard = document.getElementById("opponent-board");

socketio.on("update", (boards) => {
    playerBoard.innerHTML = "";
    opponentBoard.innerHTML = "";

    for (row of boards.player_board) {
        for (tile of row) {
            playerBoard.appendChild(renderTile(tile));
        }
    }

    for (row of boards.opponent_board) {
        for (tile of row) {
            opponentBoard.appendChild(renderTile(tile));
        }
    }
})

function renderTile(tile) {
    const tileDiv = document.createElement("div");
    tileDiv.classList.add("grid-element", "flex", "flex-center");

    if (tile === "S") {
        tileDiv.classList.add("ship-tile");
    } else if (tile === "O") {
        tileDiv.classList.add("miss-tile");
    } else if (tile === "X") {
        tileDiv.classList.add("hit-tile");
    }

    return tileDiv;
}