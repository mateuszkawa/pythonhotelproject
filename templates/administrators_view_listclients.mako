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
        </tr>
        </thead>
        <tbody>
        % for client in client_dict:
        <tr>
            <td><a href="/administrators/edit/${client_dict[client]['id']}">${client_dict[client]['name']}</a></td>
            <td><a href="/administrators/edit/${client_dict[client]['id']}">${client_dict[client]['surname']}</a></td>
        </tr>
        % endfor
        </tbody>
    </table>
</div>
</body>
</html>