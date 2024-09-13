function calculateDistribution(activeGameRooms) {
    let segments = [
        {min: 1, max: 5, count: 0, label: "1-5", color: "#33876b"},
        {min: 5, max: 10, count: 0, label: "5-10", color: "#559559"},
        {min: 10, max: 20, count: 0, label: "10-20", color: "#77a347"},
        {min: 20, max: 50, count: 0, label: "20-50", color: "#98b236"},
        {min: 50, max: Infinity, count: 0, label: "50+", color: "#e0e0e0"}
    ];

    for (let activeGameRoom of activeGameRooms) {
        for (let segment of segments) {
            if (activeGameRoom.gameResult >= segment.min && activeGameRoom.gameResult < segment.max) {
                segment.count++;
                break;
            }
        }
    }

    return segments.map((segment, index) => {
        return {
            id: index + 1,
            label: segment.label,
            value: (segment.count / activeGameRooms.length) * 100,
            color: segment.color,
        };
    });
}

function drawDonut(results) {
    const data = calculateDistribution(results)
    console.log(data)
    $("#graph").donutgraph({
        data: data,
        height: 400,
        width: 400,
        colorSetting: ["#33876b", "#559559", "#77a347", "#98b236", "#bac024", "#dcce12", "#e0e0e0"],

    });

}

function DrawPredictionTable(result) {
    console.log(result)
    $('#activePrediction').html(`
            <td>${result.roomId}</td>
            <td>${result.roundId}</td>
            <td>${result.prediction.toFixed(2)}</td>
            <td>${result.prediction3.toFixed(2)}</td>
            <td>${result.prediction4.toFixed(2)}</td>
    `)
}

function UpdateTableData(limit) {
    if (isNaN(+limit)) {
        return;
    }
    if (limit > 10) {
        limit = 10;
    }
    if (limit < 0) {
        limit = 0;
    }
    $.getJSON("/query/activeroom?orderByDesc=Id&take=" + limit, function (q) {
        if (q.results.length === 0) {
            return;
        }
        const roundIds = q.results.map(a => a.roundId);


        $.getJSON("/query/predicts?orderByDesc=Id&roundIds=" + roundIds.join(","), function (qp) {
            if (qp.results.length === 0) {
                return;
            }
            //DrawStdDevTable(qp.results);
            //DrawPredictionTable(qp.results[qp.results.length - 1])
            markUnderPredictions(q.results, qp.results)
            DrawLastResults(q.results);
            console.log(q.results)
        });
    });

}

function getPredictionClass(prediction) {
    switch (prediction) {
        case 'Unknown':
            return 'PredictionUnknown';
        case 'None':
            return 'PredictionNone';
        case 'Prediction3':
            return 'PredictionPrediction3';
        case 'Prediction4':
            return 'PredictionPrediction4';
        case 'Both':
            return 'PredictionBoth';
        default:
            return 'PredictionUnknown'; // for when there's no match
    }
}

function DrawLastResults(results) {
    $('#lastresults').fadeOut()
    $('#lastresults').empty()
    $('#lastresults').fadeIn()

    for (const item of results.reverse()) {
        const predictionClass = getPredictionClass(item.predictionHit)
        const safePredictionClass = getPredictionClass(item.SafeHit)
        $('#lastresults').append($(` <td>
           <div class="std-dev"><span class="font-bold">Round Id:</span> ${item.roundId}</div>
           <div class="game-result">${item.gameResult.toFixed(2)}</div>
            <div class="${predictionClass}">Exact: ${item.predictionHit} - ${item.predictionText}</div>
            <div class="std-dev"><span class="font-bold">Std Dev:</span> ${item.stdDev}</div>
            <div class="${safePredictionClass}">Safe? : ${item.SafeHit} - ${item.SafeText}</div>
 </td>`))
    }
}

function DrawHitOrMiss(results) {
    for (const item of results) {

        $('#lastresults').append($(`<td>${item.gameResult.toFixed(2)} </td>`))
    }
}

function markUnderPredictions(results, predictions) {
    debugger;
    for (const result of results) {
        let predictionIndex = predictions.findIndex(prediction => prediction.roundId === result.roundId);
        if (predictionIndex === -1) {
            result.predictionHit = "Not Found";
            result.stdDev = "-"
            result.predictionText = '';
            result.SafeHit = '';
            result.SafeText = ''
            continue;
        }
        const foundPrediction = predictions[predictionIndex];
        result.stdDev = foundPrediction.prediction.toFixed(2)

        if (foundPrediction.prediction3 < result.gameResult && result.gameResult - foundPrediction.prediction3 <= 1.0 && foundPrediction.prediction4 < result.gameResult && result.gameResult - foundPrediction.prediction4 <= 1.0) {
            result.predictionHit = "Both";
            result.predictionText = `${foundPrediction.prediction3.toFixed(2)}, ${foundPrediction.prediction4.toFixed(2)}`
        } else if (foundPrediction.prediction3 < result.gameResult && result.gameResult - foundPrediction.prediction3 <= 1.0) {
            result.predictionHit = "Prediction3";
            result.predictionText = `${foundPrediction.prediction3.toFixed(2)}`
        } else if (foundPrediction.prediction4 < result.gameResult && result.gameResult - foundPrediction.prediction4 <= 1.0) {
            result.predictionHit = "Prediction4";
            result.predictionText = `${foundPrediction.prediction4.toFixed(2)}`
        } else {
            result.predictionHit = "None";
            result.predictionText = '';
        }

        if (foundPrediction.prediction3 > 2 && foundPrediction.prediction4 > 2 && result.gameResult > 2) {
            result.SafeHit = "Both";
            result.SafeText = `${foundPrediction.prediction3.toFixed(2)}, ${foundPrediction.prediction4.toFixed(2)}`;
        } else if (foundPrediction.prediction3 > 2 && result.gameResult > 2) {
            result.SafeHit = "Prediction3";
            result.SafeText = `${foundPrediction.prediction3.toFixed(2)}`;
        } else if (foundPrediction.prediction4 > 2 && result.gameResult > 2) {
            result.SafeHit = "Prediction4";
            result.SafeText = `${foundPrediction.prediction4.toFixed(2)}`;
        } else {
            result.SafeHit = "None";
            result.SafeText = '';
        }
    }
}

function DrawStdDevTable(results) {
    $('#stddev').fadeOut()
    $('#stddev').empty()
    $('#stddev').fadeIn()
    for (const item of results) {

        $('#stddev').append($(`<td>${item.prediction.toFixed(2)}</td>`))
    }
}

function UpdateData(limit) {
    if (isNaN(+limit)) {
        return;
    }

    $.getJSON("/query/activeroom?orderByDesc=Id&take=" + limit, function (q) {
        const data = calculateDistribution(q.results)
        $("#graph").donutgraph("update", data);

    });
}

function LiveView() {
    drawDonut([])
    UpdateData(1000);
    $('#room_id').change(function () {
        const room_id = +$(this).val();
        
    })
    $('#limit-input').change(function () {
        const limit = +$(this).val();
        UpdateData(limit);

    });
    UpdateTableData(10);
    $('#limit-input2').change(function () {
        const limit = +$(this).val();
        UpdateTableData(limit);

    });
    $.getJSON("/query/predicts?orderByDesc=Id&take=1", function (qp) {
            if (qp.results.length === 0) {
                return;
            }

            DrawPredictionTable(qp.results[qp.results.length - 1])

        }
    )
    ;
    sseInit()


}

function sseInit() {
    const source = new EventSource('/event-stream?channels=LiveView&t=' + new Date().getTime());
    source.addEventListener('error', function (e) {
        console.log(e);

    }, false);
    $(source).handleServerEvents({
        handlers: {
            onConnect: function (u) {
                console.log(u);

            },
            onHeartbeat: function (msg, e) {
                if (console) console.log("onHeartbeat", msg, e);
            },
            NotifyLiveViewDataUpdatedPacket: function (msg, e) {

                $.getJSON("/query/predicts?orderByDesc=Id&take=1&id=" + msg.id, function (q) {
                    if (q.results.length === 0) {
                        return;
                    }
                    DrawPredictionTable(q.results[0])
                    UpdateData(+$('#limit-input').val());
                    UpdateTableData(+$('#limit-input2').val());
                });
                console.log(msg);
            },

        },

    });
}

window.addEventListener('DOMContentLoaded', LiveView);
