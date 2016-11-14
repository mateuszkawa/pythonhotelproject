<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="/assets/bootstrap/css/bootstrap.min.css" rel="stylesheet"/>
    <title>Main</title></head>
<body> <%include file="shared/menu.mako"/>
<div class="container">
    <table class="table table-striped">
        <thead>
        <tr>
            <th>Room Name</th>
            <th>Date From</th>
            <th>Date To</th>
            <th>State</th>
            <th>Pay</th>
            <th>Cancel</th>
        </tr>
        </thead>
        <tbody>
        % for room in room_dict:
        <tr>
            <td>${room_dict[room]['name']}</td>
            <td>${str(room_dict[room]['date_from'])}</td>
            <td>${str(room_dict[room]['date_to'])}</td>
            <td>${room_dict[room]['state']}</td>
            % if room_dict[room]['pay']:
                <td>Already Payed</td>
            % else:
                <td><a href="/reservation/pay/${str(room_dict[room]['id'])}">PAY</a></td>
            % endif
            <td><a href="/reservation/cancel/${str(room_dict[room]['id'])}">CANCEL</a></td>
        </tr>
        % endfor
        </tbody>
    </table>
</div>
</body>
</html>