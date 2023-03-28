$(document).ready(function(){
    // alert('Hello');
    var sec = 0;
    var min = 0;
    function CallFun(){
        function pad ( val ) { return val > 9 ? val : "0" + val; }
        interval = setInterval( function(){
            $("#seconds").html(pad(++sec%60));
            //var mins = pad(parseInt(sec/60,10));
            $("#minutes").html(pad(parseInt(sec/60,10)));
            $("#hours").html(pad(parseInt(min/60,10)));
       }, 1000);
    }

    function RemoveCheckOutAlertMessage(){
        $('#check_out_message').addClass('display_none');
        $('#check_out_message').empty();
        // $('#check_out').addClass('display_none');
        // $('#check_out_frezz').removeClass('display_none');
    }

//    function DelayTime(){
////        inst = setInterval( function(){
////
////        }, 1000);
//        var dtl = new Date();
//        var dthours = dtl.getHours();
//        var dtsecons = dtl.getSeconds();
//        var minutes = dtl.getMinutes();
//        var a = ;
//        var delayTime = $('#dlytm').attr('value');
//        console.log(delayTime);
//        console.log(typeof(a))
//            // typeof(a);
//            // var delayTime = 1;
//        if(parseInt(delayTime) <= parseInt(a)){
//                //$('#check_out_frezz').addClass('display_none');
//            $('#check_out_frezz').addClass('display_none');
//            $('#check_out').removeClass('display_none');
//                //DisableTime();
//        }else{
//            $('#check_out').addClass('display_none');
//            $('#check_out_frezz').removeClass('display_none');
//        }
//
//    }

    function CurrentTimes(){
        var dt = new Date();
        var hours = dt.getHours();
        var secons = dt.getSeconds();
        var minutes = dt.getMinutes();
        var dtimes = $('#dlytm').attr('value');
        var totalminues = minutes+parseInt(dtimes);
        console.log(totalminues);
        var CheckOutTime = hours+":"+totalminues+":"+secons;
        $('#check_out_message').removeClass('display_none');
        $('#check_out_message').html('You can not Check out <b>before '+CheckOutTime+'</b>');
        var totlseconds = parseInt(dtimes)*60000;
        var plas = setTimeout(function(){
            $('#check_out').removeClass('display_none');
            $('#check_out').addClass('check_out_work');
            RemoveCheckOutAlertMessage();
        }, totlseconds);
    }


    // Check out btn Disable the button for while
    function PuseTheClick(){
        $('#check_out').off('click');
        var dtimes = $('#dlytm').attr('value');
        var totlseconds = parseInt(dtimes)*60000;
        setTimeout(() => {
            $('#check_out').on('click', function(){
                    //        $("#seconds").html(00);
                    //        $("#minutes").html(00);
                    //        $("#hours").html(00);
                            clearInterval(interval);
                            // clearInterval(inst);
                            $('#check_out').addClass('display_none');
                            $('#check_in').removeClass('display_none');
                            var dt = new Date();
                            $('.message').empty();
                            $('.message').html('GoodBye!');
                            $('.status').empty();
                            $('.status').html('Check In!');
                            var curenttime = dt.getUTCMonth()+1+"/"+dt.getUTCDate()+"/"+dt.getFullYear()+" "+ dt.getHours() + ":" + dt.getMinutes() + ":" + dt.getSeconds();
                            var csrfs = $('#csrf').val();
                            var emplyId = $('.employee_id').val();
                            //console.log(csrfs);
                            //var csrftoken = getCookie('csrftoken');
                            console.log(curenttime)
                            $.ajaxSetup({
                                headers: {
                                   'X-CSRF-TOKEN': $('#csrf').val()
                                }
                             });
                            $.ajax({
                                url: 'http://localhost:8069/my/checkout',
                                type:"POST",
                                data: {
                                    employee_id: emplyId,
                                    time: curenttime
                                },
                                success: function (response) {
                                    //alert(response.status);
                                    console.log(response);
                                },
                                error: function () {
                                    alert("error");
                                }
                            });
                        });
        }, totlseconds);
    }









    $('#check_in').click(function(){
        $(this).addClass('display_none');
        $('#check_out').removeClass('display_none');
        $('#check_out').removeClass('check_out_work');
        var dt = new Date();
        $('.message').html('WelCome!');
        $('.status').empty();
        $('.status').html('Check Out!');
        var curenttime = dt.getUTCMonth()+1+"/"+dt.getUTCDate()+"/"+dt.getFullYear()+" "+ dt.getHours() + ":" + dt.getMinutes() + ":" + dt.getSeconds();
        var csrfs = $('#csrf').val();
        var emplyId = $('.employee_id').val();
        CurrentTimes();
        PuseTheClick();
        //window.clearTimeout(timehandler);
        //DelayTime();
        //console.log(csrfs);
        //var csrftoken = getCookie('csrftoken');
        CallFun(); // minutes live count function
        //DelayTime(); //delay time check function
        console.log(curenttime);
        $.ajaxSetup({
            headers: {
               'X-CSRF-TOKEN': $('#csrf').val()
            }
         });
        $.ajax({
            url: 'http://localhost:8069/my/checkin',
            type:"POST",
            data: {
                employee_id: emplyId,
                time: curenttime
            },
            success: function (response) {
                //alert(response.status);
                console.log(response);
            },
            error: function () {
                alert("error");
            }
        });
    });




});