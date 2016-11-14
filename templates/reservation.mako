<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="/assets/bootstrap/css/bootstrap.min.css" rel="stylesheet"/>
    <title>Main</title></head>
<body> <%include file="shared/menu.mako"/>
<div class="container">
    <form action="/reservation/create" method="post">
        % if 'collision' in room_dict:
            <div><span><h4>Collision occured. Please take another date range</h4></span></div>
        % endif
        <input type="hidden" name="room_id" value="${room_dict['id']}">
        <label for="date_start">Date Start:</label>
        <input pattern="\d{4}/\d{2}/\d{2}" name="date_start" id="date_start" class="form-control" placeholder="2016/11/18" type="text">
        <label for="date_end">Date End:</label>
        <input pattern="\d{4}/\d{2}/\d{2}" name="date_end" id="date_end" class="form-control" placeholder="2016/11/21" type="text">
        <button class="btn btn-lg btn-primary btn-block" type="submit">Reserve</button>
    </form>
</div>
</body>
</html>