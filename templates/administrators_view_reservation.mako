<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="/assets/bootstrap/css/bootstrap.min.css" rel="stylesheet"/>
    <title>Main</title></head>
<body> <%include file="shared/menu.mako"/>
<div class="container">
    <form action="/administrators/reservation/make" method="post">
        <div class="form-group">
            <label for="sel1">Select Client:</label>
            <select class="form-control selectpicker" id="sel1" data-live-search="true" name="user_id">
                % for client in client_dict:
                    <option value="${client_dict[client]['id']}" data-tokens="${client_dict[client]['name']} ${client_dict[client]['surname']}">${client_dict[client]['name']} ${client_dict[client]['surname']}</option>
                % endfor
            </select>
        </div>
        <div class="form-group">
            <label for="sel2">Select Room:</label>
            <select class="form-control selectpicker" id="sel2" data-live-search="true" name="room_id">
                % for room in rooms_dict:
                    <option value="${rooms_dict[room]['id']}" data-tokens="${rooms_dict[room]['name']}">${rooms_dict[room]['name']}</option>
                % endfor
            </select>
        </div>
        % if collision == 'val':
            <div><span><h4>Collision occured. Please take another date range</h4></span></div>
        % endif
        <label for="date_start">Date Start:</label>
        <input pattern="\d{4}/\d{2}/\d{2}" name="date_start" id="date_start" class="form-control" placeholder="2016/11/18" type="text">
        <label for="date_end">Date End:</label>
        <input pattern="\d{4}/\d{2}/\d{2}" name="date_end" id="date_end" class="form-control" placeholder="2016/11/21" type="text">
        <button class="btn btn-lg btn-primary btn-block" type="submit">Reserve</button>
    </form>
</div>
</body>
</html>