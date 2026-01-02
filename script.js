function predictScore() {

    const data = {
        batting_team: document.getElementById("batting_team").value,
        bowling_team: document.getElementById("bowling_team").value,
        runs: document.getElementById("runs").value,
        wickets: document.getElementById("wickets").value,
        overs: document.getElementById("overs").value,
        runs_last_5: document.getElementById("runs_last_5").value,
        wickets_last_5: document.getElementById("wickets_last_5").value
    };

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        if (result.predicted_score) {
            document.getElementById("result").innerText =
                "Predicted Final Score: " + result.predicted_score;
        } else {
            document.getElementById("result").innerConfirm =
                "Error: " + result.error;
        }
    })
    .catch(error => {
        document.getElementById("result").innerText = "Error occurred";
    });
}
