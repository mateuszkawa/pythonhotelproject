<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="/assets/bootstrap/css/bootstrap.min.css" rel="stylesheet"/>
    <title>Main</title></head>
<body> <%include file="shared/menu.mako"/>
<div class="container">
    <form action="/rooms/filter" method="post">
        <label for="date_start">Date Start:</label>
        <input pattern="\d{4}/\d{2}/\d{2}" name="date_start" id="date_start" class="form-control" placeholder="2016/11/18" type="text">
        <label for="date_end">Date End:</label>
        <input pattern="\d{4}/\d{2}/\d{2}" name="date_end" id="date_end" class="form-control" placeholder="2016/11/21" type="text">
        <button class="btn btn-lg btn-primary btn-block" type="submit">Filter</button>
    </form>
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