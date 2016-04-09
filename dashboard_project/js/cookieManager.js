/**
 * Created by Alvin on 2016-04-09.
 */
function getAdminCookie(cname) {
    var arr = document.cookie.match(new RegExp("(^| )" + cname + "=([^;]*)(;|$)"));
    if (arr != null) {
        return decodeURIComponent(arr[2]);
    }
    return null;
}

function setAdminCookie(cname, cvalue, min) {
    var exdate = new Date();
    exdate.setTime(exdate.getTime() + min * 60 * 1000);
    document.cookie = cname + "=" + escape(cvalue) + ((min == null) ? "" : ";expires=" + exdate.toGMTString()) + "; path=/";
    // console.log(cname + "=" + escape(cvalue) + ((min == null) ? "" : ";expires=" + exdate.toGMTString())+"; path=/");
}

//É¾³ýcookies
function delCookie(name) {
    var exp = new Date();
    exp.setTime(exp.getTime() - 1);
    var cval = getAdminCookie(name);
    if (cval != null)
        document.cookie = name + "=" + cval + ";expires=" + exp.toGMTString();
}
//
