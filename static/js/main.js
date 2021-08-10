function setCookie(cname,cvalue,ex) {
    const d = new Date();
    d.setTime(d.getTime() + (ex*60*1000));
    let expires = "expires=" + d.toGMTString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
  }
  
  function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }
  
  function checkCookie(cookie) {
    let view = getCookie(cookie);
    if (view != "") {
        //console.log(view);
    } else {
        view = cookie
       if (view != "" && view != null) {
         setCookie(cookie, view, 5);
         console.log("Vista nueva creada");
       }
    }
  }



