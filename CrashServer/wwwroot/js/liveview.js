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
            <td class="p-2"><span class="font-medium">${result.roomId}</span></td>
            <td class="p-2"><span class="font-medium">${result.roundId}</span></td>
            <td class="p-2"><span class="font-medium">${result.prediction.toFixed(2)}</span></td>
            <td class="p-2"><span class="font-medium">${result.prediction2.toFixed(2)}</span></td>
            <td class="p-2"><span class="font-medium">${result.prediction3.toFixed(2)}</span></td>
            <td class="p-2"><span class="font-medium">${result.prediction4.toFixed(2)}</span></td>
    `)
}

function UpdateTableData(limit) {
    if (isNaN(+limit)) {
        return;
    }
    if (limit > 25) {
        limit = 25;
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
        case 'Not Found':
            return 'PredictionUnknown';
        case 'None':
            return 'PredictionNone';
        case 'Prediction2':
            return 'PredictionPrediction2';
        case 'Prediction3':
            return 'PredictionPrediction3';
        case 'Prediction4':
            return 'PredictionPrediction4';
        case 'Prediction2and3':
            return 'PredictionPrediction2and3';
        case 'Prediction2and4':
            return 'PredictionPrediction2and4';
        case 'Prediction3and4':
            return 'PredictionPrediction3and4';
        case 'All':
            return 'PredictionAll';
        default:
            return 'PredictionUnknown'; // for when there's no match
    }
}
function DrawLastResults(results) {
    $('#lastresults').fadeOut()
    $('#lastresults').empty()
    $('#lastresults').fadeIn()

    for (const item of results.reverse()) {
        debugger;
        const predictionClass = getPredictionClass(item.predictionHit)
        const safePredictionClass = getPredictionClass(item.SafeHit)
        $('#lastresults').append($(` <td>
           <div class="std-dev"><span class="font-bold">Round Id:</span> ${item.roundId}</div>
           <div class="game-result">${item.gameResult.toFixed(2)}</div>
            <div class="${predictionClass}">Exact  ${item.predictionText}</div>
            <div class="std-dev"><span class="font-bold">Std Dev:</span> ${item.stdDev}</div>
            <div class="${safePredictionClass}">Safe  ${item.SafeText}</div>
 </td>`))
    }
}

function DrawHitOrMiss(results) {
    for (const item of results) {

        $('#lastresults').append($(`<td>${item.gameResult.toFixed(2)} </td>`))
    }
}
function markUnderPredictions(results, predictions) {
    for (const result of results) {
        let predictionIndex = predictions.findIndex(prediction => prediction.roundId === result.roundId);
        if (predictionIndex === -1) {
            result.predictionHit = "Not Found";
            result.stdDev = "-";
            result.predictionText = '';
            result.SafeHit = '';
            result.SafeText = '';
            continue;
        }
        const foundPrediction = predictions[predictionIndex];
        result.stdDev = foundPrediction.prediction.toFixed(2);

        // Check predictions
        const pred2Hit = foundPrediction.prediction2 < result.gameResult && result.gameResult - foundPrediction.prediction2 <= 1.0;
        const pred3Hit = foundPrediction.prediction3 < result.gameResult && result.gameResult - foundPrediction.prediction3 <= 1.0;
        const pred4Hit = foundPrediction.prediction4 < result.gameResult && result.gameResult - foundPrediction.prediction4 <= 1.0;

        // Determine predictionHit and predictionText
        if (pred2Hit && pred3Hit && pred4Hit) {
            result.predictionHit = "All";
            result.predictionText = `All : ${foundPrediction.prediction2.toFixed(2)}, ${foundPrediction.prediction3.toFixed(2)}, ${foundPrediction.prediction4.toFixed(2)}`;
        } else if (pred2Hit && pred3Hit) {
            result.predictionHit = "Prediction2and3";
            result.predictionText = `2 , 3 : ${foundPrediction.prediction2.toFixed(2)}, ${foundPrediction.prediction3.toFixed(2)}`;
        } else if (pred2Hit && pred4Hit) {
            result.predictionHit = "Prediction2and4";
            result.predictionText = `2 , 4 : ${foundPrediction.prediction2.toFixed(2)}, ${foundPrediction.prediction4.toFixed(2)}`;
        } else if (pred3Hit && pred4Hit) {
            result.predictionHit = "Prediction3and4";
            result.predictionText = `3 , 4 :${foundPrediction.prediction3.toFixed(2)}, ${foundPrediction.prediction4.toFixed(2)}`;
        } else if (pred2Hit) {
            result.predictionHit = "Prediction2";
            result.predictionText = `2 : ${foundPrediction.prediction2.toFixed(2)}`;
        } else if (pred3Hit) {
            result.predictionHit = "Prediction3";
            result.predictionText = `3 : ${foundPrediction.prediction3.toFixed(2)}`;
        } else if (pred4Hit) {
            result.predictionHit = "Prediction4";
            result.predictionText = `4 : ${foundPrediction.prediction4.toFixed(2)}`;
        } else {
            result.predictionHit = "None";
            result.predictionText = '';
        }

        // Check safe predictions
        const safe2 = foundPrediction.prediction2 > 2 && result.gameResult > 2;
        const safe3 = foundPrediction.prediction3 > 2 && result.gameResult > 2;
        const safe4 = foundPrediction.prediction4 > 2 && result.gameResult > 2;

        // Determine SafeHit and SafeText
        if (safe2 && safe3 && safe4) {
            result.SafeHit = "All";
            result.SafeText = `All : ${foundPrediction.prediction2.toFixed(2)}, ${foundPrediction.prediction3.toFixed(2)}, ${foundPrediction.prediction4.toFixed(2)}`;
        } else if (safe2 && safe3) {
            result.SafeHit = "Prediction2and3";
            result.SafeText = `2 , 3 : ${foundPrediction.prediction2.toFixed(2)}, ${foundPrediction.prediction3.toFixed(2)}`;
        } else if (safe2 && safe4) {
            result.SafeHit = "Prediction2and4";
            result.SafeText = `2 , 4 : ${foundPrediction.prediction2.toFixed(2)}, ${foundPrediction.prediction4.toFixed(2)}`;
        } else if (safe3 && safe4) {
            result.SafeHit = "Prediction3and4";
            result.SafeText = `3 , 4 : ${foundPrediction.prediction3.toFixed(2)}, ${foundPrediction.prediction4.toFixed(2)}`;
        } else if (safe2) {
            result.SafeHit = "Prediction2";
            result.SafeText = `2 : ${foundPrediction.prediction2.toFixed(2)}`;
        } else if (safe3) {
            result.SafeHit = "Prediction3";
            result.SafeText = `3 : ${foundPrediction.prediction3.toFixed(2)}`;
        } else if (safe4) {
            result.SafeHit = "Prediction4";
            result.SafeText = `4 : ${foundPrediction.prediction4.toFixed(2)}`;
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
    UpdateTableData(14);
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
