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
    <form action="/me/update" method="post">
        <label for="name">Name:</label>
        <input name="name" id="name" class="form-control" type="text" value="${client_dict['name']}">
        <label for="surname">Surname:</label>
        <input name="surname" id="surname" class="form-control" type="text" value="${client_dict['surname']}">
        <button class="btn btn-lg btn-primary btn-block" type="submit">Update</button>
    </form>
</div>
</body>
</html>