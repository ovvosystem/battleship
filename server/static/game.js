socketio = io();

const playerBoard = document.getElementById("player-board");
const opponentBoard = document.getElementById("opponent-board");

socketio.on("update", (boards) => {
    playerBoard.innerHTML = "";
    opponentBoard.innerHTML = "";

    let x = 0;
    let y = 0;

    for (row of boards.player_board) {
        for (tile of row) {
            tileDiv = renderTile(tile);
            tileDiv.dataset.x = x;
            tileDiv.dataset.y = y;
            playerBoard.appendChild(tileDiv);
            x++;
        }
        x = 0;
        y++;
    }

    x = 0;
    y = 0;

    for (row of boards.opponent_board) {
        for (tile of row) {
            tileDiv = renderTile(tile);
            tileDiv.dataset.x = x;
            tileDiv.dataset.y = y;
            opponentBoard.appendChild(tileDiv);
            x++;
        }
        x = 0;
        y++;
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