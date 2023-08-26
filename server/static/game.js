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

    opponentTiles = opponentBoard.querySelectorAll(".grid-element");
    for (const tile of opponentTiles) {
        tile.addEventListener("click", (event) => {
            const tile = event.currentTarget;
            const coords = [tile.dataset.x, tile.dataset.y];
            socketio.emit("attack", coords);
    });
}
})

function renderTile(tile) {
    const tileDiv = document.createElement("div");
    tileDiv.classList.add("grid-element", "flex", "flex-center");

    if (tile === "S") {
        tileDiv.innerHTML = '<div class="ship-tile"></div>'
    } else if (tile === "O") {
        tileDiv.innerHTML = '<div class="miss-tile"></div>'
    } else if (tile === "X") {
        tileDiv.innerHTML = '<div class="hit-tile"></div>'
    }

    return tileDiv;
}