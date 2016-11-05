<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-COMPATIBLE" content="IE=edge,chrome=1" />

        <script type="text/javascript" src="/assets/material/js/jquery.min.js"></script>
        <script type="text/javascript" src="/assets/material/js/bootstrap.min.js"></script>
        <script type="text/javascript" src="/assets/material/js/bootstrap-datepicker.js"></script>
        <script type="text/javascript" src="/assets/material/js/material.min.js"></script>
        <link href="/assets/material/css/bootstrap.min.css" rel="stylesheet" />
        <link href="/assets/material/css/material-kit.css" rel="stylesheet" />
        <link href="/assets/custom/css/custom.css" rel="stylesheet" />
        <title>Rejestracja konta</title>
    </head>
    <body class="signup-page">
        <nav class="navbar navbar-absolute">
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                         <span class="sr-only">Toggle navigation</span>
                         <span class="icon-bar"></span>
                         <span class="icon-bar"></span>
                         <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="#">Hotel</a>
                </div>

                <!-- Collect the nav links, forms, and other content for toggling -->
                     <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                       <ul class="nav navbar-nav">

                           % if example_dictionary['logged_in'] == 'true':
                                <li><a href="#">Look for room</a></li>
                                <li><a href="#">My reservations</a></li>
                           % else:
                                <li><a href="#">Register</a></li>
                                <li><a href="#">Log in</a></li>
                           % endif

                       </ul>
                     </div><!-- /.navbar-collapse -->
            </div>
        </nav>

        <div class="wrapper">
            ${self.body()}
        </div>

    </body>
</html>