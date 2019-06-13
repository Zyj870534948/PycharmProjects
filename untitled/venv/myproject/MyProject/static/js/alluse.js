myself_ip = '192.168.3.18'
myself_port='8888'

// 调用接口的aip和port
api_ip='api.robot.nplus5.com'

document.write("<script language=javascript src='http://" + myself_ip + "/libs/qi/2/qi.js'></script>");
// document.write("<script language=javascript src='http://192.168.43.179/libs/qi/2/qi.js'></script>");
document.write("<script src=\"../static/js/jquery.min.js\"></script>");
document.write("<link href=\"../static/css/style.css\" rel=\"stylesheet\">");
document.write("<link href=\"../static/css/animate.css\" rel=\"stylesheet\">");

function getId(f) {
    $.get("http://"+myself_ip+":"+myself_port+"/id", function (data, status) {
        f(data);
    });
}





