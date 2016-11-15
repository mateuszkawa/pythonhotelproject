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
            <th>Pay</th>
            <th>Cancel</th>
        </tr>
        </thead>
        <tbody>
        % for client in client_dict:
            % for state in client_dict[client]['roomstates']:
            <tr>
                <td>${client_dict[client]['roomstates'][state]['room_name']}</td>
                <td>${str(client_dict[client]['roomstates'][state]['reserved_from'])}</td>
                <td>${str(client_dict[client]['roomstates'][state]['reserved_to'])}</td>
                <td>${client_dict[client]['roomstates'][state]['state']}</td>
                % if client_dict[client]['roomstates'][state]['pay']:
                    <td>Already Payed</td>
                % else:
                    <td><a href="/administrators/showreservations/pay/${str(state)}">PAY</a></td>
                % endif
                <td><a href="/administrators/showreservations/cancel/${str(state)}">CANCEL</a></td>
            </tr>
            % endfor
        % endfor
        </tbody>
    </table>
</div>
</body>
</html>