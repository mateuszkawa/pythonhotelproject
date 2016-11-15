<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="/assets/bootstrap/css/bootstrap.min.css" rel="stylesheet"/>
    <title>Login</title>
</head>
<body>
<div class="container">
    <div class="row">
        <div class="col-md-4 col-md-offset-4 col-sm-6 col-sm-offset-3">
            <div class="card card-signup">
                <form class="form-signin" action="/hotel/rest/register" method="post">
                    <input id="Login" name="Login" type="text" class="form-control" placeholder="Login..." />
                    <input id="Password" name="Password" type="password" placeholder="Password..." class="form-control"/>
                    <input id="FirstName" name="FirstName" type="text" class="form-control" placeholder="First Name..."/>
                    <input id="LastName" name="LastName" type="text" class="form-control" placeholder="Last Name..."/>
                    <button class="btn btn-lg btn-primary btn-block" type="submit">Register</button>
                </form>
            </div>
        </div>
    </div>
</div>
</body>
</html>