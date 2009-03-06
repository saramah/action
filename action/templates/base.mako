<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta name="author" content="Sarah G Barbour" />
    
    <title>Ferocious Kitten</title>

    <!--stylesheets-->
    <link rel="stylesheet" href="css/colors.css" type="text/css" />
    <link rel="stylesheet" href="css/layout.css" type="text/css" />
    <link rel="stylesheet" href="css/markup.css" type="text/css" />
    <!--javascript-->
    <script type = "text/javascript">
        function complete(){
        }
    </script>
</head>
<body>
    <div class="navigation">
        ${h.link_to('home', h.url_for(action="index", title="home"))} 
    </div>
    <div class="content">
        ${next.body()}
    </div>
</body>
</html>
