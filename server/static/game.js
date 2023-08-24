socketio = io();

socketio.on("update", (boards) => {
    console.log(boards.player_board);
    console.log(boards.opponent_board);
})