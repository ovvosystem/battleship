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
        tile.addEventListener("click", tileAttack);
    }
})

socketio.on("getOpponent", (opponent) => {
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

socketio.on("gameover", (winner) => {
    const roomContainer = document.getElementById("room-container");
    const gameContainer = document.getElementById("game-container");
    gameContainer.classList.add("gameover");
    
    const gameoverText = document.createElement("div");
    gameoverText.classList.add("gameover-text", "flex", "flex-column", "gap-medium");
    gameoverText.innerHTML = `<h1 class="text-xl text-center text-bold">GAME OVER</h1>
                                <p class="text-l text-center text-bold">${winner} wins!</p>`;
    roomContainer.insertBefore(gameoverText, gameContainer);

    opponentTiles = opponentBoard.querySelectorAll(".grid-element");
    for (const tile of opponentTiles) {
        tile.removeEventListener("click", tileAttack);
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

function tileAttack(event) {
    const tile = event.currentTarget;
    const coords = [tile.dataset.x, tile.dataset.y];
    socketio.emit("attack", coords);
}