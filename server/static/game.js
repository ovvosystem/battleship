socketio = io();

const playerBoard = document.getElementById("player-board");
const opponentBoard = document.getElementById("opponent-board");

socketio.on("getBoards", (boards) => {
    playerBoard.innerHTML = "";
    opponentBoard.innerHTML = "";

    for (let y = 0; y < boards.player_board.length; y++) {
        for (let x = 0; x < boards.player_board.length; x++) {
            tile = boards.player_board[y][x];
            tileDiv = renderTile(tile);
            tileDiv.dataset.x = x;
            tileDiv.dataset.y = y;
            playerBoard.appendChild(tileDiv);
        }
    }

    for (let y = 0; y < boards.opponent_board.length; y++) {
        for (let x = 0; x < boards.opponent_board.length; x++) {
            tile = boards.opponent_board[y][x];
            tileDiv = renderTile(tile);
            tileDiv.dataset.x = x;
            tileDiv.dataset.y = y;
            opponentBoard.appendChild(tileDiv);
        }
    }

    opponentTiles = opponentBoard.querySelectorAll(".grid-element");
    for (const tile of opponentTiles) {
        tileClickEvent(tile);
    }
})

socketio.on("getOpponent", (opponent) => {
    console.log(opponent);
    username = document.querySelector(".opponent-area p");
    username.textContent = opponent;
})

socketio.on("update", (change) => {
    const divPosition = (change.coords[1] * 10) + change.coords[0];
    divTile = renderTile(change.status);
    if (change.target) {
        playerBoard.children.item(divPosition).innerHTML = divTile.innerHTML;
    } else {
        opponentBoard.children.item(divPosition).innerHTML = divTile.innerHTML;
    }
})

function renderTile(tile) {
    const tileDiv = document.createElement("div");
    tileDiv.classList.add("grid-element", "flex", "flex-center");

    if (tile === "S") {
        tileDiv.innerHTML = '<div class="attacked ship-tile"></div>';
    } else if (tile === "O") {
        tileDiv.innerHTML = '<div class="attacked miss-tile"></div>';
    } else if (tile === "X") {
        tileDiv.innerHTML = '<div class="attacked hit-tile"></div>';
    }

    return tileDiv;
}

function tileClickEvent(tile) {
    tile.addEventListener("click", (event) => {
        const tile = event.currentTarget;
        const coords = [tile.dataset.x, tile.dataset.y];
        socketio.emit("attack", coords);
    });
}