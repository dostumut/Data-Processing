$(document).ready(function () {
    $('#run-number-of-events').click(function () {
        $.post('/run_amount_of_events_per_application', function (data) {
            var job_id = data.job_id;
            var interval = setInterval(function () {
                $.getJSON('/poll_state',
                    {'job_id': job_id},
                    function (data) {
                        if (data.state === "PROGRESS") {
                            console.log(JSON.stringify(data));
                            $('#number-of-events-progress')
                                .text('Progress: ' + ((data.result.current / data.result.total) * 100).toFixed(2) + '%');
                        }
                        if (data.state === "SUCCESS") {
                            clearInterval(interval);
                            window.location = '/amount_of_events_result?job_id=' + job_id;
                        }
                    });
            }, 1000);
        });
    });
    
    //run amount of launch 
    $('#run-number-of-launch').click(function () {
        $.post('/run_amount_of_launch', function (data) {
            var job_id = data.job_id;
            var interval = setInterval(function () {
                $.getJSON('/poll_state',
                    {'job_id': job_id},
                    function (data) {
                        if (data.state === "PROGRESS") {
                            console.log(JSON.stringify(data));
                            $('#number-of-launch-progress')
                                .text('Progress: ' + ((data.result.current / data.result.total) * 100).toFixed(2) + '%');
                        }
                        if (data.state === "SUCCESS") {
                            clearInterval(interval);
                            window.location = '/amount_of_launch_result?job_id=' + job_id;
                        }
                    });
            }, 1000);
        });
    });

    //run duplicate events
    $('#run-find-duplicates').click(function () {
        $.post('/run_amount_of_duplicates', function (data) {
            var job_id = data.job_id;
            var interval = setInterval(function () {
                $.getJSON('/poll_state',
                    {'job_id': job_id},
                    function (data) {
                        if (data.state === "PROGRESS") {
                            console.log(JSON.stringify(data));
                            $('#number-of-duplicates-progress')
                                .text('Progress: ' + ((data.result.current / data.result.total) * 100).toFixed(2) + '%');
                        }
                        if (data.state === "SUCCESS") {
                            clearInterval(interval);
                            window.location = '/amount_of_duplicates_result?job_id=' + job_id;
                        }
                    });
            }, 1000);
        });
    });


});
