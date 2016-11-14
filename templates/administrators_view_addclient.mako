<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
    <link href="/assets/bootstrap/css/bootstrap.min.css" rel="stylesheet"/>
    <title>Main</title>
</head>
<body>
<%include file="shared/menu.mako"/>
<div class="container">
    <form action="/administrators/addclient" method="post">
        <label for="name">Name:</label>
        <input name="name" id="name" class="form-control" type="text">
        <label for="surname">Surname:</label>
        <input name="surname" id="surname" class="form-control" type="text">
        <button class="btn btn-lg btn-primary btn-block" type="submit">Create</button>
    </form>
</div>
</body>
</html>