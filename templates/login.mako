<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
    <link href="/assets/bootstrap/css/bootstrap.min.css" rel="stylesheet"/>
    <title>Login</title>
</head>
<body>
<div class="container">
    <div class="row">
        <div class="col-md-4 col-md-offset-4 col-sm-6 col-sm-offset-3">
            <div class="card card-signup">
                <form class="form-signin" action="/hotel/rest/login" method="post">
                    <h2 class="form-signin-heading">Please Login</h2>
                    <label for="inputLogin" class="sr-only">Login</label>
                    <input name="inputLogin" id="inputLogin" class="form-control" placeholder="Login" required="" autofocus=""
                           type="text">
                    <label for="inputPassword" class="sr-only">Password</label>
                    <input name="inputPassword" id="inputPassword" class="form-control" placeholder="Password" required="" type="password">
                    <button class="btn btn-lg btn-primary btn-block" type="submit">Login</button>
                </form>
            </div>
        </div>
    </div>
</div>
</body>
</html>