<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
    <link href="/assets/bootstrap/css/bootstrap.min.css" rel="stylesheet"/>
    <title>Main</title></head>
<body> <%include file="shared/menu.mako"/>
<div class="container">
    <table class="table table-striped">
        <thead>
        <tr>
            <th>Room Name</th>
            <th>ID</th>
        </tr>
        </thead>
        <tbody>
        % for room in room_dict:
        <tr>
            <td>${room_dict[room]['name']}</td>
            <td>${str(room_dict[room]['id'])}</td>
        </tr>
        % endfor
        </tbody>
    </table>
</div>
</body>
</html>