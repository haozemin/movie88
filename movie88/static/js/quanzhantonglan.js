var url=location.search;url=url.substr(1);var bs={versions:function(){var u=navigator.userAgent,app=navigator.appVersion;return{trident:u.indexOf("Trident")>-1,presto:u.indexOf("Presto")>-1,webKit:u.indexOf("AppleWebKit")>-1,gecko:u.indexOf("Gecko")>-1&&u.indexOf("KHTML")==-1,mobile:!!u.match(/AppleWebKit.*Mobile.*/)||!!u.match(/AppleWebKit/),ios:!!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/),android:u.indexOf("Android")>-1||u.indexOf("Linux")>-1,iPhone:u.indexOf("iPhone")>-1,iPad:u.indexOf("iPad")>-1}}(),language:(navigator.browserLanguage||navigator.language).toLowerCase()};var flag=true;if(bs.versions.mobile&&url!="mobile"){if(bs.versions.android||bs.versions.iPhone||bs.versions.iPad||bs.versions.ios){flag=false}}if(flag){document.writeln('<span style="color:#006600;">通知1：</span><span style="color:red;">由于不可抗原因，爱奇艺，优酷，腾讯视频，芒果TV等收费视频解析会出现波动或者打不开的现象，请重试几次更换其他线路！谢谢大家！</span><br/><span style="color:#006600;">通知2：</span><span style="color:red;">不推荐大家使用QQ浏览器,以防被QQ浏览器拦截访问。</span>')}else{};