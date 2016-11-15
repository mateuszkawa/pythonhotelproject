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
            <th>Client Name</th>
            <th>Client Surname</th>
            <th>Room Name</th>
            <th>Date From</th>
            <th>Date To</th>
            <th>State</th>
        </tr>
        </thead>
        <tbody>
        % for state in state_dict_unpayed_dict:
        <tr>
            <td>${client_dict[state_dict_unpayed_dict[state]['client_id']]['client_name']}</td>
            <td>${client_dict[state_dict_unpayed_dict[state]['client_id']]['client_surname']}</td>
            <td>${state_dict_unpayed_dict[state]['room_name']}</td>
            <td>${state_dict_unpayed_dict[state]['reserved_from']}</td>
            <td>${state_dict_unpayed_dict[state]['reserved_to']}</td>
            <td>${state_dict_unpayed_dict[state]['state']}</td>
        </tr>
        % endfor
        % for state in state_dict_payed_dict:
        <tr>
            <td>${client_dict[state_dict_payed_dict[state]['client_id']]['client_name']}</td>
            <td>${client_dict[state_dict_payed_dict[state]['client_id']]['client_surname']}</td>
            <td>${state_dict_payed_dict[state]['room_name']}</td>
            <td>${state_dict_payed_dict[state]['reserved_from']}</td>
            <td>${state_dict_payed_dict[state]['reserved_to']}</td>
            <td>${state_dict_payed_dict[state]['state']}</td>
        </tr>
        % endfor
        </tbody>
    </table>
</div>
</body>
</html>