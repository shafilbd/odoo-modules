$(document).ready(function() {
    var Status = $('.ApprovalStatus').html();
    console.log(Status);
    if(Status == 'To Approve'){
        $('.ApprovalStatus').css({'background': '#F3C973'});
    }
    else if(Status == 'Refused'){
        $('.ApprovalStatus').css({'background': '#f44336', 'color': '#fff'});
    }
    else if(Status == 'Approved'){
        $('.ApprovalStatus').css({'background': '#4CAF50', 'color': '#fff'});
        $(".enable").attr('href', '#');
        $(".enable").removeClass('btn-outline-success');
        $(".enable").addClass('btn-outline-danger');
    }
    else{
        $('#ApprovalStatus').css('background', 'transparent');
    }
    $(function() {
        $("#DateFrom").datepicker({});
    });
    $(function() {
        $("#DateTo").datepicker({});

    });
    $('#DateFrom').change(function() {
        startDate = $(this).datepicker('getDate');
        $("#DateTo").datepicker("option", "minDate", startDate);
    });
    $('#DateTo').change(function() {
        endDate = $(this).datepicker('getDate');
        $("#DateFrom").datepicker("option", "maxDate", endDate);
        func();
    });
    function func() {
        var date1 = $("#DateFrom").val();
        var date2 = $("#DateTo").val();
        date1 = new Date(date1);
        date2 = new Date(date2);
        console.log(date1);
        var milli_secs = date1.getTime() - date2.getTime();
        console.log(milli_secs);
        // Convert the milli seconds to Days
        var days = milli_secs / (1000 * 3600 * 24);
        document.getElementById("durations").value = Math.round(Math.abs(days));
    }

    $('#submitBtn').on('click', function(){
        var dayoffType = $('#offtype').val();
        var employee_id = $('#employee_id').val();
        var DayOffDateStart = $('#DateFrom').val();
        var DateToEnd = $('#DateTo').val();
        var TotalDayDurations = $('#durations').val();
        var Description = $('#description').val();
        var AdditionalFiles = $('#AdditionalFile').val();
        console.log(dayoffType, employee_id, DayOffDateStart, DateToEnd, TotalDayDurations, Description, AdditionalFiles);
        var form = new FormData();
        var file = $('#AdditionalFile').prop("files")[0];
        console.log(file);
        form.append("DayoffTypes", dayoffType);
        form.append("EmployeeId", employee_id);
        form.append("DayStart", DayOffDateStart);
        form.append("DateEnd", DateToEnd);
        form.append("Durations", TotalDayDurations);
        form.append("Descrip", Description);
        form.append("file", file);
//      var file = $('#AdditionalFile').prop("files")[0];
//      var form = new FormData();
//      form.append("file", file);
        // AddiFiles: form,
        // console.log(form);
//        {
//            DayoffTypes: dayoffType,
//            EmployeeId: employee_id,
//            DayStart: DayOffDateStart,
//            DateEnd: DateToEnd,
//            Durations: TotalDayDurations,
//            Descrip: Description,
//        }

        $.ajax({
            url: 'http://localhost:8069/my/apply-for-dayoff',
            type: "POST",
            data: form,
            success: function (response) {
                //alert(response.status);
                console.log(response);
            },
            error: function () {
                alert("error");
            }
        });
    });
    $('.attachment_update').click(function(){
        $('.attachment').hide();
        location.reload(true);
    });
});