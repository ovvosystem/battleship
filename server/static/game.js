socketio = io();

const playerBoard = document.getElementById("player-board");
const opponentBoard = document.getElementById("opponent-board");

socketio.on("update", (boards) => {
    for (let y = 0; y < boards.player_board.length; y++) {
        for (let x = 0; x < boards.player_board.length; x++) {
            tile = boards.player_board[y][x]
            tileDiv = renderTile(tile);
            tileDiv.dataset.x = x;
            tileDiv.dataset.y = y;
            playerBoard.appendChild(tileDiv);
        }
    }

    for (let y = 0; y < boards.opponent_board.length; y++) {
        for (let x = 0; x < boards.opponent_board.length; x++) {
            tile = boards.opponent_board[y][x]
            tileDiv = renderTile(tile);
            tileDiv.dataset.x = x;
            tileDiv.dataset.y = y;
            opponentBoard.appendChild(tileDiv);
        }
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