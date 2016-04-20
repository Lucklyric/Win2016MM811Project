/**
 * Created by Alvin on 2016-04-09.
 */
/**
 * Get cookie by name
 * @param cname
 * @returns {*}
 */
function getAdminCookie(cname) {
    var arr = document.cookie.match(new RegExp("(^| )" + cname + "=([^;]*)(;|$)"));
    if (arr != null) {
        return decodeURIComponent(arr[2]);
    }
    return null;
}

/**
 * set cookie by name value and time
 * @param cname
 * @param cvalue
 * @param min
 */
function setAdminCookie(cname, cvalue, min) {
    var exdate = new Date();
    exdate.setTime(exdate.getTime() + min * 60 * 1000);
    document.cookie = cname + "=" + escape(cvalue) + ((min == null) ? "" : ";expires=" + exdate.toGMTString()) + "; path=/";
    // console.log(cname + "=" + escape(cvalue) + ((min == null) ? "" : ";expires=" + exdate.toGMTString())+"; path=/");
}

/**
 * Delete the cookie by name
 * @param name
 */
function delCookie(name) {
    var exp = new Date();
    exp.setTime(exp.getTime() - 1);
    var cval = getAdminCookie(name);
    if (cval != null)
        document.cookie = name + "=" + cval + ";expires=" + exp.toGMTString();
}
//
